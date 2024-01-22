import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
st.set_page_config(
    page_title="Bjørn-Magne Portfolio",
    page_icon="favicon.ico",
)
class ContactForm:
    def __init__(self):
        self.smtp_server = "smtp.hostinger.com"
        self.smtp_port = 587
        self.smtp_username = "support@empchief.com"
        self.smtp_password = "&833NjKXpb7xjPLo"

    def send_email(self, name, email, message):
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        msg = MIMEMultipart()
        msg['From'] = self.smtp_username
        msg['To'] = self.smtp_username
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.smtp_username, self.smtp_username, msg.as_string())

def main():
    st.header("Contact us!")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    contact_form = ContactForm()

    if st.button("Submit"):
        contact_form.send_email(name, email, message)
        st.success("Thank you for contacting us!")

if __name__ == "__main__":
    main()
