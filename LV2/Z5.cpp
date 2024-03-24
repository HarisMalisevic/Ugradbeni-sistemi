#include "mbed.h"
#include "lpc1114etf.h"
DigitalOut E(LED_ACT);

DigitalOut led1(LED1);

int main()
{
    E = 0;

    int T = 50000; // pocetna proizvoljna vrijednost
    int uk = T, ug = T;
    while (1)
    {
        for (int i = 0; i < 30; i++)
        {
            led1 = 1;
            wait_us(uk);
            led1 = 0;
            wait_us(ug);
            uk += 0.063 * T;
            ug -= 0.063 * T;
        }
        for (int i = 0; i < 60; i++)
        {
            led1 = 1;
            wait_us(uk);
            led1 = 0;
            wait_us(ug);
            uk -= 0.063 * T;
            ug += 0.063 * T;
        }
    }
}
