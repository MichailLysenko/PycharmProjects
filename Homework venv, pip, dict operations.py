import json
import requests
import geopy
with open("new_weather_forecast2.json", mode="r") as file_stream:
    data = json.load(file_stream)
print(data)
searched_data = input("Podaj datę dla której chcesz sprawdzić pogodę. Proszę użyć formatu 'rok-miesiąc-dzień': ")
if searched_data in data:
    value = data[searched_data]
    # print(value)
    if value > 0.0:
        result = "będzie padać"
        print(result)
    elif value == 0.0:
        result = "nie będzie padać"
        print(result)
    else:
        result = "nie mogę wskazać prognozu pogody"

else:
    # URL do API:
    # https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}
    #
    # W URL należy uzupełnić parametry: latitude, longitude oraz searched_date
    # """
    #
    # import requests
    # import json
    # # GeoPy - Biblioteka do zwracania danych geograficznych na podstawie podanego miasta
    # import geopy

    geolocator = geopy.Nominatim(user_agent="Homework_venv_pip_dict")
    city = input("Podaj nazwę miasta dla którego chcesz sprawdzić pogodę: ")
    location = geolocator.geocode(city)
    print(location)
    print(dir(location))
    print(location.latitude)
    print(location.longitude)
    #
    latitude = location.latitude
    longitude = location.longitude
    searched_date = searched_data
    # # 2. Budowa linku do zapytania
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    # # 3. Wysłanie zapytania
    response = requests.get(URL) # Wysylamy zapytanie do API
    print(response.json()["daily"]["rain_sum"])
    #
    weather_forecast_result = response.json()["daily"]["rain_sum"]
    element_of_weather_result = weather_forecast_result[0]
    #
    #
    with open("new_weather_forecast2.json", mode="a", encoding="utf-8") as file_stream:
        if element_of_weather_result > 0.0:
            result = "będzie padać"
            print(result)
        elif element_of_weather_result == 0.0:
            result = "nie będzie padać"
            print(result)
        else:
            result = "nie mogę wskazać prognozu pogody"
    #
    #     # Przepisac wynik do zmiennej
    print(f"W miejscowosci {city} w dniu {searched_date} {result}")
    # new_data = json.dump(new_weather_forecast2, file_stream)
    file_stream.write(f"W miejscowosci {city} w dniu {searched_date} {result}\n") #Czy tutaj nalezy zmienic format odpowiedzi na dict? Tak, jak w pliku z danymi "New weather forecast2"
    # json.loads('searched_date'[value],)
    #     #json.dump(f"W miejscowosci {city} w dniu {searched_date} {result}", file_stream and "\n")
    #
    # #response_data = response.json() # Zamiana otrzymanych danych na slownik
    # #print(response_data)
    #pass
    #uruchomienie api

# # 1. Odczytanie pliku (bez sprawdzania żadnych warunków, samo odczytanie i zapisanie do zmiennej) przy użyciu biblioteki json
# # 2. Pobranie daty od użytkownika (poprzez input)
# # 3. Sprawdzenie czy pobrana data jest w odczytanych danych (klucz - data, wartosc - opady)
# # 4. Jeśli jest, wyświetlenie czy będzie padało czy nie
# # 5. Jeśli nie jest, wykonanie zapytania do API
# # 6. Zapisanie nowych danych do pliku (czyli do starych danych dodajesz nowe i zapisujesz w pliku przy użyciu biblioteki json)

# """
# Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:
#
# Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
# Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
# Istnieją trzy możliwe informacje dla opadów deszczu:
# Będzie padać (dla wyniku większego niż 0.0)
# Nie będzie padać (dla wyniku równego 0.0)
# Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
# Będzie padać
# Nie będzie padać
# Nie wiem
# Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.
#
# URL do API:
# https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}
#
# W URL należy uzupełnić parametry: latitude, longitude oraz searched_date
# """
#
# import requests
# import json
# # GeoPy - Biblioteka do zwracania danych geograficznych na podstawie podanego miasta
# import geopy
#
# with open("new_weather_forecast.json", mode="r", encoding="utf-8") as file_stream:
#
#     if searched_date == 0.0:
#         result = "będzie padać"
#         print(result)
#     elif element_of_weather_result == 0.0:
#         result = "nie będzie padać"
#     else:
#         result = "nie mogę wskazać prognozu pogody"
#
# geolocator = geopy.Nominatim(user_agent="Homework_venv_pip_dict")
# city = input("Podaj nazwę miasta dla którego chcesz sprawdzić pogodę: ")
# location = geolocator.geocode(city)
# print(location)
# print(dir(location))
# print(location.latitude)
# print(location.longitude)
#
# latitude = location.latitude
# longitude = location.longitude
# searched_date = input("Podaj datę dla której chcesz sprawdzić pogodę. Proszę użyć formatu 'rok-miesiąc-dzień': ")
# # 2. Budowa linku do zapytania
# URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
# # 3. Wysłanie zapytania
# response = requests.get(URL) # Wysylamy zapytanie do API
# print(response.json()["daily"]["rain_sum"])
#
# weather_forecast_result = response.json()["daily"]["rain_sum"]
# element_of_weather_result = weather_forecast_result[0]
#
#
# with open("new_weather_forecast.json", mode="a", encoding="utf-8") as file_stream:
#
#     if element_of_weather_result > 0.0:
#         result = "będzie padać"
#         print(result)
#     elif element_of_weather_result == 0.0:
#         result = "nie będzie padać"
#     else:
#         result = "nie mogę wskazać prognozu pogody"
#
#     # Przepisac wynik do zmiennej
#     print(f"W miejscowosci {city} w dniu {searched_date} {result}")
#     # json.dump(weather_forecast_result, file_stream)
#     file_stream.write(f"W miejscowosci {city} w dniu {searched_date} {result}\n")
#     #json.dump(f"W miejscowosci {city} w dniu {searched_date} {result}", file_stream and "\n")
#
# #response_data = response.json() # Zamiana otrzymanych danych na slownik
# #print(response_data)
# # 1. Odczytanie pliku (bez sprawdzania żadnych warunków, samo odczytanie i zapisanie do zmiennej) przy użyciu biblioteki json
# # 2. Pobranie daty od użytkownika (poprzez input)
# # 3. Sprawdzenie czy pobrana data jest w odczytanych danych (klucz - data, wartosc - opady)
# # 4. Jeśli jest, wyświetlenie czy będzie padało czy nie
# # 5. Jeśli nie jest, wykonanie zapytania do API
# # 6. Zapisanie nowych danych do pliku (czyli do starych danych dodajesz nowe i zapisujesz w pliku przy użyciu biblioteki json)