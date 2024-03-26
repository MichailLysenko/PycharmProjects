# Notatki z lekcji
# pip install requests - zainstalowalem poprzez terminal

import requests
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")
data_in_python = response.json()
print(data_in_python)


latitude = 50
longitude = 50
searched_date = "2024-03-30"
URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={searched_date}&end_date={searched_date}"
response = requests.get(URL)
print(response.json())

import json
some_list = [1, 3, 5, 7, 9]
with open ("some_list.json", mode = "w") as file_stream:
    json.dump(some_list, file_stream)