Copied from Adeept RaspTank2 and customzied.

Create keys if not available

ssh-keygen -t ed25519 -C "email"

Basic upgrade

sudo apt update
sudo apt upgrade


Make setup_modules.sh executable and run:

chmod u+x setup_modules.sh
./setup_modules.sh

Create a virtual environment "env" and use site packages as base and activate:

python3 -m venv --system-site-packages env
source env/bin/activate


Run setup:
python3 setup_virtual.py


Define a systemd service and set it up:
sudo cp my-spacetank.service /etc/systemd/system/.
sudo systemctl daemon-reload
sudo systemctl enable my-spacetank
sudo systemctl start my-spacetank


To check services and stop:
sudo systemctl status my*
sudo systemctl stop my-spacetank

Skip create_ap for now. It seems to break something in NetworkManager
Problems with create_ap
sudo apt install iptables

Run with sudo and user environment and PATH:
sudo -E env PATH="$PATH" python3 05_ws2812.py

This will use the virtual environment definded but run as root with privileges to all hardware. The PWM generator uses /dev/mem which is root access.





