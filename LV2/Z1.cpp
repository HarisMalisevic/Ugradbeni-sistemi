#include "mbed.h"
#include "lpc1114etf.h"

DigitalOut E(LED_ACT);

DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);
DigitalOut led4(LED4);

DigitalOut leds[] = {led1, led2, led3, led4};

int main() {
    E = 0;
    while (1) {
        for (int i = 0; i < 4; i++) {
            leds[i] = 1;
            wait_us(1000000);
            leds[i] = 0;
            wait_us(1000000);
        }
    }
}