"""Steven Sousa - 03/04/2021
This scripts sends email to people using Gmail as your email service.
Not that it is important to leave ON a feature in your Google Account
called Less Secure App Access, which is under the Security menu."""

# import necessary libraries
import smtplib
from email.mime.text import MIMEText

# Program starts by asking how many recipients you want to email
number_of_recipients = int(input("How many recipients? "))

# Type your email (Gmail) address that will be sending the message
sender = 'email@gmail.com'

# Type body of message
body_of_email = str(input("Type message: "))

# Encode message to html
msg = MIMEText(body_of_email, 'html')

# Fill out the subject field of email
msg['Subject'] = str(input("What's the subject? "))

# put sender (your email address) in the from field of email
msg['From'] = sender

# This host and port are for Google accounts. Look up Outlook or any other email service should you want to use them.
s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)

# You should allow the script to log in to your account in order for it to send the email.
s.login(user='email@gmail.com', password='your email address password')

# This for loop is how I managed to make this script send emails to multiple contacts.
for i in range(number_of_recipients):
    receiver = input("Type receivers email address: ")  # type recipient's email address
    msg['To'] = ''.join(receiver)                       # Places recipients email address in To field of email
    s.sendmail(sender, receiver, msg.as_string())       # Sends email

s.quit()
