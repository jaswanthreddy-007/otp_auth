
import os
from twilio.rest import Client
import random as rd
import pyotp


secret = pyotp.random_base32()
totp = pyotp.TOTP(secret) 
filename = 'otp_auth/twilliokey.txt'
account_sid = 'AC8247b456a32ed3486802b73ef45b6a6b'
# try:
#         with open(filename, 'r') as f:
#             auth_token= f.read().strip()
#except FileNotFoundError:
 #   print("'%s' file not found" % filename)
#auth_token = 616fdcc1b3277cbf6ebc207c0abcffdc
client = Client(account_sid, "616fdcc1b3277cbf6ebc207c0abcffdc")


def sendotp():
    otp = totp.now()

    message = client.messages.create(body='Hi there your otp is '+otp,
                                    from_='+13608032876',
                                    to='+919866866572'
                                    )
    return otp
otp = sendotp()
input_otp = (input('enter otp  :  '))

#print(otp)
if otp == input_otp:
    print('access granted')
else:
    print('access denied')
    
    

