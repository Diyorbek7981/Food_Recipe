import re
import threading
import phonenumbers
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError
from twilio.rest import Client
from django.conf import settings
import smtplib
import vonage
from config.settings import EMAIL, CODE

# email yoki telefon raqamiga tekshiradi ------------------------>

email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
phone_regex = re.compile(r"(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+")
username_regex = re.compile(r"^[a-zA-Z0-9_.-]+$")


def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        email_or_phone = "email"

    elif len(email_or_phone) == 13 and email_or_phone.startswith("+998"):
        email_or_phone = 'phone'

    else:
        data = {
            "success": False,
            "message": "Kiritilgan malumot noto'g'ri"
        }
        raise ValidationError(data)

    return email_or_phone


# email username va telefon raqamini regex orqali tekshiradi---------------------->

#  Loginda kiritilgan inputni username email yoki phonega ajratib beradi
def check_user_type(user_input):
    if re.fullmatch(email_regex, user_input):
        user_input = 'email'

    elif re.fullmatch(phone_regex, user_input):
        user_input = 'phone'

    elif re.fullmatch(username_regex, user_input):
        user_input = 'username'

    else:
        data = {
            "success": False,
            "message": "Email, username yoki telefon raqamingiz noto'g'ri"
        }
        raise ValidationError(data)
    return user_input


# ---------------------------------------------------------- Emailga code jo'natish
def send_email(email, code):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    # s.login('email', "password")
    s.login(EMAIL, CODE)
    # message to be sent
    subject = 'Salom do`stim! Sizning tasdiqlash kodingiz:'
    body = code

    message = f'Subject: {subject}\n\n{body}'
    # sending the mail

    s.sendmail("abdurahimov.diyorbek7981@gmail.com", f"{email}", message)
    # terminating the session
    s.quit()


# --------------------------------------------------------------------------------

# twilioda telefon raqamiga code yuborish ------------------------------------------->


def send_phone_code(phone, code):
    # account_sid = settings.TWILIO_ACCOUNT_SID
    # auth_token = settings.TWILIO_AUTH_TOKEN
    # client = Client(account_sid, auth_token)
    # client.messages.create(
    #     body=f"Salom do'stim! Sizning tasdiqlash kodingiz: {code}\n",
    #     from_="+15612993508",  # twiliodagi raqam
    #     to=f"{phone}"
    # )

    client = vonage.Client(key="3c60d33a", secret="j86gYfqwcMkipXhu")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": f"{phone}",
            "text": f"Hello Diyorber {code}",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
