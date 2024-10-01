from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Ścieżki do plików danych
SALDO_FILE = 'saldo.json'
MAGAZYN_FILE = 'magazyn.json'
HISTORIA_FILE = 'historia.json'


# Inicjalizacja danych
def init_data():
    if not os.path.exists(SALDO_FILE):
        with open(SALDO_FILE, 'w') as f:
            json.dump({"saldo": 8000.0}, f)
    if not os.path.exists(MAGAZYN_FILE):
        magazyn = {
            'rower': {'ilosc': 2, 'cena': 100},
            'samochod': {'ilosc': 3, 'cena': 1500},
            'lodka': {'ilosc': 3, 'cena': 1500}
        }
        with open(MAGAZYN_FILE, 'w') as f:
            json.dump(magazyn, f)
    if not os.path.exists(HISTORIA_FILE):
        with open(HISTORIA_FILE, 'w') as f:
            json.dump([], f)


# Wczytywanie danych
def load_data():
    with open(SALDO_FILE, 'r') as f:
        saldo = json.load(f)['saldo']
    with open(MAGAZYN_FILE, 'r') as f:
        magazyn = json.load(f)
    with open(HISTORIA_FILE, 'r') as f:
        historia = json.load(f)
    return saldo, magazyn, historia


# Zapisywanie danych
def save_data(saldo, magazyn, historia):
    with open(SALDO_FILE, 'w') as f:
        json.dump({"saldo": saldo}, f)
    with open(MAGAZYN_FILE, 'w') as f:
        json.dump(magazyn, f)
    with open(HISTORIA_FILE, 'w') as f:
        json.dump(historia, f)


@app.route("/", methods=['GET', 'POST'])
def index():
    saldo, magazyn, historia = load_data()

    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'zakup':
            produkt = request.form.get('produkt')
            cena = float(request.form.get('cena'))
            ilosc = int(request.form.get('ilosc'))
            total_cost = cena * ilosc
            if saldo >= total_cost:
                if produkt in magazyn:
                    magazyn[produkt]['ilosc'] += ilosc
                    magazyn[produkt]['cena'] = cena  # Aktualizacja ceny
                else:
                    magazyn[produkt] = {'ilosc': ilosc, 'cena': cena}
                saldo -= total_cost
                historia.append(f"Zakupiono {produkt}: {ilosc} szt. po {cena} zł każda.")
                save_data(saldo, magazyn, historia)
                return redirect(url_for('index'))
            else:
                return "Niewystarczające środki na zakup.", 400

        elif form_type == 'sprzedaz':
            produkt = request.form.get('produkt')
            cena = float(request.form.get('cena'))
            ilosc = int(request.form.get('ilosc'))
            if produkt in magazyn and magazyn[produkt]['ilosc'] >= ilosc:
                magazyn[produkt]['ilosc'] -= ilosc
                saldo += cena * ilosc
                historia.append(f"Sprzedano {produkt}: {ilosc} szt. po {cena} zł każda.")
                save_data(saldo, magazyn, historia)
                return redirect(url_for('index'))
            else:
                return "Nie można sprzedać podanej ilości lub produktu.", 400

        elif form_type == 'saldo':
            komentarz = request.form.get('komentarz')
            wartosc = float(request.form.get('wartosc'))
            saldo += wartosc
            historia.append(f"Zmiana salda: {komentarz}, wartość: {wartosc} zł.")
            save_data(saldo, magazyn, historia)
            return redirect(url_for('index'))

    return render_template('index.html', saldo=saldo, magazyn=magazyn)


@app.route("/historia/")
@app.route("/historia/<int:line_from>/<int:line_to>/")
def historia_view(line_from=None, line_to=None):
    _, _, historia = load_data()

    if line_from is not None and line_to is not None:
        selected_history = historia[line_from:line_to]
    else:
        selected_history = historia

    return render_template('historia.html', historia=selected_history)


if __name__ == "__main__":
    init_data()
    app.run(debug=True)
