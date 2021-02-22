
from twilio.rest import Client

account_sid = "ACe078720c9ab1467e341cdaa930fdf137"
auth_token = "ea2f551405393bde133e96f2baed413e"
client = Client(account_sid, auth_token)


call = client.calls.create(
    to="+998909009301",
    from_="+998909963101",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
