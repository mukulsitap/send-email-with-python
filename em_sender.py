import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) #html page that you want to send as mail
email = EmailMessage()
recipient = ['xyz@mail.com', 'abc@mail.com'] #recipient emails

email['from'] = 'xyz abc' #enter your name
email['to'] = recipient
email['subject'] = 'This is send from python' #subject for mail

email.set_content(html.substitute(name = 'ABCD'), 'html') #'name' variable is refer from html page with '$' sign

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp :
	smtp.ehlo()
	smtp.starttls()
	smtp.login('yourmail@mail.com', 'yourmailPassword') #enter your mail id and password 
	smtp.send_message(email)
	print("done!!")