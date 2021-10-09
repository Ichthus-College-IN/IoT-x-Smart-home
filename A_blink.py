from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(1)  # aan
  sleep(0.5)
  led.value(0)  # uit
  sleep(0.5)
