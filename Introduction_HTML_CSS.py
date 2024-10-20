
class Manager:

    def __init__(self):
        self.actions = {}
        self.saldo = 8000.0
        self.magazyn = {
            'rower': {
                'ilosc': 2,
                'cena': 100
            },
            'samochod': {
                'ilosc': 3,
                'cena': 1500
            },
            'lodka': {
                'ilosc': 3,
                'cena': 1500
            }
        }
        self.history = []
        self.end_program = False

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
            return cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print(f"Action '{name}' not defined")
        else:
            self.actions[name](self)

    def execute_commands(self):
        while not self.end_program:
            self.initial_message()
            operation = input('Podaj operację, którą chcesz wykonać: ')
            self.execute(operation)

    def initial_message(self):
        message = (
            "Witaj w Twoim magazynie. Lista dostępnych komend to:\n"
            " 1. Saldo\n 2. Sprzedaż\n 3. Zakup\n 4. Konto\n"
            " 5. Lista\n 6. Magazyn\n 7. Przegląd\n 8. Koniec"
        )
        print(message)

    def open_files(self):
        try:
            with open("saldo.txt", encoding="utf-8") as file_stream:
                saldo_text = file_stream.read()
                print(saldo_text)
            with open("Magazyn.txt", encoding="utf-8") as file_stream:
                magazyn_text = file_stream.read()
                print(magazyn_text)
        except FileNotFoundError:
            print("Brak plików saldo.txt lub Magazyn.txt")
        except UnicodeDecodeError as e:
            print(f"Błąd dekodowania pliku: {e}")

    def write_file(self):
        with open("saldo.txt", mode="w") as file_stream:
            file_stream.write(str(self.saldo) + "\n")
        with open("Magazyn.txt", mode="w") as file_stream:
            file_stream.write(str(self.magazyn) + "\n")


# Aktionen als dekorierte Funktionen
manager = Manager()


@manager.assign('1')
def saldo(manager):
    amount = float(input('Podaj kwotę, którą chcesz dodać lub ująć z konta. '
                         'Jeżeli chcesz ujmować, proszę podaj kwotę ujemną: '))
    manager.saldo += amount
    print(f"Konto zmieniono o kwotę {amount}, stan konta wynosi {manager.saldo}")
    manager.history.append(f'Wykonano instrukcję saldo, zasilono lub ujęto {amount}')
    manager.write_file()


@manager.assign('2')
def sprzedaz(manager):
    print(manager.magazyn)
    product = input('Podaj nazwę produktu: ')
    amount = int(input('Podaj ilość produktów: '))

    if product in manager.magazyn and manager.magazyn[product]['ilosc'] >= amount:
        manager.magazyn[product]['ilosc'] -= amount
        manager.saldo += manager.magazyn[product]['cena'] * amount
        manager.history.append(f'Sprzedano {product} w ilości {amount}')
        print(f'Sprzedano {product} w ilości {amount}')
    else:
        print(f'Nie udało się sprzedać towaru {product}, mamy go za mało na magazynie')


@manager.assign('3')
def zakup(manager):
    print(manager.magazyn)
    product = input('Podaj nazwę produktu: ')
    amount = int(input('Podaj ilość produktów: '))
    price = float(input('Podaj cenę produktu: '))

    if product in manager.magazyn:
        total_cost = price * amount
        if manager.saldo >= total_cost:
            manager.magazyn[product]['ilosc'] += amount
            manager.saldo -= total_cost
            manager.history.append(f'Zakupiono {product} w ilości {amount}')
            print(f'Zakupiono {product} w ilości {amount}')
        else:
            print("Niestety nie stać Cię na zakup tego produktu")
    else:
        total_cost = price * amount
        if manager.saldo >= total_cost:
            manager.magazyn[product] = {'ilosc': amount, 'cena': price}
            manager.saldo -= total_cost
            manager.history.append(f'Zakupiono nowy produkt {product} w ilości {amount}')
            print(f'Zakupiono nowy produkt {product} w ilości {amount}')
        else:
            print("Niestety nie stać Cię na zakup tego nowego produktu")


