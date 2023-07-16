import os
from twillio.rest import Client
import time

account_sid = os.environ("TWILLIO_SID")
account_token = os.environ("TWILLIO__ACCOUNT_TOKEN")
client = Client(account_sid,account_token)

while True:
    message = client.messages.create(body=input("DIGITE MENSAGEM"),from="NUMBER_IN_TWILLIO",to=input("NUMERO QUE RECEBERA MENSAGEM"))
    print(message.sid)
    time.sleep(60)
