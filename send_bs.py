import smtplib
import ssl
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import requests
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


load_dotenv()


# ----- Get the verse of the day 

res = requests.get("https://www.biblegateway.com")
soup = BeautifulSoup(res.content, 'html.parser')

book = soup.find('span', class_='citation').text
text = soup.find('div', id='verse-text').text


EMAIL_ADD = os.getenv("EMAIL_ADD")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_mail(send_from: str, subject: str, text: str,
              send_to: list, files=None):
    send_to = default_address if not send_to else send_to

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_ADD, EMAIL_PASS)
    server.sendmail(send_from, send_to, msg.as_string())
                    
to_emails = ['ednaodhiambo@gmail.com', 'mosotieno25@gmail.com']

send_mail(send_from=EMAIL_ADD,
          subject="Verse of the day",
          text="Dear Mosedna, \n"
                "Verse of the day is \r\n"
                f"{book}.  \n"
                f"{text} \n\r"
                "Regards, \n"
                "Moses",
            send_to=to_emails)


