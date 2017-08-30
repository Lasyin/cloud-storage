import smtplib

subject = "New backup happened!"   # the subject of the email to be sent
FROM_EMAIL = "INSERT_EMAIL_HERE"   # the sender of the email (your email account)
PASS = "INSERT_PASSWORD_HERE"      # the password for your email account
TO_EMAIL = "INSERT_EMAIL_HERE"     # the receiver of the email (should also be your email account)

def sendEmail(text):
    theMsg = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FROM_EMAIL,PASS)

    print("sending: " + theMsg)
    server.sendmail(FROM_EMAIL, TO_EMAIL, theMsg)
    server.quit()
