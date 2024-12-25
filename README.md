Copied from Adeept RaspTank2 and customzied.

Make setup_modules.sh executable and run:

chmod u+x setup_modules.sh
./setup_modules.sh

Create a virtual environment "env" and activate:

python3 -m venv env
source env/bin/activate

Run setup:
python3 setup_virtual.py

Define a systemd service and set it up:
sudo cp my-spacetank.service /etc/systemd/system/.
sudo systemctl daemon-reload
sudo systemctl enable my-spacetank
sudo systemctl start my-spacetank
