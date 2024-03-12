from machine import Pin
from time import sleep

print("Hello, Pi Pico!")
sleep(0.1) # Wait for USB to become ready

T1 = Pin(0, Pin.IN)  # Increment
T2 = Pin(1, Pin.IN)  # Decrement
T3 = Pin(2, Pin.IN)  # Set sum to 0x00
T4 = Pin(3, Pin.IN)  # Set sum to 0xFF

# Binary digits, 8-bit number with digits: 76543210
LED0 = Pin(4, Pin.OUT)
LED1 = Pin(5, Pin.OUT)
LED2 = Pin(6, Pin.OUT)
LED3 = Pin(7, Pin.OUT)
LED4 = Pin(8, Pin.OUT)
LED5 = Pin(9, Pin.OUT)
LED6 = Pin(10, Pin.OUT)
LED7 = Pin(11, Pin.OUT)

outputLEDs = [LED0, LED1, LED2, LED3, LED4, LED5, LED6, LED7]


def setZeroes(outputLEDs):
    for pin in outputLEDs:
        pin.value(0)


def setOnes(outputLEDs):
    for pin in outputLEDs:
        pin.value(1)


def increment(outputLEDs):
    carry = 1

    for pin in outputLEDs:
        current = pin.value()

        if current == 1 and carry == 1:
            pin.value(0)
        else:
            new = current + carry
            pin.value(new)
            carry = 0


def decrement(outputLEDs):
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
    setOnes(outputLEDs)
    sleep(1)

    while True:   
        
        if(T1.value()):
            increment(outputLEDs)
            while T1.value():
                sleep(0.1)
        elif(T2.value()):
            decrement(outputLEDs)
            while T2.value():
                sleep(0.1)
        elif(T3.value()):
            setZeroes(outputLEDs)
            while T3.value():
                sleep(0.1)
        elif(T4.value()):
            setOnes(outputLEDs)
            while T4.value():
                sleep(0.1)
            
        sleep(0.25)

            

if __name__ == "__main__":
    main()