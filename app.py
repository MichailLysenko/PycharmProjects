from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Konfiguracja bazy danych (SQLite for development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firma.db'  # SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizacja bazy danych i migracji
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

app = Flask(__name__)
app.secret_key = 'supersecretkey'


# Menedżer stanu konta, magazynu i historii operacji
class Manager:
    def __init__(self):
        self.saldo = 8000.0
        self.magazyn = {
            'rower': {'ilosc': 2, 'cena': 100},
            'samochod': {'ilosc': 3, 'cena': 1500},
            'lodka': {'ilosc': 3, 'cena': 1500}
        }
        self.history = []

    def zapisz_do_pliku(self):
        with open("saldo.txt", mode="w") as file_stream:
            file_stream.write(str(self.saldo) + "\n")
        with open("magazyn.txt", mode="w") as file_stream:
            file_stream.write(str(self.magazyn) + "\n")

    def wczytaj_plik(self):
        if os.path.exists("saldo.txt"):
            with open("saldo.txt", mode="r") as file_stream:
                self.saldo = float(file_stream.read().strip())
        if os.path.exists("magazyn.txt"):
            with open("magazyn.txt", mode="r") as file_stream:
                self.magazyn = eval(file_stream.read().strip())

# Model dla stanu konta
class Konto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float, nullable=False, default=8000.0)

# Model dla produktów w magazynie
class Magazyn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, nullable=False)
    cena = db.Column(db.Float, nullable=False)

# Model dla historii operacji
class Historia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opis = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime, default=db.func.now())

manager = Manager()


@app.route('/')
def index():
    manager.wczytaj_plik()  # Wczytujemy stan magazynu i saldo z plików
    return render_template('index.html', saldo=manager.saldo, magazyn=manager.magazyn)


@app.route('/zakup', methods=['POST'])
def zakup():
    nazwa = request.form['nazwa']
    cena = float(request.form['cena'])
    ilosc = int(request.form['ilosc'])

    # Sprawdzenie, czy produkt już istnieje w magazynie
    produkt = Magazyn.query.filter_by(nazwa=nazwa).first()
    konto = Konto.query.first()

    koszt = cena * ilosc
    if konto.saldo >= koszt:
        if produkt:
            produkt.ilosc += ilosc
            produkt.cena = cena  # Możemy zaktualizować cenę
        else:
            nowy_produkt = Magazyn(nazwa=nazwa, ilosc=ilosc, cena=cena)
            db.session.add(nowy_produkt)

        konto.saldo -= koszt

        # Dodanie do historii
        historia = Historia(opis=f"Zakupiono {ilosc} sztuk {nazwa} za {koszt} PLN")
        db.session.add(historia)

        db.session.commit()
        flash('Zakup zakończony pomyślnie!')
    else:
        flash('Brak wystarczających środków na koncie.')

    return redirect('/')


@app.route('/sprzedaz', methods=['POST'])
def sprzedaz():
    nazwa = request.form['nazwa']
    ilosc = int(request.form['ilosc'])

    produkt = Magazyn.query.filter_by(nazwa=nazwa).first()
    konto = Konto.query.first()

    if produkt and produkt.ilosc >= ilosc:
        dochod = produkt.cena * ilosc
        produkt.ilosc -= ilosc
        konto.saldo += dochod

        # Dodanie do historii
        historia = Historia(opis=f"Sprzedano {ilosc} sztuk {nazwa} za {dochod} PLN")
        db.session.add(historia)

        db.session.commit()
        flash('Sprzedaż zakończona pomyślnie!')
    else:
        flash('Brak wystarczającej ilości towaru na magazynie.')

    return redirect('/')


@app.route('/zmiana_salda', methods=['POST'])
def zmiana_salda():
    kwota = float(request.form['kwota'])
    manager.saldo += kwota
    manager.history.append(f'Zmieniono saldo o kwotę: {kwota}')
    flash(f'Zmieniono saldo o kwotę: {kwota}')

    manager.zapisz_do_pliku()
    return redirect(url_for('index'))


@app.route('/historia/')
@app.route('/historia/<int:start>/<int:end>')
def historia(start=None, end=None):
    if start is None or end is None:
        return render_template('history.html', history=manager.history)
    elif start >= 0 and end <= len(manager.history):
        return render_template('history.html', history=manager.history[start:end])
    else:
        flash(f'Nieprawidłowy zakres. Zakres dostępnych operacji: 0 - {len(manager.history) - 1}')
        return redirect(url_for('historia'))


@app.route('/sprawdz_integralnosc')
def sprawdz_integralnosc():
    konto = Konto.query.first()
    operacje = Historia.query.all()

    saldo_obliczone = 8000.0  # Zakładamy początkowe saldo
    for operacja in operacje:
        if "Zakupiono" in operacja.opis:
            # Odczytanie wartości zakupu z historii
            kwota = float(operacja.opis.split()[-2])
            saldo_obliczone -= kwota
        elif "Sprzedano" in operacja.opis:
            # Odczytanie wartości sprzedaży
            kwota = float(operacja.opis.split()[-2])
            saldo_obliczone += kwota

    if saldo_obliczone == konto.saldo:
        return "Dane są zgodne"
    else:
        return f"Nieprawidłowe dane! Obliczone saldo: {saldo_obliczone}, Saldo w bazie: {konto.saldo}"

if __name__ == '__main__':
    app.run(debug=True)
