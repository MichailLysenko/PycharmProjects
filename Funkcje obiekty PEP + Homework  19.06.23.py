my_job = input('Podaj swoja prace: ')
my_age = int(input('Podaj swoj wiek: '))
def check_my_age():

if my_job == 'Konserwator':
    if my_age < 18:
        print('Nie powinienes jeszcze pracowac')
    elif 18 < my_age < 65:
        print('Jestes w stanie pracowac')
    else:
        print('Jestes w wieku emerytalnym')
elif my_job == 'Programista':
    if my_age < 18:
        print('Nie powinienes jeszcze pracowac')
    elif 18 < my_age < 65:
        print('Jestes w stanie pracowac')
    else:
        print('Jestes w wieku emerytalnym')
if my_job == 'Nauczyciel':
    if my_age < 18:
        print('Nie powinienes jeszcze pracowac')
    elif 18 < my_age < 65:
        print('Jestes w stanie pracowac')
    else:
        print('Jestes w wieku emerytalnym')
else:
    if my_age < 18:
        print('Nie powinienes jeszcze pracowac')
    elif 18 < my_age < 65:
        print('Jestes w stanie pracowac')
    else:
        print('Jestes w wieku emerytalnym')