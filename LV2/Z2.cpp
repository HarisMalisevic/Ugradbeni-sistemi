#include "mbed.h"
#include "lpc1114etf.h"

DigitalOut E(LED_ACT);

DigitalOut led1(LED0), led2(LED1), led3(LED2), led4(LED3), led5(LED4), led6(LED5), led7(LED6), led8(LED7);

DigitalOut LEDs[] = {led1, led2, led3, led4, led5, led6, led7, led8};

DigitalIn Btn(Taster_1);

bool countUp = true;

void increment() {
    int carry = 1;

    for (auto &pin : LEDs) {
        int current = pin;
        if (current == 1 && carry == 1) {
            pin = 0;
        } else {
            int tmp = carry + current;
            pin = tmp;
            carry = 0;
        }
    }
}

void decrement() {
    int index = 0;

    while (index < 8) {
        if (LEDs[index] == 1) {
            break;
        } else {
            index++;
        }
    }

    if (index != 8) {
        LEDs[index] = 0;
    }

    for (int i = 0; i < index; i++) {
        LEDs[i] = 1;
    }
}

void changeDirection() {
    countUp = !countUp;
}

int main() {
    E = 0;

        while (true) {
            if (countUp)
                increment();
            else
                decrement();

            wait_us(1000000);

            if (Btn == 1)
                changeDirection();
        }
    
}