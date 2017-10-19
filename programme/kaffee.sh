#!/bin/sh

#KMaschine ein
sudo echo "out" > /sys/class/gpio/gpio22/direction
sudo echo "1" > /sys/class/gpio/gpio22/value
sudo sleep 2
sudo echo "0" > /sys/class/gpio/gpio22/value
sudo sleep 60
#Kaffee rauslassen
sudo echo "out" > /sys/class/gpio/gpio23/direction
sudo sleep 30 
sudo echo "in" > /sys/class/gpio/gpio23/direction
sudo sleep 5
#Maschine aus
sudo echo "out" > /sys/class/gpio/gpio22/direction
sudo echo "1" > /sys/class/gpio/gpio22/value
sleep 2
sudo echo "0" > /sys/class/gpio/gpio22/value 
sudo echo 'Timer muede, timer fertig...'

