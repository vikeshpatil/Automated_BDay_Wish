#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from fbchat import Client
from fbchat.models import *

from Data import encrypt
import base64

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def send_msg(FirstName, Last_Name, GroupNames):

    encrypt.decrypt(dir_path + '/credentials/fbe')
    with open(dir_path + '/credentials/fbe', mode='rb') as f:
        content = f.read()
        content = base64.b64decode(content).decode('utf-8')

    username = str(content.split()[0])
    password = str(content.split()[1])

    client = Client(username, password)

    if client.isLoggedIn():

        # ---------------Person------------------
        name = FirstName + " " + Last_Name
        friends = client.searchForUsers(name)  # return a list of names
        friend = friends[0]
        msg = "Birthdays are a new start; fresh beginnings, a time to start new endeavours with new goals. Move forward with fresh confidence and courage. You are a special person, may you have an amazing today and year. Happy birthday " + FirstName

        # Will send the image located at `<image path>`
        client.sendRemoteImage(
            "https://images.unsplash.com/photo-1558636508-e0db3814bd1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
            thread_id=friend.uid,
            thread_type=ThreadType.USER,
        )
        client.send(Message(text=msg), thread_id=str(friend.uid), thread_type=ThreadType.USER)

        # -------------------------Group----------------------
        for GroupName in GroupNames:
            try:
                gname = GroupName
                groups = client.searchForGroups(gname)

                group = groups[0]
                client.sendRemoteImage(
                    "https://images.unsplash.com/photo-1558636508-e0db3814bd1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
                    thread_id=group.uid,
                    thread_type=ThreadType.GROUP,
                )
                client.send(Message(text=msg), thread_id=group.uid, thread_type=ThreadType.GROUP)
            except:
                continue

        client.logout()

    else:
        print('not logged in')



    #------------------------Automation using browser--------------------

    chrome_options = webdriver.ChromeOptions()

    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(dir_path + "/chromedriver")

    # open facebook.com using get() method
    browser.get('https://www.facebook.com/')

    # user_name or e-mail id
    username = username
    password = password


    element = browser.find_elements_by_xpath('//*[@id ="email"]')
    element[0].send_keys(username)


    element = browser.find_element_by_xpath('//*[@id ="pass"]')
    element.send_keys(password)


    # logging in
    log_in = browser.find_elements_by_id('loginbutton')
    log_in[0].click()


    browser.get('https://www.facebook.com/events/birthdays/')

    feed = 'Happy Birthday !'

    element = browser.find_elements_by_xpath("//*[@class ='enter_submit\
    uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea \
        inlineReplyTextArea mentionsTextarea textInput']")

    cnt = 0

    for el in element:
        cnt += 1
        element_id = str(el.get_attribute('id'))
        XPATH = '//*[@id ="' + element_id + '"]'
        post_field = browser.find_element_by_xpath(XPATH)
        post_field.send_keys(feed)
        post_field.send_keys(Keys.RETURN)
        print("Birthday Wish posted for friend" + str(cnt))

    # Close the browser
    browser.close()

    encrypt.encrypt(dir_path + '/credentials/fbe')