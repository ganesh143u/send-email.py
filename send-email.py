import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'ganeshmudhiraj44@gmail.com'
email_password =os.environ.get("EMAIL_PASSWORD") #HERE WRITE THE PASSWORD OF 16 DIGITS THIS PASSWORD YOU WILL GET FROM YOUR GOOGLE ACCOUNT APP PASSWORDS
email_receiver = 'rowdyloveu062@gmail.com'

subject = ' hello worlds'
body = """
jhgadfugduhkj
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

