def write_file(path, value):
    try:
        with open(path,'w') as file:
            file.write(value)
    except:
	print("Fehler")
	pass

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

def initialize():
    write_file('/sys/class/gpio/export','23')
    write_file('/sys/class/gpio/export','22')
