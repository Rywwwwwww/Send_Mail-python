#Gmailにメールを送信する.

from email import message
import smtplib


smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'ryo1996092668@gmail.com'
to_email = 'ryo1996092668@gmail.com'
username = 'ryo1996092668@gmail.com'
password = 'rghvrayimkdnmubn'

msg = message.EmailMessage()
msg.set_content('テストメールやで......')
msg['Subject'] = 'Test mail from Gmail'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()

