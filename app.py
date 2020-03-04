import RPi.GPIO as gpio
import time
import requests
import json

gpio.setmode(gpio.BCM)

gpio.setup(23, gpio.IN, pull_up_down = gpio.PUD_DOWN)

while True:
	if(gpio.input(23) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"23"})
                print('chamando api')
            except:
                print('caiu servidor')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"23"})
                print('chamando api')
            except:
                print('caiu servidor')
	time.sleep(1)

gpio.cleanup()
exit()