# Andrew Bruckbauer
# 8/22/2020
# Distance Sensor Module
# Purpose of the code is to create a distance sensor
# https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/python-circuitpython
# See the example here for more details:
# https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# VL53L0X Adafruit Module

# Will print the sensed range/distance every second.
from time import sleep, strftime, time
import matplotlib.pyplot as plt
import board
import busio
import adafruit_vl53l0x
import RPI.GPIO as GPIO

button1=18 #Event 1
button2=27 #Event 2
button3=22 #Event 3

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def write(distance): #distance file
    with open("/home/pi/range.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(distance)))

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Main loop will read the range and print it every second. and record it
while True:
    distance = vl53.range

    print("Range: {0}mm".format(vl53.range))
    write(distance)
    plt.pause(1)
