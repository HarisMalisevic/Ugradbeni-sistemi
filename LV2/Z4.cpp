#include "mbed.h"
#include "lpc1114etf.h"

DigitalOut E(LED_ACT);

DigitalOut led1(LED0), led2(LED1), led3(LED2), led4(LED3), led5(LED4),
    led6(LED5), led7(LED6), led8(LED7);

DigitalOut LEDs[] = {led1, led2, led3, led4, led5, led6, led7, led8};

int NUM_LEDS = 8;

DigitalIn btn1(Taster_1);
DigitalIn btn2(Taster_2);

DigitalOut SignalLED(LED0);

void runningLight(int pauseTime_ms) {
  int index = -1;

  while (index + 1 < NUM_LEDS) {
    LEDs[index] = 0;
    LEDs[index + 1] = 1;
    index++;
    wait_us(pauseTime_ms);
  }

  index = NUM_LEDS - 1;

  // Svi LED-ovi su uključeni
  for (int i = 0; i < NUM_LEDS; i++) {
    LEDs[i] = 1;
  }

  wait_us(pauseTime_ms);

  while (index >= 0) {
    LEDs[index] = 0;
    index--;
    wait_us(pauseTime_ms);
  }
}
int main() {

  E = 0;

  while (true) {
    while (btn1 && btn2) {
      wait_us(100000);
    }

    if (btn1) {
      runningLight(100000);
    } else if (btn2) {
      runningLight(500000);
    } else {
      SignalLED = !SignalLED;
      wait_us(500000);
    }
  }
}