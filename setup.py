import os
dir_path = os.path.dirname(os.path.realpath(__file__))
reg_name = "\AutomatedBirthday.bat"
main_name = "\main.py"

with open("run.bat", 'w') as f:

    f.write('reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Automated_Birthday /t REG_SZ /d '+ dir_path + reg_name)

with open("AutomatedBirthday.bat", 'w') as f:
    f.write('python '+ dir_path + main_name)