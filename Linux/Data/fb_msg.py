
from fbchat import Client
from fbchat.models import *

from Data.encrypt import *
import base64

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def send_fmsg(FirstName, Last_Name, GroupNames):

    decrypt(dir_path + '/credentials/fbe')
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

    encrypt(dir_path + '/credentials/fbe')
