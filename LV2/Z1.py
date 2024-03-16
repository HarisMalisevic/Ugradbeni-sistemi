from machine import Pin
from time import sleep

# Ovo rijesenje pretpostavlja da su 4 LED-a spojena
# na susjedne GP-pinove 
START_PIN = 16

while True:
    for i in range(0, 4, 1):
        Pin(START_PIN + i, Pin.OUT).on()
        sleep(1)
        Pin(START_PIN + i, Pin.OUT).off()
        sleep(1)
