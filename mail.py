import smtplib, ssl
import config
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Sender, Reciever, Body of Email
sender = config.mail
receivers = ['500067717@stu.upes.ac.in']
body_of_email = 'Hey Gaurav tries to use your device'

#Creating the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Face_detected'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#Adds a csv file as an attachment to the email 
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('./pic1.jpg', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="harsh.jpg"')
msg.attach(part)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = config.mail, password = config.password)
s.sendmail(sender, receivers, msg.as_string())
s.quit()
print('MAIL SENT')