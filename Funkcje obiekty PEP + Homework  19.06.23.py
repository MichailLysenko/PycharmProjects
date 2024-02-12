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

# Utwórz program do zarządzania bazą szkolną.
# Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca)
# a także zarządzania nimi.

# Po uruchomieniu programu można wpisać jedną z następujących komend:
# utwórz, zarządzaj, koniec.

# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# Polecenie "koniec" - Kończy działanie aplikacji.

# Proces tworzenia użytkowników:

# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec.
# Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia
# (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie
# obsłużone) oraz nazwę klasy (np. "3C")
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela
# (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone),
# nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas,
# które prowadzi nauczyciel, aż do otrzymania pustej linii.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy
# (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone),
# a także nazwę prowadzonej klasy.
# Polecenie "koniec" - Wraca do pierwszego menu.

# Proces zarządzania użytkownikami:

# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec.
# Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C")
# program ma wypisać wszystkich uczniów, którzy należą do tej klasy,
# todo a także wychowawcę tejże klasy.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie
# lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać
# wszystkie klasy, które prowadzi nauczyciel.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać
# wszystkich uczniów, których prowadzi wychowawca.
# Polecenie "koniec" - Wraca do pierwszego menu.

# System do zarzadzania szkola
# Kilka typow menu
# Glowne i do tworzenia uzytkownikow a tak ze do zarzadzania uzytkownikami
# Wybrac strukture
# Skorzystac z funkcji

class Student:
    def __init__(self, name, surname, class_name):
        self.name = name
        self.surname = surname
        self.class_name = class_name

    def __repr__(self):
        return f"Imie = {self.name}, Nazwisko = {self.surname}, Klasa = {self.class_name}"


class Teacher:
    def __init__(self, name, surname, subject, class_name):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.class_name = class_name

    def __repr__(self):
        return f"Imie = {self.name}, Nazwisko = {self.surname}, Przedmiot = {self.subject}, Klasa = {self.class_name}"


class Educator:
    def __init__(self, name, surname, class_name):
        self.name = name
        self.surname = surname
        self.class_name = class_name

    def __repr__(self):
        return f"Imie = {self.name}, Nazwisko = {self.surname}, Klasa = {self.class_name}"

  #  def __repr__(self):
    #    return f"Imie = {self.name}, Nazwisko = {self.surname}, Przedmiót = {self.subject}, Klasy = {self.class_name}"


# TODO W domu zrobić klasy dla nauczyciela i wychowawcy i zmienili je w naszej szkole

students = [
    Student(name="Jan", surname="Nowak", class_name="2a"),
    Student(name="Piotr", surname="Kamienny", class_name="3a"),
    Student(name="Marlena", surname="Morska", class_name="7a"),
    Student(name="Konstanty", surname="Wysocki", class_name="5b"),
    Student(name="Stefan", surname="Brum", class_name="4b"),
    Student(name="Paweł", surname="Pacek", class_name="4a"),
    Student(name="Michał", surname="Krynicki", class_name="5b"),
    Student(name="Hanna", surname="Retecka", class_name="8a"),
    Student(name="Joanna", surname="Katarska", class_name="5b"),
    Student(name="Tomasz", surname="Prędky", class_name="6b"),
    Student(name="Jan", surname="Puszek", class_name="6a")

]

teachers = [
    Teacher(name='Andrzej', surname='Iwan', subject='WF', class_name=['1a', '2a']),
    Teacher(name='Paweł', surname='Strzelczyk', subject='Fizyka', class_name=['7a', '8a']),
    Teacher(name='Elżbieta', surname='Kowalska', subject='Geografia', class_name=['6a', '6b']),
    Teacher(name='Anna', surname='Kamińska', subject='Język Angielski', class_name=['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b']),
    Teacher(name='Helena', surname='Prosta', subject='Język Polski', class_name=['5a', '6a', '5b', '6b']),
    Teacher(name='Stanisław', surname='Kauer', subject='Plastyka', class_name=['7a', '8a']),
    Teacher(name='Mikołaj', surname='Wawrzyński', subject='Matematyka', class_name=['4a', '5a']),
    Teacher(name='Maria', surname='Wierna', subject='Biologia', class_name=['7a', '7b'])
]

