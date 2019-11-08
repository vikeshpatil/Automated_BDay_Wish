import datetime

import send_sms
import send_mail
#------------- Reading data in text file----------------------#

today = datetime.date.today()

with open('contacts.txt', mode='r') as f:
    readContent = f.readlines()
for j in range(len(readContent)):
    if(readContent[j].split()[4] == str(today)):
        Person = readContent[j].split()
        fname = Person[0]
        name = Person[0] + " " +Person[1]
        mobile = Person[2]
        email = Person[3]
        message = """
        Subject: Happy Birthday
        
        This message is from python project."""

        print("Happy B'day " + name + " . Your mobile numbe is " + mobile + ". And your email is " + email )
        # send_sms.sendPostRequest('7507901921', fname)
        send_mail.mail("rajp8340@gmail.com", fname)

    else:
        print("Unable to access DOB")
