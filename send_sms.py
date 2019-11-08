import requests

# get request
def sendPostRequest(phoneNo, fname):
    reqUrl = 'https://www.way2sms.com/api/v1/sendCampaign'
    req_params = {
        'apikey':'IG6MLQ7K5VN7JIJS59U0S8MDFUQ2D8S1',  #replcae with original api key
        'secret':'6J8EFICA4MMLZS0W',   #replace with original secrete key
        'usetype':'stage',        #replace with prod during production stage
        'phone': phoneNo,
        'message': """Birthdays are a new start;\n fresh beginnings, a time to start new endeavours with new goals.\n Move forward with fresh 
                    confidence and courage. You are a special person,
                    may you have an amazing today and year.\n Happy birthday""" + fname,
        'senderid': '8600700549'
  }
    return requests.post(reqUrl, req_params)

#   response = sendPostRequest('send to', 'message')

# print response if you want
# print(response.text)