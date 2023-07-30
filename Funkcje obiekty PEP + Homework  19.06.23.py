'''
def check_whether_user_has_shortened_work_time(users_job):
    return users_job in ['Policjant', 'Strazak', 'Zolnierz'] #zwroci tu wartosc albo true albo false

def check_my_age(users_age, users_job='Programista', *args, *kwargs):
    print(args)
    for argument in args:
        print(argument)
        if argument > 3999:
            print('Masz dobrze platna prace')
    for key, in value in kwargs.items():
        print(f"{key}: {value}")
    #Argument do funkcji (users_age). Tu mamy definicje, a nie wywolanie funkcji, dlatego jest ona podana na poczatku.
    if check_whether_user_has_shortened_work_time(users_job):
        if 18 > users_age:
            return('Nie powinienes jeszcze pracowac')
        elif 18 < users_age < 65:
            return('Jestes w stanie pracowac')
        else:
            return('Jestes w wieku emerytalnym')
    else:
        if users_job == 'Nauczyciel':
            return 'Jestes nauczycielem'
        return 'Nie weszlismy w zaden warunek'

my_job = input('Podaj swoja prace: ')
my_age = int(input('Podaj swoj wiek: '))

if my_job == 'Konserwator':
    displayed_text = check_my_age(my_age, my_job, pensja_konserwatora=4000)
elif my_job == 'Programista':
    displayed_text = check_my_age(my_age, liczba_projektow=24)
elif my_job == 'Nauczyciel':
    displayed_text = check_my_age(my_age, my_job)
else:
    displayed_text = check_my_age(my_age, users_job=my_job)

print(displayed_text)

def check_my_grades(*args):
    for grade in args:
        if grade == 1:
            print('Dostales jedynke')
check_my_grades(1,2,3,1,5,6,3)
'''
#Obiektowosc. Klasy - to polaczenie zmiennych i funkcji

#Utwórz program do zarządzania bazą szkolną.
# Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca)
# a także zarządzania nimi.

#Po uruchomieniu programu można wpisać jedną z następujących komend:
#utwórz, zarządzaj, koniec.

#Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
#Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
#Polecenie "koniec" - Kończy działanie aplikacji.

#Proces tworzenia użytkowników:

#Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec.
#Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
#Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia
# (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie
# obsłużone) oraz nazwę klasy (np. "3C")
#Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela
# (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone),
# nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas,
# które prowadzi nauczyciel, aż do otrzymania pustej linii.
#Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy
# (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone),
# a także nazwę prowadzonej klasy.
#Polecenie "koniec" - Wraca do pierwszego menu.

#Proces zarządzania użytkownikami:

#Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec.
# Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
#Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C")
# program ma wypisać wszystkich uczniów, którzy należą do tej klasy,
# a także wychowawcę tejże klasy.
#Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie
# lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
#Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać
# wszystkie klasy, które prowadzi nauczyciel.
#Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać
# wszystkich uczniów, których prowadzi wychowawca.
#Polecenie "koniec" - Wraca do pierwszego menu.

#System do zarzadzania szkola
#Kilka typow menu
#Glowne i do tworzenia uzytkownikow a tak ze do zarzadzania uzytkownikami
#Wybrac strukture
#Skorzystac z funkcji

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __repr__(self):
        return f"Imie = {self.name}, Nazwisko = {self.surname}"

class Teacher:
    def __init__(self, name, surname, subject, grades):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.grades = grades
    def __repr__(self):
        return f"Imie = {self.name}, Nazwisko = {self.surname}, Przedmiót = {self.subject}, Klasy = {self.grades}"

# TODO W domu zrobić klasy dla nauczyciela i wychowawcy i zmienili je w naszej szkole

our_school = {
   "klasy": {
        "1a": {
            "uczniowie":[Student(name = "Jan", surname = "Kowalski")],
            "wychowawca":{
                "imie": "Marta",
                "nazwisko": "Daszek"
            }
        },
        "2a": {
            "uczniowie":[Student(name = "Jan", surname = "Nowak")]
            },
            "wychowawca":{
                "imie": "Marta",
                "nazwisko": "Daszek"
            }
        },

    "nauczyciele":[Teacher(name='Andrzej', surname='Iwan', subject='WF', grades=['1a', '2a'])]
    }

def create_new_grade(grade):
    our_school["klasy"] [grade] = {
        "uczniowie": [],
        "wychowawca": {}
    }
def create_student_in_existing_grade(name, surname, grade):
    our_school["klasy"][grade]["uczniowie"].append(Student(name=name, surname=surname))

def create_new_student(name, surname, grade):
    grade_exists = our_school.get("klasy").get(grade)
    if not grade_exists:
        create_new_grade(grade)
    create_student_in_existing_grade(name, surname, grade)

def find_grade_by_class_number(class_number):
    for grade_number, grade in our_school["klasy"].items():
        if grade_number == class_number:
            return(f"Uczniowie to: {grade['uczniowie']} wychowawca to: {grade['wychowawca']}")
    return 'Niestety nie znaleziono Twojej klasy'

def find_class_teachers(class_number):
    found_teachers = []
    for Teacher in our_school.get('nauczyciele'):
        if class_number in Teacher.grades:
            found_teachers.append(teacher)
    return found_teachers
def find_student_by_name(name,surname):
    our_text = ''
    for grade_number, grade in our_school['klasy'].items():
        for student in grade.get('uczniowie'):
            if name == student.name and surname == student.surname:
                teachers = find_class_teachers(grade_number)
                for teacher in teachers:
                    out_text += f'Nauczyciel: {teacher.name} {teacher.surname} z przedmiotem {teacher.subject}\n'
                return our_text
    return 'Niestety Twoja klasa nie ma żadnych zajęć'


initial_menu = "Witaj w swojej szkole! Podaj proszę co chcesz zrobić:\n 1.Utwórz\n 2.Zarządzaj\n 3.Koniec\n"
create_menu = "Podaj, jakiego użytkownika chcesz utworzyć:\n 1.Uczeń\n 2.Nauczyciel\n 3.Wychowawca\n 4.Koniec\n" #TODO Koncy porobic samodzielnie
manage_menu = create_menu = "Podaj, kim chcesz zarządzać:\n 1.Klasa\n 2.Uczeń\n 3.Nauczyciel\n 4.Wychowawca\n 5.Koniec\n"
finish_program = False
while not finish_program:
    main_guess = input(initial_menu)
    if main_guess == "1":
        # Wchodzimy w tryb dodawania czegokolwiek do naszej szkoly
        create_input = input(create_menu)
        if create_input == "1":
            name = input("Podaj imię ucznia: ")
            surname = input("Podaj nazwisko ucznia: ")
            grade = input("Podaj klasę ucznia: ")
            create_new_student(name, surname, grade)
            print(our_school)
    elif main_guess == "2":
        manage_input = input(manage_menu)
        if manage_input == 1:
            class_number = input("Podaj nazwę klasy: ")
            text_to_display = find_grade_by_class_number(class_number)
            print(text_to_display)
        elif manage_input == 2:
            student_name = input('Podaj imię ucznia: ')
            student_surname = input('Podaj nazwisko ucznia: ')
            text = find_student_by_name(student_name, student_surname)
            print(text)

