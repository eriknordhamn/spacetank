#!/usr/bin/python3
# coding=utf-8
# File name   : setup_virtual.py
# Author      : erik

import os
import time

#Set to user and home
username = "erik"
user_home = "/home/erik"

quit()

curpath = os.path.realpath(__file__)
thisPath = os.path.dirname(curpath)

print(thisPath)

os.system("pip install numpy")

