#Automated Birthday Wisher
Python project to send automatic birthday wish to saved contact on his/her birthday. Program automatically checks for birthay at startup and sends birthday wishes to person's email, via sms, Facebook and whatsapp personal and groups. 
#Installation
Clone or download repository.
###Install python

Refere [this](https://wiki.python.org/moin/BeginnersGuide/Download) link for python installation.

##Windows Setup
###Setup
    1) Run Setup.bat
    2) Run run.bat
To run a .bat file just double click on file.
####Accounts Setup
    1) Run Registration.bat
    2) Enter the account details for Facebook, Gmail and SMS
To setup account for sms, we are using Way2Sms service
   1) Visit [Way2Sms](https://www.way2sms.com/)
   2) Complete Registration and login with your details
   3) Click on API and Head towards Live keys section
   4) Copy API key and secrete key and paste them while setting up account.

Make sure to enter valid credentials. (You can change the credentials by again running Registration.bat file and enter valid details. It will overwrite existing details.)

####Contact Details
    1) Run Add Contact.bat
    2) Enter details of person and group names to send wishes to
    3) Choose the file format to save details. (you can change or delete contact by opening file in credentials folder installation directory)

This will complete the setup and program will automatically send birthay wish to contact on his/her birthday. Program will need internet connection while sending wish so make sure you are connected to internet.