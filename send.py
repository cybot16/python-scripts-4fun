import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'user.name'
password = 'password'
sender = 'user.name@gmail.com'
targets = ['my.email@gmail.com']

msg = MIMEText('This is the mail content')
msg['Subject'] = 'This is the mail subject'
msg['From'] = sender
msg['To'] = ', '.join(targets)
try:
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()
except Exception, e:
    print e
