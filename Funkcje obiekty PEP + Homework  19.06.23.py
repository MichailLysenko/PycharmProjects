def check_my_age(users_age, users_job=None):
    #Argument do funkcji (users_age). Tu mamy definicje, a nie wywolanie funkcji, dlatego jest ona podana na poczatku.
    if users_job not in ['Policjant', 'Strazak', 'Zolnierz']:
        if 18 < users_age:
            print('Nie powinienes jeszcze pracowac')
        elif 18 < users_age < 65:
            print('Jestes w stanie pracowac')
        else:
            print('Jestes w wieku emerytalnym')
    else:
        if 18 < users_age:
            print('Nie powinienes jeszcze pracowac')
        elif 18 < users_age < 45:
            print('Jestes w stanie pracowac')
        else:
            print('Jestes w wieku emerytalnym')
def check_whether_user_has_shortened_work_time(users_job):
    return users_job in ['Policjant', 'Strazak', 'Zolnierz']

my_job = input('Podaj swoja prace: ')
my_age = int(input('Podaj swoj wiek: '))

if my_job == 'Konserwator':
    check_my_age(my_age)
elif my_job == 'Programista':
    check_my_age(my_age)
elif my_job == 'Nauczyciel':
    check_my_age(my_age)
else:
    check_my_age(my_age)