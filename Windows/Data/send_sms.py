#! python3

import requests
import json

from Data import encrypt
import base64

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Post request
def sendPostRequest(phoneNo, fname):

    encrypt.decrypt(dir_path + '/credentials/se')
    with open(dir_path + '/credentials/se', mode='rb') as f:
        content = f.read()
        content = base64.b64decode(content).decode('utf-8')

    ApiKey = str(content.split()[0])

    message = "Birthdays are a new start; fresh beginnings, a time to start new endeavours with new goals. Move forward with fresh confidence and courage. You are a special person, may you have an amazing today and year. Happy birthday " + fname
    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS" + "&message=" + message + "&language=english&route=p&numbers=" + phoneNo
    headers = {
        'authorization': ApiKey,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    encrypt.encrypt(dir_path + '/credentials/se')
    return requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)