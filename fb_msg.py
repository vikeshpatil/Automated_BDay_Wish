import fbchat
import base64

def send_msg():

    username = 'rajp8340@gmail.com'
    password = 'Nobi@6464' #base64.decode("b'Tm9iaUA2NDY0'".decode('utf-8'))

    client = fbchat.Client(username, password)
    client.login(username, password)

    if client.isLoggedIn():
        print('logged in')
    else:
        print('not logged in')
    # name = "Darshan"
    # friends = client.getUsers(name)
    # print(friends)
