#!/bin/bash

BASE_GPIO_PATH=/sys/class/gpio
RED=23
ON="1"

if [ ! -e $BASE_GPIO_PATH/gpio$RED ]; then
  echo $RED > $BASE_GPIO_PATH/export
fi

echo "out" > $BASE_GPIO_PATH/gpio$RED/direction
echo $ON > $BASE_GPIO_PATH/gpio$RED/value

python3 main.py weather
python3 main.py lcd
echo "Lights on"
