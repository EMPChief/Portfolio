import streamlit as st
import json

class PortfolioApp:
    def __init__(self):
        self.projects = self.load_projects("db.json")

    def set_page_config(self):
        st.set_page_config(
            page_title="Bjørn-Magne Portfolio",
            page_icon="favicon.ico",
        )

    def load_projects(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    def display_welcome_message(self):
        st.markdown("<h3 style='text-align: center;'> Welcome to my portfolio!</h3>", unsafe_allow_html=True)

    def display_about_me(self):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image('enhanced_img215931713926.png', width=400)
        with col2:
            st.markdown("<h3 style='text-align: center;'> Bjørn-Magne Kristensen</h3>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 18px; text-align: center; background-color: rgba(0, 128, 0, 0.3); padding: 10px;'>Hello there! I'm bjørn-magne, and I'm exploring the world of programming in my free time. Join me on this journey as I learn and create!</p>", unsafe_allow_html=True)

    def display_project_list(self):
        st.markdown("<h3 style='text-align: center;'> Project List:</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        image_folder = "images/"
        for i, project in enumerate(self.projects):
            with col1 if i % 2 == 0 else col2:
                image_path = image_folder + project["image"]
                description = f"{project['description']}"
                st.markdown(f"<h3 style='text-align: center;'>{project['title']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center;'>{description}</p>", unsafe_allow_html=True)
                st.image(image_path, use_column_width=True)
                button_label = f"Go to source code"
                st.markdown(f"<div style='text-align: center;'><a href='{project['url']}' target='_blank'>{button_label}</a></div>", unsafe_allow_html=True)


    def run(self):
        self.set_page_config()
        self.display_welcome_message()
        self.display_about_me()
        self.display_project_list()

if __name__ == "__main__":
    app = PortfolioApp()
    app.run()
