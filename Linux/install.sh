#!/usr/bin/env bash

python setup.py
pip install requests
pip install selenium
pip install fbchat
pip install pyAesCrypt
pip install openpyxl

chmod 744 AutomatedBirthday.sh
chmod 744 Add_Contact.sh
chmod 744 Registration.sh
chmod 744 uninstall.sh
chmod +x chromedriver

chmod 664 ~/.config/systemd/user/AutomatedBirthday.service
chmod 664 ~/.config/systemd/user/chromium.service

systemctl daemon-reload
systemctl --user enable AutomatedBirthday.service

python save_credentials.py