educators = [
    Educator(name= "Włodzimierz", surname="Stefanczyk", class_name=["1a"]),
    Educator(name= "Andrzej", surname="Iwan", class_name=["2a"]),
    Educator(name= "Paweł", surname="Strzelczyk", class_name=["3a"]),
    Educator(name= "Elżbieta", surname="Kowalska", class_name=["1b"]),
    Educator(name= "Anna", surname="Kamińska", class_name=["2b"]),
    Educator(name= "Helena", surname="Prosta", class_name=["3b"]),
    Educator(name= "Stanisław", surname="Kauer", class_name=["4a"]),
    Educator(name= "Mikołaj", surname="Wawrzyński", class_name=["4b"]),
    Educator(name= "Maria", surname="Wierna", class_name=["5a"])
]
"""
our_school = {
    "klasy": {
        "1a": {
            "uczniowie": [Student(name="Jan", surname="Kowalski", class_name="1a")],
            "wychowawca": {
                "imie": "Marta",
                "nazwisko": "Daszek"
            }
        },
        "2a": {
            "uczniowie": [Student(name="Jan", surname="Nowak", class_name="2a")],
            "wychowawca": {
                "imie": "Marta",
                "nazwisko": "Daszek"
            }
        }
    },

    "nauczyciele": [Teacher(name='Andrzej', surname='Iwan', subject='WF', class_name=['1a', '2a'])],
    "wychowawcy": [Educator(name= "Włodzimierz", surname="Stefanczyk", class_name=["1a"])]
}


def create_new_grade(grade):
    our_school["klasy"][grade] = {
        "uczniowie": [],
        "wychowawca": {}
    }


def create_student_in_existing_class(name, surname, class_name):
    our_school["klasy"][class_name]["uczniowie"].append(Student(name=name, surname=surname, class_name=class_name))

def create_teacher_in_existing_class(name,surname,subject,class_name):
    our_school ["nauczyciele"][Teacher].append(Teacher(name=name, surname=surname, subject=subject, class_name=class_name))

def create_educator_in_existing_class(name,surname,class_name):
    our_school ["wychowawcy"][Educator].append(Educator(name=name, surname=surname, class_name=class_name))

def create_new_student(name, surname, class_name):
    our_school["klasy"][grade] = {
        "uczniowie": []
    }
def create_new_student(name, surname, class_name):
    class_exists = our_school.get("klasy").get(class_name)
    if not class_exists:
        create_new_class_name(class_name)
    create_student_in_existing_class(name, surname, class_name)

def create_new_teacher(name,surname, subject, class_name):
    teachers_exists = our_school.get("nauczyciele").get(class_name)
    if not teachers_exists:
        create_teacher_in_existing_class(name,surname,subject,class_name)

def create_new_educator(name,surname,class_name):
    educator_exists = our_school.get("wychowawcy").get(class_name)
    if not educator_exists:
        create_educator_in_existing_class(name,surname,class_name)


def find_grade_by_class_name(class_grade):
    for class_grade, grade in our_school["klasy"].items():
        if grade_number == class_number:
            return (f"Uczniowie to: {grade['uczniowie']} wychowawca to: {grade['wychowawca']}")
    return 'Niestety nie znaleziono Twojej klasy'


def find_class_teachers(class_name):
    found_teachers = []
    for Teacher in our_school.get('nauczyciele'):
        if class_name in Teacher.grades:
            found_teachers.append(Teacher)
    return found_teachers

def find_class_educators(class_name):
    found_educator = []
    for Educator in our_school.get("wychowawcy"):
        if class_name in Educator.grades:
            found_educator.append(Educator)
    return found_educator


def find_student_by_name(name, surname):
    our_text = ""
    for grade_number, grade in our_school['klasy'].items():
        for student in grade.get('uczniowie'):
            if name == student.name and surname == student.surname:
                teachers = find_class_teachers(grade_number)
                for teacher in teachers:
                    our_text += f'Nauczyciel: {teacher.name} {teacher.surname} z przedmiotem {teacher.subject}\n'
                return our_text
    return 'Niestety Twoja klasa nie ma żadnych zajęć'
"""

initial_menu = "Witaj w swojej szkole! Podaj proszę co chcesz zrobić:\n 1.Utwórz\n 2.Zarządzaj\n 3.Koniec\n"

