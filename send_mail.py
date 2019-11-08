import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import getpass

#----------------Using .starttls() method (first creating unsecured connection and then encrypting it with .starttls())--------------

def mail(receiver_mail, fname):
    port = 587  # port for .starttls()
    smtp_server = "smtp.gmail.com"  # server to send mail with

    sender_email = "vikesh.patil8340@gmail.com"
    receiver_email = receiver_mail
    password = "Play!123"

    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Happy Birthday"
    message["From"] = sender_email
    message["To"] = receiver_mail

    html = """\
    <html>
        <body>
        <center>
        <h4>Birthdays are a new start; <br> fresh beginnings, a time to start new endeavours with new goals.<br> Move forward with fresh 
    confidence and courage.<br> You are a special person,<br>
    may you have an amazing today and year. <br> Happy birthday """ + fname + """
            <br><br><img src="https://images.unsplash.com/photo-1558636508-e0db3814bd1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80">
        </center>
        </body>    
    </html>
    """

    message.attach(MIMEText(html, 'html'))

    # login to server and send email
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
