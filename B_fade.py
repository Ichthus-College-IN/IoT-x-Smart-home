from machine import Pin
from machine import PWM
from time import sleep_ms
from math import sin, pi

ledPin = Pin(4, Pin.OUT)      # ledpin object maken
led = PWM(ledPin, freq=1000)  # PWM toevoegen aan de pin

def pulse(pin, t):
  for i in range(20):
    pin.duty(int(sin(i / 10 * pi) * 500 + 500)) # pin PWM-belasting aanzetten
    sleep_ms(t)               # slapen in milliseconden
          
while True:
  pulse(led, 50)              # continu faden
