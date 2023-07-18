
# Program do obslugi ladowarki paczek

parcels_amount = input(
    'Witamy w programie do obslugi ladowarki paczek! Podaj ilosc Twoich paczek (kazda paczka moze zawierac max. 20kg poszczegolnych elementow): ')
for number in parcels_amount:
    print('Zamowiono ' + number + ' paczki')
maximum_weight = 20
kilograms_sent = 0
stop_program = False
parcels_sent = 1  # Jezeli tu jest 1, to przy liczbie wagi elementow zawsze dodawany jest jeszcze jeden element,
# nie uwzgledniony w input i nie widoczny na koncu rozliczenia.
# Ale jezeli dac tu 0, to pewnie nie powiedzie sie formula *20, bo na 0 bedzie 0
parcel_weight = 0
parcel_number = 1
empty_kg_for_parcel = 20
biggest_gap_in_weight = 0
parcel_with_biggest_gap = 0
empty_kg_for_parcel = 20 - parcel_weight
while not stop_program:
    element_weight = float(input('Podaj wage elementu (przedzial wagi kazdego elementu 1-10kg): '))
    if element_weight > 10 or element_weight < 1:
        print(
            'Przekroczono wage elementu w zwiazku z czym nie moze byc on uwzgledniony i zostaje usuniety z listy. Program kończy swoją pracę.')
        stop_program = True
        break

    if parcel_weight + element_weight > 20:  # Ponad max. wage (dalej w tym wcieciu linia 67 itd)
        print(
            'Uwaga: Twoja paczka wazy juz ponad 20kg. W tym przypadku ostatni element z listy nadania zostanie przyniesiony do nastepnej paczki')

        if parcel_weight + element_weight > 20:
            if 20 - parcel_weight > biggest_gap_in_weight:
                biggest_gap_in_weight = 20 - parcel_weight
                parcel_with_biggest_gap = parcel_number
        if parcel_number == int(parcels_amount):
            print('Przekroczono ilosc zamowionych paczek: ostatni element z listy nie moze byc uwzgledniony')
            stop_program = True
            break
        parcel_weight = 0
        parcel_weight += element_weight
        parcel_number += 1
        parcels_sent += 1
        kilograms_sent += element_weight
    else:
        parcel_weight += element_weight
        kilograms_sent += element_weight

print(f'Wyslano kilogramow {kilograms_sent}')
print(f'Ilosc wyslanych paczek {parcels_sent}')
print(f'Paczka z najmniejsza waga to: {parcel_with_biggest_gap}, wazyla ona {20 - biggest_gap_in_weight}')
print('Zakonczylismy program')




