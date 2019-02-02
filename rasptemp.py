import os
import time


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return float(temp[5:-3])


while True:
    if measure_temp() >= 85:
        os.popen("shutdown now")
    time.sleep(10)
