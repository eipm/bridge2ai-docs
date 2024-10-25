import streamlit as st
from tabs.about import about_page
from tabs.healthsheet import healthsheet_page
from tabs.study_dashboard import study_dashboard_page
from tabs.study_metadata import study_metadata_page
from tabs.dataset_metadata import dataset_metadata_page
from tabs.dataset_structure_preview import dataset_structure_preview_page
from tabs.dataset_quality_dashboard import dataset_quality_dashboard_page
from tabs.dataset_uses import dataset_uses_page

def config_page(version):         
    st.set_page_config(
        page_title="Bridge2AI Voice Dashboard",
        page_icon="images/B2AI Logo.ico",
        layout="wide")

    # Add the CSS file
    with open("css/dashboard.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.logo("images/B2AI Logo.png", )

    # Add the footer
    footer = f"""
    <footer>
       © Weill Cornell Medicine | Version {version} &nbsp;|&nbsp;
       <a href="https://weill.cornell.edu/notice-privacy-practices" target="_blank">Privacy Policy</a> &nbsp;|&nbsp; 
       <a href="https://weill.cornell.edu/weill-cornell-medicine-web-terms-use" target="_blank">Terms of Use</a>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)

def create_tabs(tabs_func):
    tab_names = list(tabs_func.keys())
    tabs = st.tabs(tab_names)
    for tab, name in zip(tabs, tab_names):
        with tab:
            tabs_func[name](name)

def main():  
    # Current version of the app
    version = "0.5.0"
    # Map tab names to functions
    # In this dictionary, the key is the tab name and the value is the function that will be called when the tab is selected
    # The function is defined in the respective file
    # about_page() is defined in tabs/about.py
    # healthsheet_page() is defined in tabs/healthsheet.py
    # study_dashboard_page() is defined in tabs/study_dashboard.py
    # study_metadata_page() is defined in tabs/study_metadata.py
    # dataset_metadata_page() is defined in tabs/dataset_metadata.py
    # dataset_structure_preview_page() is defined in tabs/dataset_structure_preview.py
    # dataset_quality_dashboard_page() is defined in tabs/dataset_quality_dashboard.py
    # dataset_uses_page() is defined in tabs/dataset_uses.py
    
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