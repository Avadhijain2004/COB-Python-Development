# Python program that automates sending emails using Python's SMTP Library

import smtplib

sender_email = input("Sender_Email: ")
receiver_email = input("Receiver_Email: ")

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject : {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
app_password_key = "" #Enter your app password key 
server.login(sender_email,app_password_key)
server.sendmail(sender_email,receiver_email,text)

print("Email has been sent to " + receiver_email)