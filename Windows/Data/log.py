import datetime
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

today = datetime.date.today()

def log_write():

    with open(dir_path + '/log.txt', 'w') as f:
        f.write(today.isoformat())

def log_read():
    with open(dir_path + '/log.txt', 'r') as f:
        content = f.read()
        if((str(content) == str(today.isoformat()))):
            return True
        else:
            return False