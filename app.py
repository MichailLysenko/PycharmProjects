from flask import Flask, render_template, request, redirect, url_for, flash
import os

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


manager = Manager()


@app.route('/')
def index():
    manager.wczytaj_plik()  # Wczytujemy stan magazynu i saldo z plików
    return render_template('index.html', saldo=manager.saldo, magazyn=manager.magazyn)


@app.route('/zakup', methods=['POST'])
def zakup():
    nazwa_produktu = request.form['nazwa']
    cena = float(request.form['cena'])
    ilosc = int(request.form['ilosc'])

    total_cost = cena * ilosc

    if nazwa_produktu in manager.magazyn:
        if manager.saldo >= total_cost:
            manager.magazyn[nazwa_produktu]['ilosc'] += ilosc
            manager.saldo -= total_cost
            manager.history.append(f'Zakupiono {ilosc} szt. {nazwa_produktu}')
            flash(f'Zakupiono {ilosc} szt. {nazwa_produktu}')
        else:
            flash('Nie wystarczająca ilość środków na zakup.')
    else:
        if manager.saldo >= total_cost:
            manager.magazyn[nazwa_produktu] = {'ilosc': ilosc, 'cena': cena}
            manager.saldo -= total_cost
            manager.history.append(f'Zakupiono nowy produkt: {ilosc} szt. {nazwa_produktu}')
            flash(f'Zakupiono nowy produkt: {ilosc} szt. {nazwa_produktu}')
        else:
            flash('Nie wystarczająca ilość środków na zakup nowego produktu.')

    manager.zapisz_do_pliku()
    return redirect(url_for('index'))


@app.route('/sprzedaz', methods=['POST'])
def sprzedaz():
    nazwa_produktu = request.form['nazwa']
    ilosc = int(request.form['ilosc'])

    if nazwa_produktu in manager.magazyn and manager.magazyn[nazwa_produktu]['ilosc'] >= ilosc:
        manager.magazyn[nazwa_produktu]['ilosc'] -= ilosc
        manager.saldo += manager.magazyn[nazwa_produktu]['cena'] * ilosc
        manager.history.append(f'Sprzedano {ilosc} szt. {nazwa_produktu}')
        flash(f'Sprzedano {ilosc} szt. {nazwa_produktu}')
    else:
        flash(f'Nie można sprzedać {nazwa_produktu}, niewystarczająca ilość w magazynie.')

    manager.zapisz_do_pliku()
    return redirect(url_for('index'))


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


if __name__ == '__main__':
    app.run(debug=True)
