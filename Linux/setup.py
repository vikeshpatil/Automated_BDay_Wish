import os
dir_path = os.path.dirname(os.path.realpath(__file__))

main_name = "/main.py"

from pathlib import Path
home = str(Path.home())

with open(dir_path + "/AutomatedBirthday.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n\npython '+ dir_path + main_name)

with open(dir_path + "/Add_Contact.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n\npython '+ dir_path + '/Data/save_data.py')

with open(dir_path + "/Registration.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n\npython '+ dir_path + '/save_credentials.py')

with open(home + '/.config/systemd/user/AutomatedBirthday.service', 'w') as f:
    f.write('[Unit]\nWants=network-online.target\nAfter=network-online.target\n\n[Service]\nExecStart=' + dir_path + '/AutomatedBirthday.sh\n\n[Install]\nWantedBy=default.target')

with open(home + '/.config/systemd/user/chromium.service', 'w') as f:
    f.write('[Unit]\nDescription="Starting chromium on startup"\nPartOf=graphical-session.target\n\n[Service]\nExecStart=/usr/lib64/chromium/chromium\n\n[Install]\nWantedBy=multi-user.target')

with open(dir_path + "/uninstall.sh", 'w') as f:
    f.write('#!/usr/bin/env bash\n\nrm ' + home + '/.config/systemd/user/AutomatedBirthday.service\nrm ' + home + '/.config/systemd/user/chromium.service')