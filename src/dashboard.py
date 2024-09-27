import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

custom_style = """
<style>

[data-testid="stDecoration"] {
	display: none;
}

/* Hide the Streamlit hamburger menu */
#MainMenu {visibility: hidden;}

/* Set the font size for the tab headers */ 
.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size: 18px;
}

/* Reduce white space on top */
.block-container {
    padding-top: 2rem;
    # padding-left: 5px;
    # padding-right: 5px;
    # padding-bottom: 0;
    # margin-left: 0;
    # margin-right: 0;
}

/* Sticky footer */
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f1f1f1;
    display: flex;
    height: 30px;
    justify-content: center;
    padding: 4px;
    z-index: 1000;
    font-size: smaller;
}

</style>
"""
 
def coming_soon_message(tab_name):
        # Your Streamlit application code
    st.title('Bridge2AI Voice Dashboard')
    st.write(f"{tab_name} - Coming soon!")

    # Add an image to the page
    image_path = "images/Wave.png"  # Replace with your image file name
    st.image(image_path, caption='', use_column_width=True)

def about_page(tab_name):
    coming_soon_message(tab_name)

def healthsheet_page(tab_name):
    coming_soon_message(tab_name)

def study_dashboard_page(tab_name):
    coming_soon_message(tab_name)
    
def study_metadata_page(tab_name):
    coming_soon_message(tab_name)

def dataset_metadata_page(tab_name):
    coming_soon_message(tab_name)
    
def dataset_structure_preview_page(tab_name):
    coming_soon_message(tab_name)

def dataset_quality_dashboard_page(tab_name):
    coming_soon_message(tab_name)
    
def dataset_uses_page(tab_name):
    coming_soon_message(tab_name)

def create_tabs(tabs_func):
    tab_names = list(tabs_func.keys())
    tabs = st.tabs(tab_names)
    for tab, name in zip(tabs, tab_names):
        with tab:
            tabs_func[name](name)

def config_page(version):         
    st.set_page_config(
        page_title="Bridge2AI Voice Dashboard",
        page_icon="images/B2AI Logo.ico",
        layout="wide")

    st.markdown(custom_style, unsafe_allow_html=True)

    # Add the footer
    footer = f"""
    <footer>
       © Weill Cornell Medicine | Version {version} &nbsp;|&nbsp;
       <a href="https://weill.cornell.edu/notice-privacy-practices" target="_blank" style="color: black">Privacy Policy</a> &nbsp;|&nbsp; 
       <a href="https://weill.cornell.edu/weill-cornell-medicine-web-terms-use" target="_blank" style="color: black">Terms of Use</a>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)


def main():  
    # Define the version variable
    version = "0.4.0"
    # Map tab names to functions
    tab_functions = {
        "About": about_page,
        "Healthsheet": healthsheet_page,
        "Study Dashboard": study_dashboard_page,
        "Study Metadata": study_metadata_page,
        "Dataset Metadata": dataset_metadata_page,
        "Dataset Structure Preview": dataset_structure_preview_page,
        "Dataset Quality Dashboard": dataset_quality_dashboard_page,
        "Dataset Uses": dataset_uses_page
    }
    
    # Set page configuration
    config_page(version)
    # Create tabs
    create_tabs(tab_functions)

if __name__ == "__main__":

    main()
