"""
Write a program that will send an email to people by having their email stored in a dictionary.
 """


import smtplib, email, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
fromaddr = 'samandevacc20@gmail.com'
x = open('/Users/saman/Desktop/pas.txt', 'r')
password = x.read()
subject = "Python Programming Email"
body = "This is an email with attachment sent from Python"
sender_email = fromaddr
receiver_email = ''


context = ssl.create_default_context()

server.login(sender_email, password)

server.login(fromaddr, password)
t_p = '''Hello To You! I am writing this letter to say I have learned to send many emails using python. I 
am Saman. :) '''
text_m = '''
Hello To You! I am writing this letter to say I have learned to send many emails using python. I 
am Saman. :)

'''
html = """\
<html>
  <body>
    <p><br>
       Thanks for Everything ! <br>
       There is a wallpaper attached below this mail, just to show I know how to use them... :-)
    </p>
  </body>
</html>
"""

ImgFileName = "/Users/saman/Desktop/picture.jpeg"
img_data = open(ImgFileName, 'rb').read()
msg = MIMEMultipart()
image = MIMEImage(img_data, name=ImgFileName)


part2 = MIMEText(html, "html")


contacts = {
    'P': 'SAMPLE_EMAIL_1@gmail.com',
    'M': 'SAMPLE_EMAIL_2@gmail.com',

}
for contact, toaddr in contacts.items():
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = toaddr
    message["Subject"] = subject
    message["Bcc"] = receiver_email
    if contact == 'P':
        part1 = MIMEText(text_p, "plain")
        message.attach(part1)
        message.attach(part2)
        message.attach(image)
        server.sendmail(fromaddr, toaddr, message.as_string())
    elif contact == "M":
        part1 = MIMEText(text_m, "plain")
        message.attach(part1)
        message.attach(part2)
        message.attach(image)
        server.sendmail(fromaddr, toaddr, message.as_string())

server.quit()
