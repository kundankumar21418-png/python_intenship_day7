import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
RECEIVER = "receiver@gmail.com"

msg = EmailMessage()
msg['From'] = EMAIL
msg['To'] = RECEIVER
msg['Subject'] = "Test Email"
msg.set_content("This is a Python test email :)")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)