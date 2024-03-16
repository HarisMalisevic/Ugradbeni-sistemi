from machine import Pin
from time import sleep

LED0 = Pin(12, Pin.OUT)
LED1 = Pin(13, Pin.OUT)
LED2 = Pin(14, Pin.OUT)
LED3 = Pin(15, Pin.OUT)
LED4 = Pin(4, Pin.OUT)
LED5 = Pin(5, Pin.OUT)
LED6 = Pin(6, Pin.OUT)
LED7 = Pin(7, Pin.OUT)

outputLEDs = [LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7]


def setZeroes():
    for pin in outputLEDs:
        pin.value(0)


def setOnes():
    for pin in outputLEDs:
        pin.value(1)


def runningLight(pauseTime):

    index = -1

    while True:

        while index + 1 < len(outputLEDs):
            outputLEDs[index].off()
            outputLEDs[index + 1].on()
            index += 1
            sleep(pauseTime)

        while index > 0:
            outputLEDs[index - 1].on()
            outputLEDs[index].off()
            index -= 1
            sleep(pauseTime)


def main():
    setOnes()
    sleep(1)
    setZeroes()

    runningLight(0.2)

    print("Uredan kraj!")


if __name__ == "__main__":
    main()
