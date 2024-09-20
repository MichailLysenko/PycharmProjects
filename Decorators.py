# Rozbuduj program do zarządzania firmą.
# Wszystkie funkcjonalności (komendy, zapisywanie i czytanie przy użyciu pliku itp.) pozostają bez zmian.
# Stwórz clasę Manager, która będzie implementowała dwie kluczowe metody - execute i assign.
# Przy ich użyciu wywołuj poszczególne fragmenty aplikacji.
# Metody execute i assign powinny zostać zaimplementowane zgodnie z przykładami z materiałów do zajęć.
#
# Niedozwolone są żadne zmienne globalne, wszystkie dane powinny być przechowywane wewnątrz obiektu Manager.
# 1
# Postep refaktoryzacji:
# Przejzenie kodu i podzial jego struktury wzgledem dalszego grupowania w bloki - refaktoryzacja
# Dopasowanie blokow wzgledem ich funkcjonalnosci do metod execute i assign.
# Umozliwienie dzialania kodu.
# 2
# Podział na bloki:
# ' 1. Saldo\n 2. Sprzedaz\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przeglad\n 8. Koniec'
# Manager - stale wartosci - Saldo, magazyn, historia
# Execute - zakup (czynnosc), przeglad
# Assign - przypisanie czynnosci do komend

# PROBLEMY[8]:
# 1. Błędne odwołanie do zmiennej end_program v
# 2. Błędne odwołanie do zmiennej saldo  v
# 3. Problem z pętlą while i brakiem case w bloku if
# 4. Brak obsługi zakończenia programu  v
# 5. Błędne użycie metod statycznych i self  v
# 6. Poprawne wywołanie main i instancji klasy
# 7. Poprawienie logicznych błędów
# 8. Pętla w metodzie execute_commands

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
















