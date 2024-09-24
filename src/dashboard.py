import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

custom_style = """
<style>
/* Hide the Streamlit hamburger menu */
#MainMenu {visibility: hidden;}

</style>
"""
    
st.set_page_config(
    page_title="Bridge2AI Voice Dashboard",
    page_icon="images/B2AI Logo.ico",
    layout="wide")

st.markdown(custom_style, unsafe_allow_html=True)

# Your Streamlit application code
st.title('Bridge2AI Voice Dashboard')
st.write("Coming soon!")

# Add an image to the page
image_path = "images/Wave.png"  # Replace with your image file name
st.image(image_path, caption='', use_column_width=True)

