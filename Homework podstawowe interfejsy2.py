import json
import requests
import geopy

class WeatherForecast:
    def __init__(self):
        self._data = self.read_file()

    def main(self):
        city, searched_date = self.get_users_data()
        should_overwrite_file = False
        if searched_date in self._data:
            value = self._data[searched_date]
        else:
            value = self.get_value(city, searched_date)
            self._data[searched_date] = value
            should_overwrite_file = True
        result = self.is_going_to_rain(value)
        self.print_result(city, searched_date, result)
        if should_overwrite_file:
            self.overwrite_file()

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def items(self):
        return self._data.items()

    def read_file(self):
        try:
            with open("new_weather_forecast2.json", mode="r") as file_stream:
                data = json.load(file_stream)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        print(data)
        return data

    def get_users_data(self):
        city = input("Podaj nazwę miasta dla którego chcesz sprawdzić pogodę: ")
        searched_date = input("Podaj datę dla której chcesz sprawdzić pogodę. Proszę użyć formatu 'rok-miesiąc-dzień': ")
        return city, searched_date

    def get_value(self, city, searched_date):
        geolocator = geopy.Nominatim(user_agent="Homework_venv_pip_dict")
        location = geolocator.geocode(city)
        print(location)
        latitude, longitude = location.latitude, location.longitude

        URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
        response = requests.get(URL)
        weather_forecast_result = response.json()["daily"]["rain_sum"]
        value = weather_forecast_result[0]
        return value

    def is_going_to_rain(self, value):
        if value > 0.0:
            result = "będzie padać"
        elif value == 0.0:
            result = "nie będzie padać"
        else:
            result = "nie mogę wskazać prognozu pogody"
        return result

    def print_result(self, city, searched_date, result):
        print(f"W miejscowosci {city} w dniu {searched_date} {result}")

    def overwrite_file(self):
        with open("new_weather_forecast2.json", mode='w') as file_stream:
            json.dump(self._data, file_stream)

weather_forecast = WeatherForecast()
weather_forecast.main()



