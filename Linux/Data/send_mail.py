
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
from Data.encrypt import *
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#----------------Using .starttls() method (first creating unsecured connection and then encrypting it with .starttls())--------------

def mail(receiver_mail, fname):

    decrypt(dir_path + '/credentials/gme')
    with open(dir_path + '/credentials/gme', mode='rb') as f:
        content = f.read()
        content = base64.b64decode(content).decode('utf-8')

    sender_email = str(content.split()[0])
    password = str(content.split()[1])

    port = 587  # port for .starttls()
    smtp_server = "smtp.gmail.com"  # server to send mail with

    receiver_email = receiver_mail

    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Happy Birthday"
    message["From"] = sender_email
    message["To"] = receiver_mail

    html = """\
    <html>
    <head>
    <link href="https://fonts.googleapis.com/css?family=Yeon+Sung&display=swap" rel="stylesheet">
        <style>
            h4{
            font-size:22px;
            font-family: 'Yeon Sung', cursive;
            }
        </style>
    </head>
        <body>
        <center>
        <h4 >Birthdays are a new start; <br> fresh beginnings, a time to start new endeavours with new goals.<br> Move forward with fresh 
    confidence and courage.<br> You are a special person,<br>
    may you have an amazing today and year. <br> Happy birthday <strong><big>""" + fname + """</big></strong>
            <br><br><img src="https://res.cloudinary.com/vikesh/image/upload/v1573208937/birthdaypic.jpg" width="100%" height="auto">
        </center>
        </body>    
    </html>
    """

    message.attach(MIMEText(html, 'html'))

    # ---------------Sending image-------------
    # img_open = open(dir_path + 'birthdaypic.jpg', 'rb')
    # img = MIMEImage(img_open.read())
    # img_open.close()
    # message.attach(img)

# #------------------------Attaching Video------------------
#     part = MIMEBase('application', "octet-stream")
#     fo = open(dir_path + 'birthday_vid.mp4', "rb")
#     part.set_payload(fo.read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename("birthday_vid.mp4"))
#     message.attach(part)

    #login to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # To identify yourself to the server, .helo() (SMTP) or .ehlo() (ESMTP) should be called
        server.starttls(context=context)  # Secure the connection
        server.ehlo()
        server.login(sender_email, password)

        # Send email here
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        # print errors
        print(e)
    finally:
        server.quit()

    encrypt(dir_path + '/credentials/gme')
