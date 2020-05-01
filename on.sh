#!/bin/bash

# Common path for all GPIO access
BASE_GPIO_PATH=/sys/class/gpio

# Assign names to GPIO pin numbers for each light
RED=23

# Assign names to states
ON="1"

if [ ! -e $BASE_GPIO_PATH/gpio$RED ]; then
  echo $RED > $BASE_GPIO_PATH/export
fi

echo "A"
# Utility function to set a pin as an output
echo "out" > $BASE_GPIO_PATH/gpio$RED/direction
echo $ON > $BASE_GPIO_PATH/gpio$RED/value
echo "Lights on"
mkdir test
