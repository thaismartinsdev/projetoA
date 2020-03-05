import RPi.GPIO as gpio
import time
import requests
import json

gpio.setmode(gpio.BCM)

gpio.setup(4, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(27, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(22, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(24, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(5, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(6, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_DOWN)



while True:
	if(gpio.input(4) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"1"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"1"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)


	if(gpio.input(17) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"2"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"2"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)


	if(gpio.input(27) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"3"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"3"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)

	if(gpio.input(22) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"4"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"4"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)


	if(gpio.input(24) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"5"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"5"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)


	if(gpio.input(5) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"6"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"6"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)


	if(gpio.input(6) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"7"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"7"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)


	if(gpio.input(12) == 1):
            try:
                requests.post('http://localhost:3000/change', json={"status":"true", "key":"8"})
                print('Chamando API')
            except:
                print('ERROR')
	else:
            try:
                requests.post('http://localhost:3000/change', json={"status":"false", "key":"8"})
                print('Chamando API')
            except:
                print('ERROR')
	time.sleep(1)

gpio.cleanup()
exit()
