from twilio.rest import Client

def sendSms():
    account_sid = 'AC2d2644a19c071b01fa7ef2fd8892bb64'
    auth_token = 'b7472543797690c104714e599bf4e7fa'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12565784053',
        body='Intruder Detected',
        to='your_phone_number'
    )

    print(message.sid)
