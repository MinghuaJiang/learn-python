import smtplib

sender = 'test@virginia.edu'
receiver = 'mj2eu@virginia.edu'

message = """From: %s
To: %s
Subject: SMTP e-mail test

This is a test e-mail message.
""" % (sender, receiver)

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, [receiver], message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"


message = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
""" % (sender, receiver)

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, [receiver], message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"

