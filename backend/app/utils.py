from .config import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

def send_email(to_email: str, subject: str, html_body: str, plain_body: str = ""):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = to_email

    part1 = MIMEText(plain_body or html_body, "plain")
    part2 = MIMEText(html_body, "html")
    msg.attach(part1)
    msg.attach(part2)

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            if settings.SMTP_USER and settings.SMTP_PASSWORD:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.sendmail(settings.EMAIL_FROM, to_email, msg.as_string())
    except Exception as e:
        print("Error sending email:", e)

def send_fcm_notification(server_key: str, device_token: str, title: str, body: str):
    if not server_key or not device_token:
        return
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
        "Authorization": f"key={server_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": device_token,
        "notification": {
            "title": title,
            "body": body
        }
    }
    try:
        requests.post(url, json=payload, headers=headers, timeout=5)
    except Exception as e:
        print("FCM send error:", e)
