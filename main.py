import datetime
import codecs
import send_sms
import send_mail
import whatsapp_msg
import fb_msg
#------------- Reading data in text file----------------------#

today = datetime.date.today()



with open('contacts.txt', mode='r') as f:
    readContent = f.readlines()
for j in range(len(readContent)):
    if(readContent[j].split()[4] == str(today)):
        Person = readContent[j].split()
        fname = Person[0]
        lname = Person[1]
        name = Person[0] + " " + Person[1]
        mobile = Person[2]
        email = Person[3]
        whatapp_contact_list = []  # contacts to send message
        for i in range(5, len(Person)):
            whatapp_name = Person[i].split('_')

            whatapp_name = '"' + ' '.join(whatapp_name) + '"'

            whatapp_contact_list.append(whatapp_name)

        print("Happy B'day " + name + " . Your mobile numbe is " + mobile + ". And your email is " + email )
        # send_sms.sendPostRequest(str(mobile), fname)     #send sms
        # send_mail.mail("rajp8340@gmail.com", fname)       #send mail
        # whatsapp_msg.send_msg(whatapp_contact_list, fname)     #whatsapp message
        # fb_msg.send_msg(fname, lname, whatapp_contact_list)
    else:
        print("Unable to access DOB")

