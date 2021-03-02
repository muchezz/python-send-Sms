import os
from twilio.rest import Client


account_sid = 'ACfeab8754347b3ce85a356a7d62ea193a',
auth_token = '8a1027373307a309a929653f7d56373a'
#account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message =client.messages.create(from_='+17076402663',
                      to='+254714869114',
                      body='You just sent an SMS from Python using Twilio!')

print(message.sid)