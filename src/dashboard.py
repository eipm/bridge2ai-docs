import streamlit as st

from tabs.overview import overview_page
from tabs.collection_methods import collection_methods_page
from tabs.data_governance import data_governance_page
from tabs.study_dashboard import study_dashboard_page
from tabs.study_metadata import study_metadata_page
from tabs.healthsheet import healthsheet_page
from tabs.data_pre_processing import data_pre_processing_page
from tabs.ai_readiness import ai_readiness_page

def config_page(version):         
    st.set_page_config(
        page_title="Bridge2AI Voice Dashboard",
        page_icon="images/B2AI Logo.ico",
        layout="wide")

    # Add the CSS file
    with open("css/dashboard.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Add review notice header
    st.markdown("""
    <div class="review-notice">
        This repository is under review for potential modification in compliance with Administration directives.
    </div>
    """, unsafe_allow_html=True)

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
    version = "2.0.0"
    # Map tab names to functions
    # In this dictionary, the key is the tab name and the value is the function that will be called when the tab is selected
    # The function is defined in the respective file
    # overview_page() is defined in tabs/overview.py
    # collections_methods_page() is defined in tabs/collections_methods.py
    # data_governance_page() is defined in tabs/data_governance.py
    # study_dashboard_page() is defined in tabs/study_dashboard.py
    # study_metadata_page() is defined in tabs/study_metadata.py
    # healthsheet_page() is defined in tabs/healthsheet.py
    # data_pre_processing_page() is defined in tabs/data_pre_processing.py
    # ai_readiness_page() is defined in tabs/ai_readiness.py
    # if 'current_tab' not in st.session_state:
    #     st.session_state['current_tab'] = 'Study Metadata'
    # if 'scroll_to' not in st.session_state:
    #     st.session_state['scroll_to'] = None
    
    tab_functions = {
        "Overview": overview_page,
        "Collection Methods": collection_methods_page,
        "Data Governance": data_governance_page,
        "Study Dashboard": study_dashboard_page,
        "Study Metadata": study_metadata_page,
        "Healthsheet": healthsheet_page,
        "Data Pre-Processing": data_pre_processing_page,
        "AI-Readiness": ai_readiness_page,
    }
    
    # Set page configuration
    config_page(version)
    # Create tabs
    create_tabs(tab_functions)

if __name__ == "__main__":
    main()