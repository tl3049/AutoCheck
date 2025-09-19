import time
import schedule
import smtplib, ssl
from email.message import EmailMessage
from check import check_author
import os


EMAIL_USER = os.environ.get("EMAIL_USER")
TO_ADDR = os.environ.get("TO_ADDR")#first recipient
TO_ADDR_2 = os.environ.get("TO_ADDR_2")#second recipient
EMAIL_PASS = os.environ.get("EMAIL_PASS")
NAME = os.environ.get("NAME")
URL = os.environ.get("URL")


# ========== Send emails ==========
def send_email(subject: str, body: str, addr: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = addr
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

# ========== Job Function ==========
def job(name, url):
    print("任务开始执行...")
    published, words = check_author(name, url)
    if published:
        subject = "您的论文已出版✅"
        body = "Congratulations! " + words
        send_email(subject, body, TO_ADDR)
        send_email(subject, body, TO_ADDR_2)
        print("已发送邮件。")
    else:
        print("条件未满足。")


if __name__ == '__main__':
    job(name = NAME, url = URL)
