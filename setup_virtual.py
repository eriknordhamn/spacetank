#!/usr/bin/python3
# coding=utf-8
# File name   : setup_virtual.py
# Author      : Erik Nordhamn

import os
import time

#Set user and user home
username = "erik"
user_home = "/home/erik"

#Find path to the script
curpath = os.path.realpath(__file__)
thisPath = os.path.dirname(curpath)
print(thisPath)

def replace_num(file,initial,new_num):
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)


def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    return status, result

def check_rpi_model():
    _, result = run_command("cat /proc/device-tree/model |awk '{print $3}'")
    result = result.strip()
    if result == '3':
        return int(3)
    elif result == '4':
        return int(4)
    else:
        return None

def check_raspbain_version():
    _, result = run_command("cat /etc/debian_version|awk -F. '{print $1}'")
    return int(result.strip())

def check_python_version():
    import sys
    major = int(sys.version_info.major)
    minor = int(sys.version_info.minor)
    micro = int(sys.version_info.micro)
    return major, minor, micro

def check_os_bit():
    '''
    # import platform
    # machine_type = platform.machine() 
    latest bullseye uses a 64-bit kernel
    This method is no longer applicable, the latest raspbian will uses 64-bit kernel 
    (kernel 6.1.x) by default, "uname -m" shows "aarch64", 
    but the system is still 32-bit.
    '''
    _ , os_bit = run_command("getconf LONG_BIT")
    return int(os_bit)


commands_pip_1 = [
"pip3 install adafruit-circuitpython-motor",
"pip3 install adafruit-circuitpython-pca9685",
"pip3 install flask",
"pip3 install flask_cors",
"pip3 install numpy",
"pip3 install pyzmq",
"pip3 install imutils zmq pybase64 psutil",
"pip3 install websockets",
"pip3 install adafruit-circuitpython-ads7830"
]
commands_pip_2 = [
"pip3 install adafruit-circuitpython-motor",
"pip3 install adafruit-circuitpython-pca9685",
"pip3 install flask",
"pip3 install flask_cors",
"pip3 install numpy",
"pip3 install pyzmq",
"pip3 install imutils zmq pybase64 psutil",
"pip3 install websockets",
"pip3 install adafruit-circuitpython-ads7830"
]
mark_pip = 0
OS_version = check_raspbain_version()
if OS_version <= 11:
    for x in range(3):
        for command in commands_pip_1:
            if os.system(command) != 0:
                print("Error running installation step pip")
                mark_pip = 1
        if mark_pip == 0:
            break
else:
    for x in range(3):
        for command in commands_pip_2:
            if os.system(command) != 0:
                print("Error running installation step pip")
                mark_pip = 1
        if mark_pip == 0:
            break

commands_3 = [
    "cd ..;git clone https://github.com/oblique/create_ap",
    "cd ../create_ap && sudo make install",
    "sudo apt install -y util-linux procps hostapd iproute2 iw haveged dnsmasq"
]

mark_3 = 0
for x in range(3):
    for command in commands_3:
        if os.system(command) != 0:
            print("Error running installation step 3")
            mark_2 = 1
    if mark_3 == 0:
        break

#try:
#    replace_num("/boot/firmware/config.txt", '#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
#except:
#    print('Error updating boot config to enable i2c. Please try again.')

try:
    os.system("sudo touch " + user_home + "/startup.sh")
    os.system("sudo chmod 777 /" + user_home + "/startup.sh")
    with open("/" + user_home + "/startup.sh",'w') as file_to_write:
        #you can choose how to control the robot
        file_to_write.write("#!/usr/bin/bash\nsleep 5\nsource " + thisPath + "/env/bin/activate\npython3 " + thisPath + "/web/webServer.py")
except:
    pass

quit()


replace_num('/etc/rc.local','fi','fi\n/'+ user_home +'startup.sh start')

# try: #fix conflict with onboard Raspberry Pi audio
#     os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
#     with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
#         file_to_write.write("blacklist snd_bcm2835")
# except:
#     pass
# try:
#     os.system("sudo cp -f /"+ user_home +"/adeept_rasptank/server/config.txt //etc/config.txt")
# except:
#     os.system("sudo cp -f "+ thisPath  +"/adeept_rasptank/server/config.txt //etc/config.txt")
print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("sudo reboot")
