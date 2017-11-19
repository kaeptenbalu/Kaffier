import time
from flask import current_app

PINS = ["22", "23"]

def write_file(path, value):
    try:
        with open(path,'w') as file:
            file.write(value)
        return True
    except:
        current_app.logger.error("Could not write in file: %s", path)
        return False

def set_direction(pin, direction):
    if pin not in PINS:
        return False
    path = "/sys/class/gpio/gpio{}/direction".format(pin)
    if write_file(path, direction):
        return True

def set_value(pin, value):
    if pin not in PINS:
        return False
    path = "/sys/class/gpio/gpio{}/value".format(pin)
    if write_file(path, value):
        return True

def timer(h,m):
    while True:
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]

        if hour == h and minute == m:
	    #Maschine starten
            write_file("/sys/class/gpio/gpio22/direction", "out")
            write_file("/sys/class/gpio/gpio22/value","1")
            time.sleep(2)
            write_file("/sys/class/gpio/gpio22/value","0")
            time.sleep(60)
	    #Kaffee rauslassen
            write_file('/sys/class/gpio/gpio23/direction','out')
            time.sleep(30)
            write_file('/sys/class/gpio/gpio23/direction','in')
            time.sleep(5)
	    #Maschine aus
            write_file("/sys/class/gpio/gpio22/direction", "out")
            write_file("/sys/class/gpio/gpio22/value","1")
            time.sleep(2)
            write_file("/sys/class/gpio/gpio22/value","0")
            print('Timer muede, timer fertig...')
            break

def initialize():
    errors = 0
    for pin in PINS:
        if not write_file('/sys/class/gpio/export', pin):
            errors += 1
    if errors > 0:
        return False
    return True

def on_off():
    if not set_direction("22", "out"):
        return False
    if not set_value("22", "1"):
        return False
    time.sleep(5)
    if not set_value("22", "0"):
        return False
    return True
