import os
dir_path = os.path.dirname(os.path.realpath(__file__))
reg_name = "\AutomatedBirthday.bat"
main_name = "\main.py"

with open(dir_path + "\\run.bat", 'w') as f:

    f.write('reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Automated_Birthday /t REG_SZ /d '+ dir_path + reg_name)

with open(dir_path + "\AutomatedBirthday.bat", 'w') as f:
    f.write('python '+ dir_path + main_name)

with open(dir_path + '\Registration.bat', 'w') as f:
    f.write('python ' + dir_path + '\save_credentials.py')

with open(dir_path + '\Add Contact.bat', 'w') as f:
    f.write('python ' + dir_path + '\Data\save_data.py')