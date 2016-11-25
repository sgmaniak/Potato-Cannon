from twilio.rest import TwilioRestClient


def get_phone_number_from_input():
    #Emma's job!


account_sid = "ACa47a4aa2ba8587cbb1129f10e988da1e"
auth_token = "564b5a658c755ac4e9f49f9ec98b296c"
client = TwilioRestClient(account_sid, auth_token)

print('Arrr!! Ahoy Matey! I have this Potato Cannon here, and its achin\' for a good launch! Yaaa ha ha *cough* ha haa!!)

print('Yar gonna need to give me your phone number if ya want to send a potato!')

#get phone number and store it in a variable as a string
sender_phone_number =


print('Now give me the phone number of the poor soul on the receivin\' end!')

receving_phone_number = #??????

/# TODO: Change the phone numbers
message = client.messages.create(to="+12316851234", from_="+15555555555", body="Potato!")
