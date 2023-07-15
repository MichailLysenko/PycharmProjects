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

parcels_amount = input('Witamy w programie do obslugi ladowarki paczek! Podaj proszę ilosc Twoich paczek: ')
maximum_weight = 20
kilograms_sent = 0
stop_program = False
parcels_sent = 1
parcel_weight = 0
parcel_number = 1
empty_kg_for_parcel = 20
biggest_gap_in_weight = 0
parcel_with_biggest_gap = None
while not stop_program:
    element = float(input('Podaj wage elementu: '))
    if 10 < element < 1:
        stop_program = True
        #TODO zeby tutaj tez wykonac sprawdzenia wagi paczki i pustych kilogramow
    else:
        if parcel_weight + element > 20:
            if 20 - parcel_weight > biggest_gap_in_weight:
                biggest_gap_in_weight = parcel_weight
                parcel_with_biggest_gap = parcel_number
            if parcel_number == int(parcels_amount):
                print('Niestety nie masz juz dostepnych paczek, element zostal usuniety')
                stop_program = True
                break
            parcel_weight = 0
            parcel_weight += element
            parcel_number += 1
            parcels_sent += 1
            kilograms_sent += element
        else:
            parcel_weight += element
            kilograms_sent += element
            #TODO wykombinowac, jak zakonczyc program, kiedy nie chcemy juz podawac kolejnego elementu
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