# Notatki z lekcji
# pip install requests - zainstalowalem poprzez terminal
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
# 1. Pytanie o parametry
latitude = 50
longitude = 50
searched_date = "2024-03-28"
# 2. Budowa linku do zapytania
URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
# 3. Wysłanie zapytania
response = requests.get(URL) # Wysylamy zapytanie do API
response_data = response.json() # Zamiana otrzymanych danych na slownik
print(response_data)
print(response.json()["daily"]["rain_sum"][0])  # Dostajemy poszukiwany parametr

import json
with open ("weather_forecast.json", mode="w") as file_stream:
    json.dump(response_data, file_stream) # Sposob 1: Zapisanie poprzez dump()

# JSON zapisywanie i odczytywanie

some_list = [1, 3, 5, 7, 9]
with open ("some_list.json", mode="w") as file_stream:
    json.dump([f"Number:{number}" for number in some_list], file_stream) # Sposob 2: Zapisanie poprzez dumps()
    # Lista składana

for number in some_list:
    print(f"Number:{number}") # For przed przerobieniem na liste skladana

# Odczytywanie plikow json
"""
with open ("weather_forecast.json") as file_stream:
    response_data = file_stream.read()
    # response_data_dict = json.loads(response_data)
    response_data_dict = json.load(file_stream) # Odczytujemy dane JSON z pliku i zamieniamy na slownik.
print(response_data_dict)
print(response_data_dict["Latitude"])
"""
# json.dump(<dane wejsciowe>, <file_stream>) # Sluzy do zapisywania danych do pliku (wewnatrz kontekstu [with ...])
# json.load(<file_stream>) # Sluzy do odczytywania danych z pliku. Ale nie zawsze mamy dane w postaci pliku (wewnatrz kontekstu [with ...])
# json.loads() # Pozwala na zamiany stringa w postaci JSON na typ dict

response_data_str = response.text
print(type(response_data_str))
response_data_dict = json.loads(response_data_str) # .loads() pozwala zamienic str na dict
print(type(response_data_dict), response_data_dict)
response_data_dict["elevation"] = 123456789.0 # Jak mozemy zmodyfikowac dane

data_as_string = json.dumps(response_data_dict) # .dumps() zamienia slownik na string w postaci JSON
print(type(data_as_string), data_as_string)


"""
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=50&longitude=50&start_date=2024-03-28&end_date=2024-03-28")
print(response)
print(dir(response))
print(response.text)
print(response.json()["latitude"])
data_in_python = response.json()
print(data_in_python["timezone"])
"""
"""
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")
data_in_python = response.json()
#with open ("Data.json", mode="w") as file_stream:
    #response_json = json.load(response_dict)
   # file_stream.write(response.json)

print(data_in_python)


latitude = 50
longitude = 50
#searched_date = input(f"Prosze podac date, dla ktorej naleyz sprawdyic pogode. Prosze zachowac format daty 'rok-dzien-miesiac': ") # "2024-03-30"


searched_place = input(f"Prosze podac nazwe miejscowosci, dla ktorej nalezy sprawdzic pogode: ")
URL = f"https://openweathermap.org/find?q={searched_place}"
response = requests.get(f"https://openweathermap.org/find?q={searched_place}")
print(response.json())


#URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={searched_date}&end_date={searched_date}"

response = requests.get(URL)
print(response.json())

import json
some_list = [1, 3, 5, 7, 9]
with open ("some_list.json", mode = "w") as file_stream:
    json.dump(some_list, file_stream)
"""