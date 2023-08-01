'''
students = ['Marcin Brzeczyszczykiewicz', 'Michal Zietkowski', 'Maciej Dlugosz', 'Adam Wawszczyk', True, 11]
students.append('Marcin Zabawa')
students.insert(0, 'Ula Nowak')
print(students)
students_length = len(students)
print(students_length)
print(students[1:4])

students.remove('Marcin Brzeczyszczykiewicz')
print(students)
print(students.index('Michal Zietkowski'))

for student in students:
    print(type(student) == str)
for index, student in enumerate(students):
    print(index)

my_tuple = 1,2,3,False
print(id(my_tuple))
my_tuple_1 = tuple((1,2,3,False))
print(my_tuple)
print(my_tuple_1)


students_set = {'Michal Zietkowski', 'Jan Wojcik', 'Adam Nowak', 'Zbigniew Kot', 1, 2, False, 5}
print(students_set)
#print(students_set[0]) #To blokuje reszte ponizej, bo niewykonywalne

students_set.remove('Adam Nowak')
students_set.add('Ada Sliwa')
print(students_set)

students_dict = {
    'student_1':'Michal Zietkowski',
    'student_2':'Jan Wojcik',
    'student_3' : 'Adam Nowak'
}

print(students_dict['student_1'])

#Klucz i defaultowa funkcja
print(students_dict.get('student_4')) #'Michal Zietkowski'))
# Tu nie mozna robic przepisywania wartosci

for student in students_dict.values():
    if student == 'Michal Zietkowski':
        print(students_dict.keys())

for key, student in students_dict.items():
    if student == 'Michal Zietkowski':
        students_dict[key] = 'Teraz dziala'
# U mnie nie dziala
'''
#Saldo - program pobiera kwote do dodania lub odjecia z konta

# + dodajemy wpis do historii!
#Sprzedaz - program pobiera nazwe produktu, cene oraz liczbe sztuk.
    #produkt musi znajdowac sie na magazynie
    #Po wykonaniu operacji: 1) usunac produkt z magazynu, 2) dodac kwote do salda
  #W momencie, kiedy operacja sie nie powiedzie, i tak wpisujemy do historii,
  #Ale z informacja, ze operacja sie nie udala.
#Zakup - program pobiera nazwe produktu, cene oraz liczbe sztuk.
    #produkt zostaje dodany do magazynu, jesli go nie bylo
    #Obliczenia są wykonane odwrotnie do komendy "sprzedaz".
    #Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
    # - Dodac produkt do magazynu
        #jesli prod, jest - dodac ilosc, jesli nie - dodac nowy produkt)
    # - Zmniejszyc stan konta
#Konto - program wyswietla stan konta
#Lista - program wyswietla calkowity stan magazynu wraz z cenami produktow i ich iloscia
    #print
#Magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
    #dane wejsciowe - nazwa, wyszukiwac po nazwie
#TODO zrobic For, porownac, czy mamy produkt.
#Przeglad -  Program pobiera dwie zmienne „od” i „do”,
    #na ich podstawie wyświetla wszystkie wprowadzone akcje
    #zapisane pod indeksami od „od” do „do”.
    #Jeżeli użytkownik podał pustą wartość „od” lub „do”,
    #program powinien wypisać przegląd od początku lub/i do końca.
    #Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować
    #i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).

    #Jezeli chce sie wiecej operacji, niz sa dostepne, to podajemy blad i nazwy operacji do dyspozycji
    #W przyciwnym wypadku printujemy historie (liste)
    #TODO zrobic walidacje, jezeli value jest wieksze od naszej listy. Wyprintowac dlugosc listy (len)
#Koniec - Aplikacja konczy dzialanie

#Magazyn to jest lista slownikow
#Magazyn_1 to jest slownik z klucza (nazwa) slownikow
saldo = 8000.0
magazyn = {
    'rower': {
        'ilosc' : 2,
        'cena' : 100
    },
    'lodka': {
        'ilosc': 3,
        'cena' : 1500
    },
}
history = []
new_product = None
new_amount = None
initial_message = 'Witaj w Twoim magazynie. Lista dostepnych komend to:\n'\
                  ' 1. Saldo\n 2. Sprzedaz\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przeglad\n 8. Koniec'

end_program = False
while not end_program:
    print(magazyn)
    print(saldo)
    print(initial_message)
    operation = input('Podaj operacje ktora chcesz wykonac: ')
    #TODO: Przerobic ponizszy if na match_case
    if operation == '1':
        amount = float(input('Podaj kwote, ktora chcesz dodac lub ujac z konta: '))
        saldo += amount
        #Jezeli chcemy odjac, to dajemy kwote ujemna
        #TODO poprosic jeszcze o rodzaj operacji: czy dodajemy, czy odejmujemy
        history.append(f'Wykonano instrukcje saldo, zasilono {amount}')
    if operation == '2':
        print(magazyn)
        product = str(input('Podaj nazwe produktu: '))
        #TODO zmienic na float, bo np kg.
        amount = int(input('Podaj ilosc produktow: '))
        product_found = False
        #Najpierw sprawdzmy, czy mamy towar
        for item, item_details in magazyn.items(): #Bez items byliby tylko kluczy.
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

                new_product = str(input(f'Jeszcze nie mamy takiego produktu na magazynie.\nProsze ponownie podac nazwe produktu -\nzostanie on wpisany do naszej bazy danych: ')),
                new_amount = int(input(f'Prosze podac ilosc produktu: ')),
                print(f'Zakupiono{new_product} w ilosci {new_amount} sztuk')
                for item_details in magazyn.items():  # Bez items byliby tylko kluczy.
                    magazyn.items += new_product

                    saldo -= (item_details['cena'] * new_amount) and saldo > 0
                    product_found = False
                history.append(f'Zakupiono {new_product} w ilosci {new_amount} sztuk'),

        # program pobiera nazwe produktu, cene oraz liczbe sztuk.
    #produkt zostaje dodany do magazynu, jesli go nie bylo
    #Obliczenia są wykonane odwrotnie do komendy "sprzedaz".
    #Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
    # - Dodac produkt do magazynu
        #jesli prod, jest - dodac ilosc, jesli nie - dodac nowy produkt)
    # - Zmniejszyc stan konta
    if operation == '4': #program wyswietla stan konta
        pass
    if operation == '5': #program wyswietla calkowity stan magazynu wraz z cenami produktow i ich iloscia
    #print
        pass
    if operation == '6': #Magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
    #dane wejsciowe - nazwa, wyszukiwac po nazwie
        pass
#TODO zrobic For, porownac, czy mamy produkt.
    if operation == '7':
        #TODO jak value bedzie wieksze od naszej listy to wyprintowac dlugosc listy instrukcja len()
        value_from = input('Podaj poczatkowy zakres: ')
        value_to = input('Podaj koncowy zakres: ')
        if not value_to and not value_from:
            print(history)
        if value_from and not value_to:
            print(history[value_from:])
