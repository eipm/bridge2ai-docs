import streamlit as st
import os
import streamlit.components.v1 as components

def dataset_structure_preview_page(tab_name):
    st.title(f"{tab_name}")

    # Define the path to the HTML file
    html_file_path = os.path.join(os.path.dirname(__file__), '../bids-like_structure_preview.html')

    # Check if the HTML file exists
    if os.path.exists(html_file_path):
        # Read the HTML file content
        with open(html_file_path, 'r', encoding='utf-8') as file:
            b2aipreview = file.read()

        # Display the HTML content in a scrollable iframe
        components.html(b2aipreview, height=600, scrolling=True)
    else:
        st.error("Failed to load dataset structure preview. The HTML file was not found.")
