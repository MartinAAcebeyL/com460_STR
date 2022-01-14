import time
import logging
from random import uniform

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def reloj():
    day = 0
    hour = 0
    min = 0
    sec = 0

    while True:
        time.sleep(1)
        if sec == 59:
            sec = -1
            min = min + 1
        sec = sec + 1
        if min == 60:
            min = 0
            hour = hour + 1
        if hour == 24:
            hour = 0
            day = day + 1
        return f'{day}:{hour}:{min}:{sec}'

def temperatura():
    return round(uniform(1, 50),2)
