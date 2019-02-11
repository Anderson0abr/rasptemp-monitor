from pushover import apikey, userkey
from time import sleep
import os
import requests


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return float(temp[5:-3])


def notify(title, message):
    url = 'https://api.pushover.net/1/messages.json'
    data = {
            'token': apikey,
            'user': userkey,
            'title': title,
            'message': message
            }
    requests.post(url, data)


while True:
    if measure_temp() >= 85:
        try:
            notify("Raspberry Pi", "Temperature limit exceeded. Shutting down...")
        except:
            pass
        os.popen("shutdown now")
    sleep(10)