@manager.assign('4')
def konto(manager):
    print(f"Stan konta wynosi: {manager.saldo}")


@manager.assign('5')
def lista(manager):
    print("Stan magazynu:")
    for product, details in manager.magazyn.items():
        print(f"{product}: ilość = {details['ilosc']}, cena = {details['cena']}")


@manager.assign('6')
def magazyn(manager):
    searched_product = input("Proszę podać nazwę produktu: ")
    if searched_product in manager.magazyn:
        print(f"W magazynie znaleziono {searched_product}")
        manager.history.append(f'Znaleziono {searched_product}')
    else:
        print(f"Nie znaleziono {searched_product}")
        manager.history.append(f'Nie znaleziono {searched_product}')


@manager.assign('7')
def przeglad(manager):
    value_from = input('Podaj początkowy zakres: ')
    value_to = input('Podaj końcowy zakres: ')

    if not value_from and not value_to:
        print(manager.history)
    elif value_from and not value_to:
        print(manager.history[int(value_from):])
    elif value_from and value_to:
        print(manager.history[int(value_from):int(value_to)])


@manager.assign('8')
def koniec(manager):
    manager.end_program = True
    print("Zakończenie programu")


# Manager - wywolanie
manager.execute_commands()

# Zadanie polega na zaprojektowaniu strony głównej dla aplikacji
# do zarządzania magazynem i księgowością oraz podstrony "Historia".
#
# 1.Strona główna powinna zawierać następujące elementy:
#
# Wyświetlanie aktualnego stanu magazynowego i aktualnego salda.
# Trzy formularze:
# a. Formularz do zakupu: z polami: nazwa produktu, cena jednostkowa, liczba sztuk.
# b. Formularz do sprzedaży: z polami: nazwa produktu, cena jednostkowa, liczba sztuk.
# c. Formularz zmiany salda: z polami: komentarz, wartość (tylko liczbowa).
#
# 2.Podstrona "Historia"
#
# Podstrona powinna być dostępna pod adresem "/historia/" i "/historia/<line_from>/<line_to>/"
# Jeśli nie podano parametrów, powinna wyświetlać całą historię.
# Jeśli podano parametry, powinna wyświetlać dane z danego zakresu.
#
# 3.CSS
#
# Zapewnij przyjazny dla użytkownika interfejs, stosując style CSS.

<!DOCTYPE html>

<head>

<link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre.min.css">
<link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-exp.min.css">
<link rel="stylesheet" href="https://unpkg.com/spectre.css/dist/spectre-icons.min.css">

</head>

<img src="sciezka-do-plliku.jpg" />
<h1>Treść nagłówka</h1>
<h2>Treść nagłówka</h2>
<h3>Treść nagłówka</h3>
<h4>Treść nagłówka</h4>
<h5>Treść nagłówka</h5>
<h6>Treść nagłówka</h6>

<p>Paragraf teksu</p>

<div id="pierwszy-element" class="klasa-1 klasa-2 klasa-3"></div>

< form
method = "METODA"
action = "ADRES" > ...
Zawartość
formularza... < / form >

# Pole tekstowe - jedna linia:

<input type="text" name="nazwa pola" value="wartosc domyslna" />

# Pole tekstowe - tylko numery:

<input type="number" name="nazwa pola" value="wartosc domyslna" />

# Pole typu checkbox:

<input type="checkbox" name="nazwa pola" />

# Jeśli chcecie, żeby pole było domyślnie zaznaczone:

<input type="checkbox" checked="checked" name="nazwa pola" />

# Jeśli chcecie przekazać wartość niewidoczną dla użytkownika:

<input type="hidden" name="nazwa pola" value="wartosc pola" />

# Przycisk do wysłania formularza:

<input type="submit" value="Etykieta przycisku" />
# lub
<button type="submit">Etykieta Pola</button>

