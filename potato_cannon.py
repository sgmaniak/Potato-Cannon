# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACa47a4aa2ba8587cbb1129f10e988da1e"
auth_token = "564b5a658c755ac4e9f49f9ec98b296c"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12316851234", from_="+15555555555", body="Potato!")
