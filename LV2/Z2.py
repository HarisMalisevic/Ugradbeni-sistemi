from machine import Pin
from time import sleep

T1 = Pin(0, Pin.IN)  # Increment
T2 = Pin(1, Pin.IN)  # Decrement
T3 = Pin(2, Pin.IN)  # Set sum to 0x00
T4 = Pin(3, Pin.IN)  # Set sum to 0xFF

# Binary digits, 8-bit number with digits: 76543210
LED0 = Pin(12, Pin.OUT)
LED1 = Pin(13, Pin.OUT)
LED2 = Pin(14, Pin.OUT)
LED3 = Pin(15, Pin.OUT)
LED4 = Pin(4, Pin.OUT)
LED5 = Pin(5, Pin.OUT)
LED6 = Pin(6, Pin.OUT)
LED7 = Pin(7, Pin.OUT)

outputLEDs = [LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7]

button1 = Pin(0, Pin.IN)


def setZeroes():
    for pin in outputLEDs:
        pin.value(0)


def setOnes():
    for pin in outputLEDs:
        pin.value(1)


def increment():
    carry = 1

    for pin in outputLEDs:
        current = pin.value()

        if current == 1 and carry == 1:
            pin.value(0)
        else:
            new = current + carry
            pin.value(new)
            carry = 0


def decrement():
    index = 0
    
    while index < len(outputLEDs):
        if outputLEDs[index].value() == 1:
            break
        else:
            index = index + 1

    if index != len(outputLEDs):
        outputLEDs[index].value(0)

    for i in range(index):
        outputLEDs[i].value(1)
        

def main():
    setOnes()
    sleep(1)
    setZeroes()

    while True:

        sleep(0.3)
        while True:
            sleep(0.3)
            increment()

            if button1.value():

                break
        
        sleep(0.3)
        while True:
            decrement()
            sleep(0.3)

            if button1.value():
                break

        
            

if __name__ == "__main__":
    main()