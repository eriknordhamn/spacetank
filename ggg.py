#!/usr/bin/python3
# coding=utf-8
# File name   : setup_virtual.py
# Author      : erik

import os
import time

#Set to user and home
username = "erik"
user_home = "/home/erik"

os.system("cd ~")

os.system("ls")

curpath = os.path.realpath(__file__)
thisPath = os.path.dirname(curpath)

print(thisPath)

