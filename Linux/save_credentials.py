#! python3
# For reference visit   https://www.simplifiedpython.net/python-gui-login/


from tkinter import *
import base64
from Data import encrypt

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(dir_path + '/Data/credentials/'):
    os.mkdir(dir_path + '/Data/credentials')

buffersize = 64 *1024   #encryption or decryption buffer size

def main_account_screen():
    global main_screen

    main_screen = Tk()  # create a GUI window
    main_screen.geometry("500x350")  # set the configuration of GUI window
    main_screen.title("Save Details")  # set the title of GUI window


    Label(text="Choose option to save details", bg="white", fg="black", width="300", height="2", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Facebook Login Details", height="2", width="30", command=FB_login).pack()
    Label(text="").pack()

    Button(text="Gmail Login Details", height="2", width="30", command=Gmail_login).pack()
    Label(text="").pack()

    Button(text="Sms Keys Setup", height="2", width="30", command=Sms_details).pack()

    main_screen.mainloop()  # start the GUI


def FB_login():

    global fbusername
    global fbpassword
    global fbconfirm_pass
    global fbusername_entry
    global fbconfirm_password_entry
    global fbpassword_entry
    global FB_login_screen

    FB_login_screen = Toplevel(main_screen)
    FB_login_screen .title("Register")
    FB_login_screen .geometry("500x350")

    # Set text variables
    fbusername = StringVar()
    fbpassword = StringVar()
    fbconfirm_pass = StringVar()

    # Set label for user's instruction
    Label(FB_login_screen, text="Please enter your Facebook datails", bg="white", fg="black", width="300", height="2", font=("Calibri", 15)).pack()
    Label(FB_login_screen, text="").pack()

    # Set username label
    username_lable = Label(FB_login_screen , height="2", width="30",text="Username * ")
    username_lable.pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    fbusername_entry = Entry(FB_login_screen, width=30, textvariable=fbusername)
    fbusername_entry.pack(ipady=2)

    # Set password label
    password_lable = Label(FB_login_screen , height="2", width="30", text="Password * ")
    password_lable.pack()

    # Set password entry
    fbpassword_entry = Entry(FB_login_screen, width=30, textvariable=fbpassword, show='*')
    fbpassword_entry.pack(ipady=2)

    # Set password label
    confirm_password_lable = Label(FB_login_screen, height="2", width="30", text="Confirm Password * ")
    confirm_password_lable.pack()

    # Set password entry
    fbconfirm_password_entry = Entry(FB_login_screen, width=30, textvariable=fbconfirm_pass, show='*')
    fbconfirm_password_entry.pack(ipady=2)

    Label(FB_login_screen, text="").pack()

    # Set register button
    Button(FB_login_screen, text="Save", width=20, height=2, bg="green", command=FB_save).pack()



def FB_save():
    # get username and password
    username_info = fbusername.get()
    password_info = fbpassword.get()
    confirm_pass_info = fbconfirm_pass.get()

    successfull = False
    if password_info == confirm_pass_info:
        username_n_pass = username_info + " " + password_info
        username_n_pass_en = base64.b64encode(username_n_pass.encode('utf-8'))

        # Open file in write mode
        file = open(dir_path + '/Data/credentials/fbe', "w")

        # write username and password information into file
        file.write(username_n_pass_en.decode('utf-8'))
        file.close()

        encrypt.encrypt(dir_path + '/Data/credentials/fbe')      #encryot the file

        fbusername_entry.delete(0, END)
        fbpassword_entry.delete(0, END)
        fbconfirm_password_entry.delete(0, END)

        # set a label for showing success information on screen

        successfull = True
    if successfull:
        Label(FB_login_screen, text="Details Saved Successfully. You can close Window", fg="green", font=("calibri", 13)).pack()
        FB_login_screen.destroy()
    else:
        Label(FB_login_screen, text="Password Do Not Match", fg="red", font=("calibri", 13)).pack()


#     -----------Gmail Details----------------
def Gmail_login():

    global Gmailusername
    global Gmailpassword
    global Gmailconfirm_pass
    global Gmailusername_entry
    global Gmailconfirm_password_entry
    global Gmailpassword_entry
    global Gmail_login_screen

    Gmail_login_screen = Toplevel(main_screen)
    Gmail_login_screen .title("Register")
    Gmail_login_screen .geometry("500x350")

    Gmailusername = StringVar()
    Gmailpassword = StringVar()
    Gmailconfirm_pass = StringVar()

    Label(Gmail_login_screen, text="Please enter your Gmail details", bg="white", fg="black", width="300", height="2", font=("Calibri", 15)).pack()
    Label(Gmail_login_screen, text="").pack()

    username_lable = Label(Gmail_login_screen , height="2", width="30",text="Email * ")
    username_lable.pack()

    Gmailusername_entry = Entry(Gmail_login_screen, width=30, textvariable=Gmailusername)
    Gmailusername_entry.pack(ipady=2)

    password_lable = Label(Gmail_login_screen , height="2", width="30", text="Password * ")
    password_lable.pack()

    Gmailpassword_entry = Entry(Gmail_login_screen , width=30,textvariable=Gmailpassword, show='*')
    Gmailpassword_entry.pack(ipady=2)

    confirm_password_lable = Label(Gmail_login_screen, height="2", width="30", text="Confirm Password * ")
    confirm_password_lable.pack()

    Gmailconfirm_password_entry = Entry(Gmail_login_screen,width=30, textvariable=Gmailconfirm_pass, show='*')
    Gmailconfirm_password_entry.pack(ipady=2)

    Label(Gmail_login_screen, text="").pack()

    Button(Gmail_login_screen , text="Save", width=20, height=2, bg="green", command=Gmail_save).pack()

def Gmail_save():

    username_info = Gmailusername.get()
    password_info = Gmailpassword.get()
    confirm_pass_info = Gmailconfirm_pass.get()

    successfull = False
    if password_info == confirm_pass_info:

        username_n_pass = username_info + " " + password_info
        username_n_pass_en = base64.b64encode(username_n_pass.encode('utf-8'))

        file = open(dir_path + '/Data/credentials/gme', "w")

        file.write(username_n_pass_en.decode('utf-8'))
        file.close()

        encrypt.encrypt(dir_path + '/Data/credentials/gme')

        Gmailusername_entry.delete(0, END)
        Gmailpassword_entry.delete(0, END)
        Gmailconfirm_password_entry.delete(0, END)

        successfull = True
    if successfull:
        Label(Gmail_login_screen, text="Details Saved Successfully. You can close window.", fg="green", font=("calibri", 13)).pack()

        Gmail_login_screen.destroy()
    else:
        Label(Gmail_login_screen, text="Password Do Not Match", fg="red", font=("calibri", 13)).pack()


def Sms_details():

    global Sms_details_screen
    global SmsApi
    global SmsApi_entry


    Sms_details_screen = Toplevel(main_screen)
    Sms_details_screen .title("Register")
    Sms_details_screen .geometry("600x350")

    SmsApi = StringVar()

    Label(Sms_details_screen, text="Please enter API Key From Your fast2sms Profile", fg="black", bg="white", width="300", height="2", font=("Calibri", 15)).pack()
    Label(Sms_details_screen, text="").pack()

    SmsApi_lable = Label(Sms_details_screen, height="2", width="30",text="API Key * ")
    SmsApi_lable.pack()

    SmsApi_entry= Entry(Sms_details_screen, width=40, textvariable=SmsApi, show='*')
    SmsApi_entry.pack(ipady=2)

    Label(Sms_details_screen, text="").pack()

    Button(Sms_details_screen, text="Save", width=20, height=2, bg="green", command=Sms_save).pack()

def Sms_save():

    SmsApiKey = SmsApi.get()

    SmsApiKey_en = base64.b64encode(SmsApiKey.encode('utf-8'))

    file = open(dir_path + '/Data/credentials/se', "w")

    file.write(SmsApiKey_en.decode('utf-8'))
    file.close()

    encrypt.encrypt(dir_path + '/Data/credentials/se')

    SmsApi_entry.delete(0, END)


    Label(Sms_details_screen, text="Details Saved. You can close window", fg="green", font=("calibri", 13)).pack()
    Sms_details_screen.destroy()


main_account_screen()  # call the main_account_screen() function