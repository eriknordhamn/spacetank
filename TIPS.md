Hotspot
Adeept_Robot, 12345678
192.168.12.1:5000

sudo killall python3
sudo create_ap wlan0 eth0 Adeept_Robot 12345678

nano
Y to save

import time
from gpiozero import LED

def switchSetup():
    global led1,led2,led3
    led1 = LED(9)
    led2 = LED(25)
    led3 = LED(11)

def switch(port, status):
    if port == 1:
        if status == 1:
            led1.on()
        elif status == 0:
            led1.off()