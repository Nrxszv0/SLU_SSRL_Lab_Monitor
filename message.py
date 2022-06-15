#from Clarity Coders

import smtplib
from email.message import EmailMessage

def email_alert(to, subject, body):
    msg= EmailMessage()
    msg.set_content(body)

    msg['subject'] = subject
    msg['to'] = to  
    
    user = "slubotssrl@gmail.com"
    msg['from'] = user
    password = "uckyzdrtlxqnsdjv"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)

    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    # email_alert("Michael.crothersmc@gmail.com", "Subject", "Body")
    email_alert("6366759462@txt.att.net", "Hi", "Hello")

