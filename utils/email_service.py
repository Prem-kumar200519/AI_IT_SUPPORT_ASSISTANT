import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(receiver_email, subject, body):

    message = EmailMessage()

    message["Subject"] = subject
    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver_email

    message.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        smtp.send_message(message)