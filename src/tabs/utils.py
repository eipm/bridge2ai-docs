import streamlit as st
import pandas as pd
import os
import json

# All tab pages are defined below
def coming_soon_message(tab_name):
    st.title('Bridge2AI Voice Dashboard')
    st.write(f"{tab_name} - Coming soon!")

    image_path = "images/Wave.png"
    st.image(image_path, caption='', use_container_width=True)

def create_html_table(csv_file_path, caption=None, cell_values=[], column_index=-1):
    # Read CSV file
    df = pd.read_csv(csv_file_path, dtype=str)  # Ensure all columns are read as strings

    # Replace NaN with an empty string;
    df = df.fillna("")

    bold_cells = df.iloc[:, column_index].tolist() if column_index >= 0 else []

    # Convert DataFrame to HTML table
    html_table = df.to_html(index=False, classes='table table-striped')

    if bold_cells and len(bold_cells) > 0:
        for bold_cell in bold_cells:
            html_table = html_table.replace(f'<td>{bold_cell}</td>', f'<td class="bold-cell">{bold_cell}</td>')

    if cell_values and len(cell_values) > 0:
        for cell_value in cell_values:
            html_table = html_table.replace(f'<td>{cell_value}</td>', f'<td class="center-align">{cell_value}</td>')

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
        
        .table th {
            background-color: #f2f2f2;
        }
        
        .table .center-align {
            text-align: center; /* Center alignment for specific columns */
        }
        
        .table .bold-cell {
            font-weight: bold; /* Bold font for first column cells */
        }
        
        @media (prefers-color-scheme: dark) {
            .table th {
                color: #000000;
                background-color: darkgrey;
                border-color: #ffffff !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display HTML table
    st.markdown(html_table_with_caption, unsafe_allow_html=True)
    
def load_data():
    # Read the JSON object from the file
    docs_data_path = os.getenv('DOCS_DATA_PATH')
    file_path = 'dashboard_data.json'
    if docs_data_path is not None:
        file_path = os.path.join(docs_data_path, file_path)
    
    # Check if the file path is valid and the file exists
    if not os.path.isfile(file_path):
        st.warning(f"The file at path {file_path} does not exist. Data is unavailable.")
        return {}
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data