import json
import requests
import geopy


# 1 Odczytywanie pliku
with open("new_weather_forecast2.json", mode="r") as file_stream:
    data = json.load(file_stream)
print(data)
should_overwrite_file = False

# 2 Pobieranie danych od użytkownika
city = input("Podaj nazwę miasta dla którego chcesz sprawdzić pogodę: ")
searched_date = input("Podaj datę dla której chcesz sprawdzić pogodę. Proszę użyć formatu 'rok-miesiąc-dzień': ")

# 3 Pobieranie wartosci
if searched_date in data:
    value = data[searched_date]
else:
    # URL do API:
    # https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}
    # W URL należy uzupełnić parametry: latitude, longitude oraz searched_date

    geolocator = geopy.Nominatim(user_agent="Homework_venv_pip_dict")

    location = geolocator.geocode(city)
    print(location)
    print(dir(location))
    print(location.latitude)
    print(location.longitude)

    latitude = location.latitude
    longitude = location.longitude
    # 2. Budowa linku do zapytania
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    # 3. Wysłanie zapytania
    response = requests.get(URL) # Wysylamy zapytanie do API
    print(response.json()["daily"]["rain_sum"])
    #
    weather_forecast_result = response.json()["daily"]["rain_sum"]
    value = weather_forecast_result[0]
    data[searched_date] = value
    should_overwrite_file = True

# 4.1 Weryfikacja
if value > 0.0:
    result = "będzie padać"
elif value == 0.0:
    result = "nie będzie padać"
else:
    result = "nie mogę wskazać prognozu pogody"
#     # Przepisac wynik do zmiennej

# 4.2 Wyswietlenie wyniku
print(f"W miejscowosci {city} w dniu {searched_date} {result}")
# new_data = json.dump(new_weather_forecast2, file_stream)

# 5 Warunek nadpsisywania wartosci
if should_overwrite_file:
    with open("new_weather_forecast2.json", mode='w') as file_stream:
        json.dump(data, file_stream)

