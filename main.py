import sys
import os
import requests

from weather import Weather

weather = Weather()

if sys.argv[1] == "weather":
    weather.check_weather()
elif sys.argv[1] == "lcd":
    lcd()
