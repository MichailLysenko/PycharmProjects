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

#Magazyn to jest lista slownikow
#Magazyn_1 to jest slownik z klucza (nazwa) slownikow
saldo = 8000.0
magazyn = [
    {
    'nazwa' : 'rower',
    'ilosc' : 2,
    'cena_jednostkowa' : 100
    },
]
magazyn_1 = {
    'rower':{
    'ilosc' : 2,
    'cena' : 100
    },
    'lodka':{
    'ilosc': 3,
    'cena' : 1500
    },
}

initial_message = 'Witaj w Twoim magazynie. Lista dostepnych komend to:\n'\
                  ' 1.Saldo\n 2.Sprzedaz\n 3.Zakup\n 4.Konto\n 5.Lista\n 6.Magazyn\n 7.Przeglad\n 8.Koniec'

end_program = False
while not end_program:
    print(initial_message)
    operation = input('Podaj operacje ktora chcesz wykonac: ')

#TODO: Przerobic ponizszy if na match_case

if operation ==