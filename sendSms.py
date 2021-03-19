import os
from readData import *
from twilio.rest import Client


def send_sms( event = None, context= None):
    

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

#message =client.messages.create(from_='+17076402663',
                     # to='+254714869114',
                      #body='Hi Man, whats up')

    message = client.messages \
        .create(
             from_='+17076402663',
             body="A happy new week! Here is a list of people on duty this week 🙏 \n {}  \n See you on Thur at 7pm".format(text_msg),
             to='+254714869114'
         )

