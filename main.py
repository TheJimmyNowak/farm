import sys

from file import CSVFile
from lcd import LCD
from weather import Weather

dataset_file = CSVFile("dataset", ["date", "pressure", "humidity"])
weather = Weather(dataset_file)
lcd = LCD()

if sys.argv[1] == "weather":
    weather.check_weather()
elif sys.argv[1] == "lcd":
    pass
    #lcd.print(weather.get_weather_info())
