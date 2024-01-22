import streamlit as st
import json
#Page settings
st.set_page_config(
    page_title="Bjørn-Magne Portfolio",
    page_icon="favicon.ico",
)

# Importing the projects from the json file
with open("db.json", "r") as file:
    projects = json.load(file)

# Welcome message
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='text-align: center;'> Welcome to my portfolio!</h3>", unsafe_allow_html=True)

# About me section with image
col1, col2 = st.columns([2, 1])
with col1:
    st.image('enhanced_img215931713926.png', width=400)
with col2:
    st.markdown("<p style='font-size: 18px; text-align: center;'>Hello there! I'm bjørn-magne, and I'm exploring the world of programming in my free time. Join me on this journey as I learn and create!</p>", unsafe_allow_html=True)

# Project List
st.markdown("<h3 style='text-align: center;'> Project List:</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
image_folder = "images/"
for i, project in enumerate(projects):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"<h3 style='text-align: center;'>{project['title']}</h3>", unsafe_allow_html=True)
        
        image_path = image_folder + project["image"]
        description = f"{project['description']}"
        st.image(image_path, caption=description, use_column_width=True)
        button_label = f"Open {project['title']} Website"
        st.markdown(f"<div style='text-align: center;'><a href='{project['url']}' target='_blank'>{button_label}</a></div>", unsafe_allow_html=True)
