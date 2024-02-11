import os
from twilio.rest import Client

# Initialize Twilio client
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_client = Client(twilio_account_sid, twilio_auth_token)

def lambda_handler(event, context):
    # Specify the message for the call
    call_message = "Your website is down. Immediate attention required."

    # Trigger a phone call using Twilio
    call = twilio_client.calls.create(
        twiml=f'<Response><Say>{call_message}</Say></Response>',
        to='<TARGET_PHONE_NUMBER>',
        from_='<TWILIO_PHONE_NUMBER>'
    )
    
    print(f"Call initiated with SID: {call.sid}")

# Note: Replace 'TARGET_PHONE_NUMBER' and 'TWILIO_PHONE_NUMBER' with actual numbers.
