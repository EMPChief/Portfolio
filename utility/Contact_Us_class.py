import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


"""
ContactForm class for sending contact form emails.

Initializes with SMTP server details and provides a send_email() 
method to send the contact form contents to the configured 
email address.
"""


class ContactForm:
    def __init__(self):
        self.smtp_server = "smtp.hostinger.com"
        self.smtp_port = 587
        self.smtp_username = "support@empchief.com"
        self.smtp_password = "&833NjKXpb7xjPLo"

    def send_email(self, name, email, message):
        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        msg = MIMEMultipart()
        msg['From'] = self.smtp_username
        msg['To'] = self.smtp_username
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.smtp_username,
                            self.smtp_username, msg.as_string())
