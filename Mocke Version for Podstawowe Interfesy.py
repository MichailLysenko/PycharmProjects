import json
import requests
import geopy

with open("new_weather_forecast2.json", mode="r") as file_stream:
    data = json.load(file_stream)
print(data)

for data in data:
    print f"data:{})