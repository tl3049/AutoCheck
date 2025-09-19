import time
import schedule
import smtplib, ssl
from email.message import EmailMessage
from dotenv import load_dotenv
from check import check_author
import os

load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
TO_ADDR = os.getenv("TO_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
WORKING = True


# ========== 邮件发送函数 ==========
def send_email(subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = TO_ADDR
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

# ========== 任务函数 ==========
def job():
    print("任务开始执行...")
    published, words = check_author()
    if published:
        subject = "您的IJCAI论文已出版✅"
        body = "Congratulations! " + words
        send_email(subject, body)
        print("已发送邮件。")
        global WORKING
        WORKING = False
    else:
        print("条件未满足。")


# subject = "This is a test email"
# body = "Hi, Please ignore this message"
# send_email(subject, body)


# # ========== 定时调度 ==========
#schedule.every().hour.do(job)   # 每小时执行一次
schedule.every(1).minutes.do(job)
print("定时任务启动，每隔 1 小时运行一次...")
while WORKING:
    schedule.run_pending()
    time.sleep(5)

print("This is the end of the program.")