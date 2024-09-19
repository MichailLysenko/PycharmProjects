# Zadanie alternatywne:
# Napisz kod implementujący silnię oraz dekorator mierzący czas obliczenia.
# Wyniki dla różnych wywołań zapisz w pliku tekstowym w formacie:
# "Czas obliczenia silnii dla wartości {value} wynosi {calculation_time}".
#
# Silnia dla wartości 3: 1 * 2 * 3
# Silnia dla wartości 7: 1 * 2 * 3 * 4 * 5 * 6 * 7
#
# + Opcjonalnie dodać mechanizm cache'owania
#
# Zadanie należy sprawdzić dla wartości: 1, 9, 27, 88, 175, 299, 512, 1024

import time


# Dekorator mierzący czas wykonania
def time_decorator(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        start_time = time.time()  # Zaczynamy pomiar czasu
        result = func(n)
        end_time = time.time()  # Kończymy pomiar czasu
        calculation_time = end_time - start_time

        # Zapis wyniku do pliku
        with open("wyniki_silnia.txt", mode="a") as file:
            file.write(f"Czas obliczenia silnii dla wartości {n} wynosi {calculation_time:.10f} sekund\n")

        cache[n] = result
        return result

    return wrapper


# Funkcja obliczająca silnię
@time_decorator
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


# Testowanie dla podanych wartości
values_to_test = [1, 9, 27, 88, 175, 299, 512, 1024]

for value in values_to_test:
    print(f"Silnia dla {value} wynosi {silnia(value)}")