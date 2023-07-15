'''
my_name = Michail
for letter in my_name:
    if letter == 'M':
        break
    print(letter)

for number in range (2,18,2):
    print(number)


my_job = input('Podaj swoja prace ')
match my_job:
    case 'Nauczyciel':
        print('Musisz miec spora wiedze z danego przedmiotu')
    case 'Kierowca':
        print('Musisz dobrze prowadzic pojazdy')
    case 'Tancerz':
        print('Musisz dobrze czuc rytm')
    case 'Polityk':
        print('Musisz dobrze klamac')
    case _:
        print(my_job + ' to również musi byc ciekawy zawod')


my_job = input('Podaj swoja prace ')
if my_job == 'Nauczyciel':
    print('Musisz miec spora wiedze z danego przedmiotu')
elif my_job == 'Kierowca':
    print('Musisz dobrze prowadzic pojazdy')
elif my_job == 'Tancerz':
    print('Musisz dobrze czuc rytm')
elif my_job == 'Polityk':
    print('Musisz dobrze klamac')
else:
    print(my_job + ' to również musi byc ciekawy zawod')
'''

#Program do obslugi ladowarki paczek

parcels_amount = input('Witamy w programie do obslugi ladowarki paczek! Podaj ilosc Twoich paczek (kazda paczka moze zawierac max. 20kg poszczegolnych elementow): ')
for number in parcels_amount:
    print('Zamowiono '+ number + ' paczki')
maximum_weight = 20
kilograms_sent = 0
stop_program = False
parcels_sent = 1 #Jezeli tu jest 1, to przy liczbie wagi elementow zawsze dodawany jest jeszcze jeden element,
# nie uwzgledniony w input i nie widoczny na koncu rozliczenia.
# Ale jezeli dac tu 0, to pewnie nie powiedzie sie formula *20, bo na 0 bedzie 0
parcel_weight = 0
parcel_number = 1
empty_kg_for_parcel = 20 #Bylo 20
biggest_gap_in_weight = 0 #= 0 (bylo) - Jak to jest mozliwe? Ok - pozniejsze '>' not supported between instances of 'float' and 'NoneType'
parcel_with_biggest_gap = 0 #Jeszcze sie okaze pozniej - none. Nie weszlo, to 0
empty_kg_for_parcel = 20 - parcel_weight
while not stop_program:
    element_weight = float(input('Podaj wage elementu (przedzial wagi kazdego elementu 1-10kg): '))
    if 10 > element_weight >= 1 and parcel_weight <= 20:
        stop_program = True
        #TODO zeby tutaj tez wykonac sprawdzenia wagi paczki i pustych kilogramow
    else:
        if element_weight > 10:
            print('Przekroczono wage elementu w zwiazku z czym nie moze byc on uwzgledniony i zostaje usuniety z listy. Prosze sproboj podac wage elementu ponownie')
            continue

        if parcel_weight + element_weight > 20: #Ponad max. wage (dalej w tym wcieciu linia 67 itd)
            print('Uwaga: Twoja paczka wazy juz ponad 20kg. W tym przypadku ostatni element z listy nadania zostanie przyniesiony do nastepnej paczki')


            if empty_kg_for_parcel > biggest_gap_in_weight:
                biggest_gap_in_weight = parcel_weight
                parcel_with_biggest_gap = parcel_number

            if parcel_number == int(parcels_amount):
                print('Przekroczono ilosc zamowionych paczek: ostatni element z listy nie moze byc uwzgledniony')
                stop_program = True
                break
            parcel_weight = 0
            parcel_weight += element_weight #To samo, co w linii 73
            parcel_number += 1
            parcels_sent += 1
            kilograms_sent += element_weight #To samo, co w linii 74
        else:
            parcel_weight += element_weight
            kilograms_sent += element_weight
            #TODO wykombinowac, jak zakonczyc program, kiedy nie chcemy juz podawac kolejnego elementu
            #Ilosc elementow jest podawana przez uzytkownika i powinna miescic sie wedlug ich wagi w paczkach po max. 20 kg.
            #Jezeli te kryteria sa uwzglednione w programie to program sie zakonczy sam.
print(f'Wyslano kilogramow {kilograms_sent}')
print(f'Ilosc wyslanych paczek {parcels_sent}')
print(f'Paczka z najmniejsza waga to: {parcel_with_biggest_gap}, wazyla ona {biggest_gap_in_weight}')
print('Zakonczylismy program')


'''
liczba_paczek_wyslanych
liczba_kilogramow_wyslanych
suma_pustych_kilogramow
paczka_najwiecej_pustych_kg
'''