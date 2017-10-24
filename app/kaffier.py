#/usr/bin/python2

from flask import Flask, render_template, request, url_for
import subprocess
from datetime import datetime
import time
from threading import Thread
import sqlite3
from flask import g

'----------------------> Helpers <-----------------------------'
def write_file(path, value):
    try:
        with open(path,'w') as file:
            file.write(value)
    except:
	print "Fehler"
	pass


DATABASE = '/home/pi/Data.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

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
	    print 'Timer muede, timer fertig...'
            break


'-----------------------> Initialisierung <--------------------'
write_file('/sys/class/gpio/export','23')
write_file('/sys/class/gpio/export','22')


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def do():
    on_off = request.args.get('on_off')
    go = request.args.get('go')
    alarm_time = request.args.get('time')

    if go is not None:
	write_file('/sys/class/gpio/gpio23/direction','out')
	time.sleep(5)
        write_file('/sys/class/gpio/gpio23/direction','in')
    	return 'Hmmmm chafe.. nom nom'

    if on_off is not None:
        write_file("/sys/class/gpio/gpio22/direction", "out")
        write_file("/sys/class/gpio/gpio22/value","1")
	time.sleep(5)
	write_file("/sys/class/gpio/gpio22/value","0")
       	return 'haeaseasea...'

    if alarm_time is not None:
        alarm_h = int(alarm_time[:2])
        alarm_m = int(alarm_time[3:])
        timer_thread = Thread(target=timer, args=(alarm_h, alarm_m,))
        timer_thread.start()
        return 'Timer gesetzt'
	return render_template('form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1337)






