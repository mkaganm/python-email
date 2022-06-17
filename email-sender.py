import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import content


msg = MIMEMultipart()
msg["From"] = content.sender
msg["To"] = content.to
msg["Subject"] = content.subject

text = content.text

msg_body = MIMEText(text, "plain")
msg.attach(msg_body)

try:
    mail = smtplib.SMTP("smtp.office365.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(content.sender, content.pswrd)

    mail.sendmail(msg["From"], msg["To"], msg.as_string())
    print("Email process is successful")
    mail.close()

except:
    sys.stderr.write("ERROR!?!...")
    sys.stderr.flush()
