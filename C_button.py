from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)             # led object maken op pin 4
push_button = Pin(18, Pin.IN)     # knop object maken op pin 18

while True:
  if push_button.value():         # als op de knop gedrukt wordt..
      led.value(not led.value())  # ..switchen we de led van waarde
      while push_button.value():  # nietsdoen tot de knop niet meer ingedrukt wordt
        pass
      sleep(0.2)                  # tijd geven om stroom weg te laten lopen zodra de knop losgelaten wordt
