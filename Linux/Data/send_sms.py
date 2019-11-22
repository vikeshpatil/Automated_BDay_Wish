
import requests
from Data.encrypt import *
import base64

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# get request
def sendPostRequest(phoneNo, fname):

    decrypt(dir_path + '/credentials/se')
    with open(dir_path + '/credentials/se', mode='rb') as f:
        content = f.read()
        content = base64.b64decode(content).decode('utf-8')

    ApiKey = str(content.split()[0])
    SecreteKey = str(content.split()[1])
    SenderId = str(content.split()[2])

    reqUrl = 'https://www.way2sms.com/api/v1/sendCampaign'
    req_params = {
        'apikey': ApiKey,
        'secret': SecreteKey,
        'usetype': 'prod',
        'phone': phoneNo,
        'message': "Birthdays are a new start; fresh beginnings, a time to start new endeavours with new goals. Move forward with fresh confidence and courage. You are a special person, may you have an amazing today and year. Happy birthday" + fname,
        'senderid': SenderId
  }
    encrypt(dir_path + '/credentials/se')
    return requests.post(reqUrl, req_params)
#   response = sendPostRequest('send to', 'message')

# print response if you want
# print(response.text)