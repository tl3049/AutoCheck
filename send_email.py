import time
import schedule
import smtplib, ssl
from email.message import EmailMessage
from check import check_author
import os

# ========== Environment Variables ==========
EMAIL_USER = os.environ.get("EMAIL_USER")
TO_ADDR = os.environ.get("TO_ADDR")#first recipient
TO_ADDR_2 = os.environ.get("TO_ADDR_2")#second recipient
EMAIL_PASS = os.environ.get("EMAIL_PASS")
NAME = os.environ.get("NAME")
URL = os.environ.get("URL")


# ========== Send emails ==========
def send_email(subject: str, body: str, addr: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER#sender
    msg["To"] = addr#receiver
    msg["Subject"] = subject#subject
    msg.set_content(body)#body

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:#smtp server
        smtp.login(EMAIL_USER, EMAIL_PASS)#login
        smtp.send_message(msg)#send the email

# ========== Job Function ==========
def job(name, url):
    print("Excuting the job...")
    published, words = check_author(name, url)#check if the paper is published
    if published:
        subject = "Your paper has been published✅"
        body = "Congratulations! " + words
        send_email(subject, body, TO_ADDR)#send the msg to the first recipient
        send_email(subject, body, TO_ADDR_2)#send the msg to the second recipient
        print("Mail sent successfully.")
    else:
        print("Not published yet.")


if __name__ == '__main__':
    job(name = NAME, url = URL)#excute the job once
