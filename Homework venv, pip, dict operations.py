"""
Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:

Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
Istnieją trzy możliwe informacje dla opadów deszczu:
Będzie padać (dla wyniku większego niż 0.0)
Nie będzie padać (dla wyniku równego 0.0)
Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
Będzie padać
Nie będzie padać
Nie wiem
Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.

URL do API:
https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}

W URL należy uzupełnić parametry: latitude, longitude oraz searched_date
"""

import requests
import json
# GeoPy - Biblioteka do zwracania danych geograficznych na podstawie podanego miasta
import geopy

geolocator = geopy.Nominatim(user_agent="Homework_venv_pip_dict")
city = input("Podaj nazwę miasta dla którego chcesz sprawdzić pogodę: ")
location = geolocator.geocode(city)
print(location)
print(dir(location))
print(location.latitude)
print(location.longitude)

latitude = location.latitude
longitude = location.longitude
searched_date = input("Podaj datę dla której chcesz sprawdzić pogodę. Proszę użyć formatu 'rok-miesiąc-dzień': ")
# 2. Budowa linku do zapytania
URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
# 3. Wysłanie zapytania
response = requests.get(URL) # Wysylamy zapytanie do API
print(response.json()["daily"]["rain_sum"])

weather_forecast_result = response.json()["daily"]["rain_sum"]
element = weather_forecast_result[0]


with open("new_weather_forecast.json", mode="w", encoding="utf-8") as file_stream:


    print(f"W miejscowosci {city} w dniu {searched_date}")

    if element > 0.0:
        wynik = "będzie padać"
        print(wynik)
    elif element == 0.0:
        print(f"nie będzie padać")
    else:
        print("Nie wiem")

    # Przepisac wynik do zmiennej

    json.dump(weather_forecast_result, file_stream)
    json.dump([f"W miejscowosci {city} w dniu {searched_date}" for element in weather_forecast_result], file_stream) #encoding="UTF8")

#response_data = response.json() # Zamiana otrzymanych danych na slownik
#print(response_data)
