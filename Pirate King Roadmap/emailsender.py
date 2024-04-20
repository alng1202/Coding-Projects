''' 
Alan Nguyen
    Project date: 4/17/23 - 4/17/23
    From: Pirate King Roadmap --> freeCodeCamp.org
    Purpose: Create a simple email sender using the EmailMessage library
'''

###### WORK STARTS BELOW ######

## email password code: vvpa ugpd pauu wgxd

## main email formatter/creator library
from email.message import EmailMessage
# secure socket layer (SSL)
# provides access to Transport Layer Security
import ssl 
import smtplib

email_sender = 'alannguyen321@gmail.com'
# for google, go into account settings and input app password
email_password = 'vvpa ugpd pauu wgxd'

email_receiver = 'alanhoangng@gmail.com' # change email to any recipient 

subject = "Email Subject"

body = """
Email Body

Pirate King Roadmap
"""
## create an EmailMessage instance
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()


# Google's gmail smtp server: smtp.gmail.com
# port: 465
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string()) # convert all content in instance to string to allow sending