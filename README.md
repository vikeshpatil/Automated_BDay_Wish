# Automated Birthday Wisher
Python project to send automatic birthday wish to saved contact on his/her birthday. Program automatically checks for birthday at startup and sends birthday wishes to person's email, via sms, Facebook and Whatsapp personal and groups. 

# Installation
Clone or download repository.

### Requirements
1) Python 3.x must be installed. Refere [this](https://realpython.com/installing-python/) link for python installation.
 Download Python 3.x from (https://www.python.org/downloads/) Select appropriate operating system. 
 <b>Make sure to check <i>add to PATH</i> while installing python</b>
2) Chrome Browser should be installed in system. (Download Chrome from [here](https://www.google.com/chrome/))
3) Way2Sms service account to send sms.
4) Your Gmail account should allow less secure apps which important to send mail. If your account has two factor authentication then it must be disabled for program to be work.([Click here](https://devanswers.co/allow-less-secure-apps-access-gmail-account/) for guidance)

<i>At first 3-4 times facebook will decline login due to newly used IP but after that it will allow user to send messages. So stay tuned.
</i>

#### Setup Sms Accout 
To setup account for sms, we are using Way2Sms service
   1) Visit [Way2Sms](https://www.way2sms.com/)
   2) Complete Registration and login with your details
   3) Click on <b>API</b> at the top right.
   4) Then click on <b>Live keys</b> and select Get/Generate Api and Secrete key
   4) Copy API key and secrete key and paste them while setting up local account. (Given below)

## Windows Setup

### Setup
Navigate to the project folder you cloned or downloaded and 

    Run Install.bat
    
To run a .bat file just double click on file.

At the end, a registration window will appear to save login details. Fill the correct details and click on save. (You can change the credentials by again running <i>'Registration.bat'</i> file and enter valid details. It will overwrite existing details.)

#### Add Contact/Person Details
    1) Run Add Contact.bat
    2) Enter details of person and group names to send wishes to
    3) Choose the file format to save details. (you can change or delete contact by opening file in Data/credentials folder in installation directory)


This will complete the setup and program will automatically send birthday wish to contact on his/her birthday. After restarting system program will check for birthday and program will need internet connection while sending wish so make sure you are connected to internet.


#### Uninstall

    Run Uninstall.bat
<br><br>

## Linux Installation

### Setup
Navigate to the Navigate to the project folder you cloned or downloaded and Open the terminal there (location can be /home/user/programs/Automated_BDay_Wish/Linux/)

Type the following commands in terminal
    
    $ chmod +x install.sh
    $ ./install.sh

At the end a registration window will appear to save login details. Fill the correct details and click on save.

#### Changing login details
Navigate to project folder and open terminal there and enter following command
    
    $ ./Registration.sh

Now enter details to be changed and save.

#### Add Contact/Person Details
Navigate to program folder and open terminal there

    1) Type ./Add_Contact.sh and hit enter
    2) Enter details of person and group names to send wishes to
    3) Choose the file format to save details. (you can change or delete contact by opening file in Data/credentials folder in program directory)

This will complete the setup and program will automatically send birthday wish to contact on his/her birthday. After restarting system program will check for birthday and program will need internet connection while sending wish so make sure you are connected to internet.

#### Uninstall
    
    $ ./uninstall.sh
    

<br><br>
<b><i>** Unfortunately Whatsapp feature is not working in Linux</i></b>
