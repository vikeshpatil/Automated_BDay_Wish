# Automated Birthday Wisher
Python project to send automatic birthday wish to saved contact on his/her birthday. Program automatically checks for birthday at startup and sends birthday wishes to person's email, via sms, Facebook and Whatsapp personal and groups. 

# Installation
Clone or download repository.

### Install python
Refere [this](https://realpython.com/installing-python/) link for python installation.

#### Setup Sms Accout 
To setup account for sms, we are using Way2Sms service
   1) Visit [Way2Sms](https://www.way2sms.com/)
   2) Complete Registration and login with your details
   3) Click on API and Head towards Live keys section
   4) Copy API key and secrete key and paste them while setting up local account.

## Windows Setup

### Setup
Navigate to the project folder you cloned or downloaded and 

    Run Setup.bat
    
To run a .bat file just double click on file.

At the end a registration window will appear to save login details. Fill the correct details and click on save. (You can change the credentials by again running 'Registration.bat' file and enter valid details. It will overwrite existing details.)

#### Add Contact/Person Details
    1) Run Add Contact.bat
    2) Enter details of person and group names to send wishes to
    3) Choose the file format to save details. (you can change or delete contact by opening file in Data/credentials folder in installation directory)

This will complete the setup and program will automatically send birthay wish to contact on his/her birthday. Program will need internet connection while sending wish so make sure you are connected to internet.

#### Uninstall

    Run Uninstall.bat
<br><br>

## Linux Installation

### Setup
Navigate to the Navigate to the project folder you cloned or downloaded and Open the terminal there (location can be /home/user/programs/Automated_BDay_Wish/Linux/)

Type the following commands in terminal
    
    $ chmod +x setup.sh
    $ ./setup.sh

At the end a registration window will appear to save login details. Fill the correct details and click on save.

##### Changing login details
Navigate to project folder and open terminal there and enter following command
    
    $ ./Registration.sh

Now enter details to be changed and save.

#### Add Contact/Person Details
Navigate to program folder and open terminal there

    1) Type ./Add_Contact.sh and hit enter
    2) Enter details of person and group names to send wishes to
    3) Choose the file format to save details. (you can change or delete contact by opening file in Data/credentials folder in program directory)

#### Uninstall
    
    $ ./uninstall.sh
    

<br><br>
<b><i>** Unfortunately Whatsapp feature is not working in Linux</i></b>