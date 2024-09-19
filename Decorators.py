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
        self.new_product = None
        self.new_amount = None
        self.new_saldo = None
        self.product = None
        self.end_program = False
        self.product_found = None

    def main(self):
        self.open_files()
        self.execute_commands()
        self.write_file()

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)

    def execute_commands(self):  # Odnosi się do uruchomienia kodu
        while not self.end_program:
            self.initial_message()
            operation = input('Podaj operacje, którą chcesz wykonać: ')
            match operation:
                case '1':  # SALDO
                    amount = float(input('Podaj kwotę, którą chcesz dodać lub ująć z konta. Jeżeli chcesz ujmować, proszę podaj kwotę ujemną: '))
                    self.saldo += amount
                    print(f"Konto zmieniono o kwotę {amount}, stan konta wynosi {self.saldo}")
                    self.history.append(f'Wykonano instrukcję saldo, zasilono lub ujęto {amount}')
                    print(self.history)
                    self.write_file()

                case '2':  # SPRZEDAŻ
                    print(self.magazyn)
                    self.product = str(input('Podaj nazwę produktu: '))
                    amount = int(input('Podaj ilość produktów: '))
                    self.product_found = False

                    for item, item_details in self.magazyn.items():
                        if self.product == item:
                            if item_details['ilosc'] >= amount:
                                item_details['ilosc'] -= amount
                                self.saldo += (item_details['cena'] * amount)
                                self.product_found = True
                                self.history.append(f'Sprzedano {self.product} w ilości {amount}')
                                print(f'Sprzedano {self.product} w ilości {amount}')
                            else:
                                print(f'Nie udało się sprzedać towaru {self.product}, mamy go za mało na magazynie')
                            break

                    if not self.product_found:
                        self.history.append(f'Nie udało się sprzedać towaru {self.product}, mamy go za mało na magazynie lub nie mamy wcale')

                case '3':  # ZAKUP
                    print(self.magazyn)
                    self.product = str(input('Podaj nazwę produktu: '))
                    amount = int(input('Podaj ilość produktów: '))
                    price = float(input('Podaj cenę produktu: '))
                    self.product_found = False

                    for item, item_details in self.magazyn.items():
                        if self.product == item:
                            if self.saldo >= item_details['cena'] * amount:
                                item_details['ilosc'] += amount
                                self.saldo -= item_details['cena'] * amount
                                self.product_found = True
                                self.history.append(f'Zakupiono {self.product} w ilości {amount}')
                                print(f'Zakupiono {self.product} w ilości {amount}')
                            else:
                                print("Niestety nie stać Cię na zakup tego produktu")
                            break

                    if not self.product_found:
                        self.new_product = input(
                            'Jeszcze nie mamy takiego produktu na magazynie.\nProszę ponownie podać nazwę produktu - zostanie on wpisany do naszej bazy danych: ')
                        self.new_amount = int(input('Proszę podać ilość produktu: '))
                        price_to_pay = price * self.new_amount

                        if self.saldo - price_to_pay >= 0:
                            print(f'Zakupiono {self.new_product} w ilości {self.new_amount} sztuk')
                            self.magazyn[self.new_product] = {'ilosc': self.new_amount, 'cena': price}
                            self.saldo -= price_to_pay
                            self.history.append(f'Zakupiono {self.new_product} w ilości {self.new_amount} sztuk')
                        else:
                            print("Niestety nie stać Cię na zakup tego produktu")

                case '4':  # KONTO
                    print(f"Stan konta wynosi: {self.saldo}")

                case '5':  # LISTA
                    print("Stan magazynu:")
                    for product, details in self.magazyn.items():
                        print(f"{product}: ilość = {details['ilosc']}, cena = {details['cena']}")

                case '6':  # MAGAZYN
                    searched_product = str(input("Proszę podać nazwę produktu: "))
                    if self.magazyn.get(searched_product):
                        print(f"W magazynie znaleziono {searched_product}")
                        self.history.append(f'Znaleziono {searched_product}')
                    else:
                        print(f"Nie znaleziono {searched_product}")
                        self.history.append(f'Nie znaleziono {searched_product}')
                        with open("magazyn.txt", mode="w") as file_stream:
                            file_stream.writelines(f"W magazynie nie znaleziono {searched_product}\n")

                case '7':  # PRZEGLĄD
                    value_from = input('Podaj początkowy zakres: ')
                    value_to = input('Podaj końcowy zakres: ')
                    if not value_from and not value_to:
                        print(self.history)
                    elif value_from and not value_to:
                        print(self.history[int(value_from):])
                    elif value_from and value_to:
                        print(self.history[int(value_from):int(value_to)])

                case '8':  # ZAKOŃCZ PROGRAM
                    self.end_program = True
                    print("Zakończenie programu")

    def open_files(self):
        try:
            with open("saldo.txt", encoding="utf-8") as file_stream:
                written_text_first = file_stream.read()
                print(written_text_first)
            with open("Magazyn.txt", encoding="utf-8") as file_stream:
                written_text_second = file_stream.read()
                print(written_text_second)
        except FileNotFoundError:
            print("Brak plików saldo.txt lub Magazyn.txt")
        except UnicodeDecodeError as e:
            print(f"Błąd dekodowania pliku: {e}")

    def write_file(self):
        with open("saldo.txt", mode="w") as file_stream:
            file_stream.writelines(str(self.saldo) + "\n")
        with open("Magazyn.txt", mode="w") as file_stream:
            file_stream.writelines(str(self.magazyn) + "\n")

def initial_message(self):
    message = 'Witaj w Twoim magazynie. Lista dostępnych komend to:\n' \
                ' 1. Saldo\n 2. Sprzedaż\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przegląd\n 8. Koniec'
    print(message)
    return message

# Magazyn to jest lista słowników
# Magazyn_1 to jest słownik z klucza (nazwa) słowników

manager = Manager()
manager.initial_message
















