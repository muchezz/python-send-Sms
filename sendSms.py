import os
from twilio.rest import Client


account_sid = ' ',
auth_token = ''
#account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message =client.messages.create(from_='',
                      to='',
                      body='You just sent an SMS from Python using Twilio!')

print(message.sid)