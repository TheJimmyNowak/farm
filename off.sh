#!/bin/bash

BASE_GPIO_PATH=/sys/class/gpio
RED=23
OFF="0"

if [ ! -e $BASE_GPIO_PATH/gpio$RED ]; then
  echo $RED > $BASE_GPIO_PATH/export
fi

echo "out" > $BASE_GPIO_PATH/gpio$RED/direction
echo $OFF > $BASE_GPIO_PATH/gpio$RED/value
echo "Lights off on pin" + $RED
