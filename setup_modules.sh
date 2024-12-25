#!/usr/bin/sh
echo "Setting up additional packages"
sudo apt update
sudo apt install python3-gpiozero python3-pigpio
sudo apt install -y python3-opencv
sudo apt install -y python3-pyqt5 python3-opengl
sudo apt install -y python3-picamera2
sudo apt install -y python3-picamera2 --no-install-recommends
sudo apt install -y python3-opencv
sudo apt install -y opencv-data
sudo apt install -y python3-pyaudio

