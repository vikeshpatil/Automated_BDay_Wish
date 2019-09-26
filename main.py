from collections import namedtuple
import smtplib, ssl
import getpass


# Person = namedtuple('Person', 'fname, lname, email, mob, dob')
#
# #dict = {'Shreyansh' : Person(fname='Shreyansh', lname='Patil', email='patilshree8918', mob=7028332871, dob='18/09/2000')}

# -------------Using SMTP_SSL() method (secure from outset)----------------------------

# port = 465 #465 for SMTP_SSL()
# password = getpass.unix_getpass(prompt='Enter Password: ')     #input("Type your password and press enter: ")
#
# #Create a secure SSL context
# context = ssl._create_default_https_context()
#
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context) as server:
#     server.login("vikesh.patil", password)


#----------------Using .starttls() method (first creating unsecured connection and then encrypting it with .starttls())--------------

smtp_server = "smtp.gmail.com"
port = 587 # port for .starttls()

sender_email = "vikesh.patil8340@gmail.com"
receiver_email = "rajp8340@gmail.com"
password = getpass.unix_getpass("Enter Password: ")

context = ssl.create_default_context()

message = "Testing Automated B'Day wish"

#login to server and send email

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() #To identify yourself to the server, .helo() (SMTP) or .ehlo() (ESMTP) should be called
    server.starttls(context=context) #Secure the connection
    server.ehlo()
    server.login(sender_email, password)

    #Send email here
    if server.sendmail(sender_email, receiver_email, message):
        print("Mail sent!")

except Exception as e:
    #print errors
    print(e)
finally:
    server.quit()


