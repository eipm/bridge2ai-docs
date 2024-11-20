import streamlit as st
import pandas as pd

# All tab pages are defined below
def coming_soon_message(tab_name):
    st.title('Bridge2AI Voice Dashboard')
    st.write(f"{tab_name} - Coming soon!")

    image_path = "images/Wave.png"
    st.image(image_path, caption='', use_container_width=True)

def create_html_table(csv_file_path, caption=None):
       # Read CSV file
    df = pd.read_csv(csv_file_path, dtype=str)  # Ensure all columns are read as strings

    # Replace NaN with an empty string;
    df = df.fillna("")
    
    # Convert DataFrame to HTML table
    html_table = df.to_html(index=False, classes='table table-striped')
    
    if caption is not None:
        html_table_with_caption = f"""
        <table class="table table-striped">
            <caption style="caption-side: top; text-align: left; font-weight: bold; font-size: 1.2em;">
                {caption}
            </caption>
            {html_table}
        </table>
        """
    else:
        html_table_with_caption = f"""
        <table class="table table-striped">
            {html_table}
        </table>
        """

    # Add CSS for table styling
    st.markdown(
        """
        <style>
        .table {
            width: 100%;
            border-collapse: collapse;
        }
        .table th, .table td {
            border: 1px solid !important;
            padding: 4px !important;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display HTML table
    st.markdown(html_table_with_caption, unsafe_allow_html=True)
