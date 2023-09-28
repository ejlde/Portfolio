import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title = "My Webpage", page_icon =":tada:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: # 200 = successful
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style/", unsafe_allow_html=True)

local_css("style/style.css")


# Load assets
lottie_coding = load_lottieurl("https://lottie.host/91b596fb-cd56-4c7f-910f-6ad19453d683/44qYmVQfXj.json")

img_contact_form = Image.open("images/space.png")
## insert other images here img_contact_form_2

# Header Section
with st.container():
    st.subheader("Hi, I am Eric :wave:")
    st.title("An Aerospace Engineer from Colorado")
    st.write("I am passionate about finding ways to use technology to improve the global quality of life.")
    st.write("[Portfolio >](https://ejldean13.wixsite.com/website)")

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am an aerospace engineer at York Space Systems with an expertise in:
            - Python Development
            - Mission Operations Automation
            - Astronautical Engineering
            """
        )
        # link here
    
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")


# Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Holographic Microscope Investigating Enceladus")
        st.write(
            """
            Optics Lead for a holographic microscope investigating the presence of life
            on Enceladus.
            """
        )
        st.markdown("[LINK TO HOMIE WEBSITE...](WEBSITE LINK HERE)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form) ## insert other image here

# Contact Form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    # https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/ejldean13@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

