from machine import Pin
from time import sleep

red = Pin(14, Pin.OUT)
green = Pin(12, Pin.OUT)
blue = Pin(13, Pin.OUT)


def setRGB(r, g, b):  # True / False (1 / 0)
    red.value(r)
    green.value(g)
    blue.value(b)


def permuteRGB(pauseTime):
    for r in [False, True]:
        for g in [False, True]:
            for b in [False, True]:
                setRGB(r, g, b)
                sleep(pauseTime)


def main():

    
    while True:
        pauseTime = 0.1
        
        while pauseTime <= 1.0:
            permuteRGB(pauseTime)
            pauseTime += 0.1
        print("max")
        
        while pauseTime >= 0.1:
            permuteRGB(pauseTime)
            pauseTime -= 0.1
        print("min")


if __name__ == "__main__": 
    main()