import json
import requests
import geopy

should_overwrite_file = False

class WeatherForecast:

    def main(self):
        data = self.read_file()
        city, searched_date = self.get_users_data()
        should_overwrite_file = False
        if searched_date in data:
            value = data[searched_date]
        else:
            get_value = self.get_value()
            data[searched_date] = value
            should_overwrite_file = True
        result = self.is_going_to_rain(value)
        show_result = self.print_result(city, searched_date, result)
        if should_overwrite_file:
            with open("new_weather_forecast2.json", mode='w') as file_stream:
                json.dump(data, file_stream)


    def read_file(self):
        with open("new_weather_forecast2.json", mode="r") as file_stream:
            data = json.load(file_stream)
        print(data)
        return data

    def get_users_data(self):
        city = input("Podaj nazwę miasta dla którego chcesz sprawdzić pogodę: ")
        searched_date = input(
            "Podaj datę dla której chcesz sprawdzić pogodę. Proszę użyć formatu 'rok-miesiąc-dzień': ")
        return city, searched_date

    def get_value(self):

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
            response = requests.get(URL)  # Wysylamy zapytanie do API
            print(response.json()["daily"]["rain_sum"])
            #
            weather_forecast_result = response.json()["daily"]["rain_sum"]
            value = weather_forecast_result[0]
            data[searched_date] = value
            should_overwrite_file = True
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
        return print

    def overwrite_file(self):
        with open("new_weather_forecast2.json", mode='w') as file_stream:
            json.dump(self, file_stream)




