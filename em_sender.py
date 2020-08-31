import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
emaillist = ['mukulsitap@gmail.com', 'dsitap1975@gmail.com']

email['from'] = 'D Sitap'
email['to'] = emaillist
email['subject'] = 'This is send from python'

email.set_content(html.substitute(name = 'MukulSitap'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp :
	smtp.ehlo()
	smtp.starttls()
	smtp.login('vrushalisitap@gmail.com', 'Sitap@123')
	smtp.send_message(email)
	print("done!!")