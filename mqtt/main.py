# MQTT library van https://github.com/bborncr/ESP32MQTT-Micropython
# aangepast door Bns

#%% publish/subscribe thread
import esp32
import time
import _thread

start_time = time.ticks_ms()
interval = 10000 # 10 second interval for publishing data

# Returns True if interval has passed
def ready_to_publish():
    global start_time
    if time.ticks_ms() - start_time > interval:
        start_time = time.ticks_ms()
        return True
    else:
        return False

def publish():
    count = 1
    while True:
        checkwifi()                                                         # check if WiFi is still connected
        client.check_msg()                                                  # check for incoming messages (non-blocking)
        if ready_to_publish():                                              # if the interval time has passed, publish again
            client.ping()                                                   # ping the MQTT broker to refresh the keepalive
            temperature=esp32.raw_temperature()                             # get internal temperature of chip
            msg = '{"Count":%u,"Temperature":%2.2f}' % (count,temperature)  # create a message in JSON format
            client.publish('ESP32' + '/data/json', msg)
            count = count + 1

_thread.start_new_thread(publish, ())

#%% main thread
from machine import Pin, PWM
from math import sin, pi

def LEDs_init(pin_list):
	LEDs = []
	for pin in pin_list:
		LEDs += [Pin(pin, Pin.OUT)]
	return LEDs

def LEDs_PWM_init(LEDs_list, f=1000):
	LEDs_PWM = []
	for LED in LEDs_list:
		LEDs_PWM += [PWM(LED, freq = f)]
	return LEDs_PWM

def pulse(LEDs_list, t=25):
	for i in range(40):
		offset = 0
		for j in LEDs_list:
			j.duty(int(sin(i / 20 * pi + offset * pi) * 500 + 500)) # set PWM duty cycle to some value depending on the LED
			offset += 0.5
		time.sleep_ms(t)               								# sleep for 't' milliseconds

def no_pulse(LEDs_list):
	for j in LEDs_list:
		j.duty(0) 													# set PWM duty cycle for all LEDs to 0

pins = [2, 25, 26, 27]
LEDs = LEDs_init(pins)
LEDs_PWM = LEDs_PWM_init(LEDs)

while True:
	if enable:
		pulse(LEDs_PWM)
	else:
		no_pulse(LEDs_PWM)
		time.sleep_ms(10)