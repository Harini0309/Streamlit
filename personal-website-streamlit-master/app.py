import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/new.png")
img_lottie_animation = Image.open("images/new1.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Kudos, I am Harini Selvaraj :wave:")
    st.title("An inspiring Data Scientist Student")
    st.write(
        "I am passionate about learning new stuffs daily."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/hariniselvaraj03/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am currently pursuing my B.Tech in Artificial Intelligence and Data Science at KPR Institute of Engineering and Technology.
             My short time goal is to get placed in an esteemed organization. My long time goal is to complete MS Degree.
             I am capable enough in building a Machine Learning model for given dataset. I am more interested towards learning Deep Learning. 
            """
        )
        st.write("[Github >](https://github.com/Harini0309)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/hariniselvaraj@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Feedback" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
