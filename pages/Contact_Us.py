import streamlit as st
from utility import ContactForm

st.set_page_config(
    page_title="Bjørn-Magne Portfolio",
    page_icon="./favicon.ico",
)


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
