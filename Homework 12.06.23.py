# Magazyn to jest lista slownikow
# Magazyn_1 to jest slownik z klucza (nazwa) slownikow
saldo = 8000.0
magazyn = {
    'rower': {
        'ilosc': 2,
        'cena': 100
    },
    'lodka': {
        'ilosc': 3,
        'cena': 1500
    }
}
history = []
new_product = None
new_amount = None
new_saldo = None
product = None
initial_message = 'Witaj w Twoim magazynie. Lista dostepnych komend to:\n' \
                  ' 1. Saldo\n 2. Sprzedaz\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przeglad\n 8. Koniec'

end_program = False
while not end_program:
    print(initial_message)
    operation = input('Podaj operacje ktora chcesz wykonac: ')
    # TODO: Przerobic ponizszy if na match_case
    if operation == '1':
        amount = float(input('Podaj kwote, ktora chcesz dodac lub ujac z konta: '))
        saldo += amount
        # Jezeli chcemy odjac, to dajemy kwote ujemna
        # TODO poprosic jeszcze o rodzaj operacji: czy dodajemy, czy odejmujemy
        history.append(f'Wykonano instrukcje saldo, zasilono {amount}')
    if operation == '2':
        print(magazyn)
        product = str(input('Podaj nazwe produktu: '))
        # TODO zmienic na float, bo np kg.
        amount = int(input('Podaj ilosc produktow: '))
        product_found = False
        # Najpierw sprawdzmy, czy mamy towar
        for item, item_details in magazyn.items():  # Bez items byliby tylko kluczy.
            if product == item:
                item_details['ilosc'] -= amount
                saldo += (item_details['cena'] * amount)
                product_found = True
                history.append(f'Sprzedano {product} w ilosci {amount}')
                break
        if not product_found:
            history.append(f'Nie udalo sie sprzedac towaru {product}, mamy go za malo na magazynie')
            pass
    if operation == '3':
        print(magazyn)
        product = str(input('Podaj nazwe produktu: '))
        # TODO zmienic na float, bo np kg.
        amount = int(input('Podaj ilosc produktow: '))
        price = float(input('Podaj cene produktu: '))
        product_found = False
        # Najpierw sprawdzmy, czy mamy towar

        for item, item_details in magazyn.items():  # Bez items byliby tylko kluczy.
            if product == item:
                item_details['ilosc'] += amount
                saldo -= (item_details['cena'] * amount) and saldo > 0
                product_found = True

                history.append(f'Zakupiono {product} w ilosci {amount}')
                break
        if not product_found:

            new_product = input(
                f'Jeszcze nie mamy takiego produktu na magazynie.\nProsze ponownie podac nazwe produktu -\nzostanie on wpisany do naszej bazy danych: ')
            new_amount = int(input(f'Prosze podac ilosc produktu: '))
            price_to_pay = price * new_amount

                #tutaj musisz stworzyc nowy produkt tylko, ze bez fora
            if saldo - price_to_pay > 0:
                print(f'Zakupiono {new_product} w ilosci {new_amount} sztuk')
                magazyn[new_product] = {}
                magazyn[new_product]['ilosc'] = new_amount
                magazyn[new_product]['cena'] = price
                new_saldo = saldo - price_to_pay


                product_found = False
                history.append(f'Zakupiono {new_product} w ilosci {new_amount} sztuk')
            else:
                print("Niestety nie stać Cię na zakup tego produktu")


        # program pobiera nazwe produktu, cene oraz liczbe sztuk.
    # produkt zostaje dodany do magazynu, jesli go nie bylo
    # Obliczenia są wykonane odwrotnie do komendy "sprzedaz".
    # Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
    # - Dodac produkt do magazynu
    # jesli prod, jest - dodac ilosc, jesli nie - dodac nowy produkt)
    # - Zmniejszyc stan konta
    if operation == '4':  # program wyswietla stan konta
        if saldo > 0:
            print(saldo)
        elif new_saldo > 0:
            print(new_saldo)
        else:
            print('Konto magazynu jest puste')

    if operation == '5':  # program wyswietla calkowity stan magazynu wraz z cenami produktow i ich iloscia
        print(magazyn)

    if operation == '6':
        searched_product = str(input("Prosze podac nazwe produktu: "))

        # Magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
        # dane wejsciowe - nazwa, wyszukiwac po nazwie
        pass
    # TODO zrobic For, porownac, czy mamy produkt.
    if operation == '7':
        # TODO jak value bedzie wieksze od naszej listy to wyprintowac dlugosc listy instrukcja len()
        value_from = input('Podaj poczatkowy zakres: ')
        value_to = input('Podaj koncowy zakres: ')
        if not value_to and not value_from:
            print(history)
        if value_from and not value_to:
            print(history[value_from:])
