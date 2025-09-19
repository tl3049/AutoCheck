import time
import schedule
import smtplib, ssl
from email.message import EmailMessage
from check import check_author
import os


EMAIL_USER = os.environ.get("EMAIL_USER")
TO_ADDR = os.environ.get("TO_ADDR")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
NAME = os.environ.get("NAME")
URL = os.environ.get("URL")
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
def job(name, url):
    print("任务开始执行...")
    published, words = check_author(name, url)
    if published:
        subject = "您的IJCAI论文已出版✅"
        body = "Congratulations! " + words
        send_email(subject, body)
        print("已发送邮件。")
        global WORKING
        WORKING = False
    else:
        print("条件未满足。")


if __name__ == '__main__':
    job(name = NAME, url = URL)

# # ========== 定时调度 ==========
#schedule.every().hour.do(job)   # 每小时执行一次
# schedule.every(1).minutes.do(job)
# print("定时任务启动，每隔 1 小时运行一次...")
# while WORKING:
#     schedule.run_pending()
#     time.sleep(5)

# print("This is the end of the program.")