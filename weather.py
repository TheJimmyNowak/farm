import requests
import os
import datetime

from file import CSVFile


class Weather:
    def __init__(self, dataset_file: CSVFile):
        self.dataset_file = dataset_file
        self._last_pressure = int(self.dataset_file.read(len(dataset_file)-1)["pressure"])
        self._last_humidity = int(self.dataset_file.read(len(dataset_file)-1)["humidity"])

    def check_weather(self):
        try:
            res = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?lat=49.784398&lon=22.751835&appid="
                + os.environ['OPEN_WEATHER_KEY']).json()
        except requests.HTTPError as err:
            print(err)
        
        self._last_pressure = res["main"]["pressure"]
        self._last_humidity = res["main"]["humidity"]
        self.dataset_file.append([[datetime.datetime.now(), self._last_pressure, self._last_humidity]])

    def get_weather_info(self):
        return str(str(datetime.datetime.now()) + str("\nPressure: {}\nHumidity: {}")
                   .format(self._last_pressure, self._last_humidity))
