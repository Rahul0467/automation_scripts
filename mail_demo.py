import imghdr
import os
import smtplib
from email.message import EmailMessage

email_address = os.environ.get("gmail_user")
email_password = os.environ.get("gmail_password")

msg = EmailMessage()
msg["Subject"] = "Photo"
msg["From"] = email_address
msg["To"] = ["rahulharinath098@gmail.com"]
msg.set_content("This is a plain text email")

msg.add_alternative("""\
<!doctype html>
<html>
    <body>
        <h1 style="color:SlateGrey;"> This is an HTML Email! </h1>
    </body>
</html>
""", subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
