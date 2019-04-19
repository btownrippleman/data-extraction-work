import twilio
from twilio.rest import Client

account = ##.. 
token = ##.. 
client = Client(account, token)

message = client.messages.create(
    to="2092517035", 
    from_="8019358918",
    body="Hello from Python!")

print(message.sid)