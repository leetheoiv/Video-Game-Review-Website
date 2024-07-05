import streamlit as st
from layout.main import *
# from models.main import *
from streamlit_option_menu import option_menu
from layout.home import Home
from layout.submit_review import Submit_Review
from layout.data_viz import *

# Function to read the content of style.css
def get_style():
    with open("layout/style.css", "r") as f:
        return f.read()

with open("layout/layout.html",'r') as f:
    html_data = f.read()

# Show in webpage
st.markdown(html_data, unsafe_allow_html=True)

# Apply the custom CSS
custom_css = get_style()
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Create page sidebar
with st.sidebar:
    selected=option_menu(
        menu_title='Menu',
        options=['Home','Submit a Review','Data Viz'],
        icons = ['house','chat-square-quote','bar-chart-line'],
        default_index=0
    )

if selected == 'Home':
    Home()

if selected == 'Submit a Review':
    Submit_Review()

if selected == 'Data Viz':
    dataviz()











