### GPIO

```
from machine import Pin
led = Pin(2, Pin.OUT)         // D4 <--> GPIO 2

led.value(0 / 1)
led.on()
led.off()

```
