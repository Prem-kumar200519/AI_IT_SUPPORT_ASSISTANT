import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

print("BREVO API KEY:", BREVO_API_KEY)


def send_email(receiver_email, subject, body):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "AI IT Support Assistant",
            "email": "itsmeprem200519@gmail.com"
        },
        "to": [
            {
                "email": receiver_email
            }
        ],
        "subject": subject,
        "textContent": body
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )
    
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code not in [200, 201]:
        raise Exception(response.text)