create_menu = "Podaj, jakiego użytkownika chcesz utworzyć:\n 1.Uczeń\n 2.Nauczyciel\n 3.Wychowawca\n 4.Koniec\n"  # TODO Koncy porobic samodzielnie
manage_menu = "Podaj, kim chcesz zarządzać:\n 1.Klasa\n 2.Uczeń\n 3.Nauczyciel\n 4.Wychowawca\n 5.Koniec\n"
finish_program = False
while not finish_program:
    main_guess = input(initial_menu)
    if main_guess == "1":
        # Wchodzimy w tryb dodawania czegokolwiek do naszej szkoly
        create_input = input(create_menu)
        if create_input == "1":
            name = input("Podaj imię ucznia: ")
            surname = input("Podaj nazwisko ucznia: ")
            class_name = input("Podaj klasę ucznia: ")
            #create_new_student(name, surname, class_name)
            student = Student(name=name, surname=surname, class_name=class_name)
            students.append(student)
            print(student)
            print("Nowy uczeń został dodany do systemu")
            #print(our_school)
        elif create_input == "2":
            name = input("Podaj imie nauczyciela: ")
            surname = input("Podaj nazwisko nauczyciela:")
            subject = input("Podaj przedmiot nauczyciela: ")
            class_name = input("Podaj nazwe klasy nauczyciela: ")
            teacher = Teacher(name=name, surname=surname, subject=subject, class_name=class_name)
            teachers.append(teacher)
            print(teacher) #todo Tutaj przy wykonaniu "run" wychodzi wartosc numeryczna z nazwa galęzi(?) - chociaż przypadek identyczny z uczniami
            print("Nowy nauczyciel został dodany do systemu")
            #create_new_teacher(name, surname, subject, class_name)
            #print(our_school)
        elif create_input == "3":
            name = input ("Podaj imie wychowawcy: ")
            surname = input("Podaj nazwisko wychowawcy: ")
            class_name = input("Podaj klase wychowawcy: ")
            educator = Educator(name=name, surname=surname, class_name=class_name)
            educators.append(educator)
            print(educator)
            print("Nowy wychowawca został dodany do systemu")
            #create_new_educator(name, surname, class_name)
            #print(our_school)
        elif create_input == "4":
            print("Koniec działania programu")

    elif main_guess == "2":
        manage_input = int(input(manage_menu))
        if manage_input == 1:
            class_name = input("Podaj nazwę klasy: ")
            #1 Dziala na podstawie listy uczniow. Czy tu trzeba dodac wyszukiwanie po nauczycielach i wychowawcach?
            class_found = False
            for name_of_class in students:
                if name_of_class.class_name == class_name:
                    print(name_of_class)
                    class_found = True
            if not class_found:
                print("Nie znalieziono takiej klasy na podstawie przeglądu listy uczniów")
            class_found = False
            for name_of_class_by_edu in educators: #todo Czemu nie mozna wyciagnac danych o klasie z listy wychowawców?... Aaa - bo dla listy trzeba podac [wartosc] :D
                if name_of_class_by_edu.class_name == class_name or name_of_class_by_edu.class_name == [class_name]:
                    print(name_of_class_by_edu)
                    class_found = True
            if not class_found:
                print("Nie znalieziono takiej klasy na podstawie przeglądu listy wychowawców")
            #text_to_display = find_grade_by_class_number(class_name)
            #print(text_to_display)
        elif manage_input == 2:
            student_name = input('Podaj imię ucznia: ')
            student_surname = input('Podaj nazwisko ucznia: ')
            student_found = False
            # Specjalnie zmienilem indeks w forze na podobna nazwe do studenta, zeby uswiadomic, ze nazwa jest obojetna,
            # ale zeby tez nie stracic nawiazania do tematu. Bo w poprzednim przypadku "Student" nastapilo nadpisanie klasy.
            for pupil in students:
                if pupil.name == student_name and pupil.surname == student_surname:
                    print(pupil)
                    student_found = True
            if not student_found:
                print("Nie znaleziono takiego ucznia")
            #text = find_student_by_name(student_name, student_surname)
            #print(text)
        elif manage_input == 3:
            teachers_name = input('Podaj imię nauczyciela: ')
            teachers_surname = input('Podaj nazwisko nauczyciela: ')
            class_name = input("Podaj nazwę klasy: ")
            teacher_found = False
            for lector in teachers:
                if lector.name == teachers_name and lector.surname == teachers_surname or lector.class_name == [class_name]:
                    print(lector)
                    teacher_found = True
            if not teacher_found:
                print("Nie znaleziono takiego nauczyciela")
            #text_to_display = find_class_teachers(our_school)
            #print(text_to_display)
        elif manage_input == 4:
            educator_name = input('Podaj imię wychowawcy: ')
            educator_surname = input('Podaj nazwisko wychowawcy: ')
            educator_found = False
            for behaviorist in educators:
                if behaviorist.name == educator_name and behaviorist.surname == educator_surname:
                    print(behaviorist)
                    educator_found = True
            if not educator_found:
                print("Nie znaleziono takiego wychowawcy") #todo czemu zawsze wychodzi, ze nie ma takiego wychowawcy, nawet jak on jest? Załatwiono
            #text = find_class_educators(our_school)
            #print(text)
        elif manage_input == 5:
            print("Koniec dzialania programu")
    elif main_guess == "3":
        print("Koniec dzialania programu")


