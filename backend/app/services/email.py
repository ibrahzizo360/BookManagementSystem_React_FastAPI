import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
import hashlib
import secrets
import string
from app.config import settings

sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

def generate_verification_code(length=8):
    digit = string.digits
    return ''.join(secrets.choice(digit) for i in range(length))


from_email = Email(settings.FROM_EMAIL) 



def send_verification_code(to_email: str):
    verification_code = generate_verification_code()
    hashed_verification_code = hashlib.sha256(verification_code.encode('iso-8859-1')).hexdigest()
    body = f"Your verification code is {verification_code}"
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject="Email verification code",
        html_content=body
    )
    sg.send(message)
    return hashed_verification_code
