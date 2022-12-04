# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import random as rd
# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
account_sid = 'AC8247b456a32ed3486802b73ef45b6a6b'
auth_token = 'a4931f421460e2cc23601c0767d3ec47'
client = Client(account_sid, auth_token)

rd.seed()
def sendotp():
    otp = rd.randint(1000,9999)

    message = client.messages.create(body='Hi there your otp is '+str(otp),
                                    from_='+13608032876',
                                    to='+918688833274'
                                    )
    return otp
otp = sendotp()
input_otp = int(input('enter otp  :  '))
if otp==input_otp:
    print('access granted')
else:
    print('access denied')
    print('try again')
    sendotp()
    

