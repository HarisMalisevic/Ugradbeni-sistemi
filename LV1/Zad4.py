from time import sleep
from machine import Pin

T4 = Pin(3, Pin.IN)

LED7 = Pin(11, Pin.OUT)

while True:
    LED7.value(T4.value())
    sleep(0.001)

