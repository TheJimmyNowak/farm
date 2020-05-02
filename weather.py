import requests
import os


class Weather:
    def __init__(self):
        self._pressure = 0
        self._humidity = 0

    def check_weather(self):
        try:
            res = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?lat=49.784398&lon=22.751835&appid="
                + os.environ['OPEN_WEATHER_KEY']).json()
        except requests.HTTPError:
            return
        finally:
            self._pressure = res["main"]["pressure"]
            self._humidity = res["main"]["humidity"]

    def get_actual_weather(self):
        return self._pressure, self._humidity
