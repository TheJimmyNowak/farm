import sys
import os
import requests

from lcd import LCD
from weather import Weather

weather = Weather()
lcd = LCD()

if sys.argv[1] == "weather":
    weather.check_weather()
elif sys.argv[1] == "lcd":
    LCD.print(weather.get_actual_weather())
