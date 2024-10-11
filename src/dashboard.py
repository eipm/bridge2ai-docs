import streamlit as st
import pandas as pd
import plotly.express as px
import json

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

def load_data():
    # Read the JSON object from the file
    with open('data/dashboard_data.json', 'r') as json_file:
        data = json.load(json_file)
    return data

def get_data(json_data, tag, name_mapping=None):
    data = json_data.get(tag)
    names = list(data.keys())
    values = list(data.values())
    if name_mapping:
        new_names = [name_mapping.get(name, name) for name in names]
        return new_names, values
    return names, values

def get_chart_title_poperty():
    return {
            'font': {
                'size': 24,
                'family': 'Arial',
                'color': 'black'
            },
            'pad': {
                't': 10,
                'b': 10,
                'l': 20,
                'r': 10
            }
        }

def get_chart_legend_property():
    return {
            'font': {
                'size': 14,
                'color': 'black'
            },
            'title': {
                'font': {
                    'size': 16,
                    'color': 'black'
                }
            },
            'traceorder': 'normal',
            'x': 1,
            'y': 1,
            'xanchor': 'left',
            'yanchor': 'top',
            'valign': 'top',
            'orientation': 'v',
            'bordercolor': 'black',
            'borderwidth': 1,
            'itemwidth': 30,
            'tracegroupgap': 5
        }


def plot_pie_chart(names, values, title):    
    fig = px.pie(names=names, values=values, title=title, category_orders={'names': list(names)}, color_discrete_sequence=px.colors.qualitative.Set2) 
    fig.update_layout(
        title=get_chart_title_poperty(),
        autosize=True,
        showlegend=True,
        legend=get_chart_legend_property(),
        height=680,
        font=dict(
            size=16,
            color='black',
        ),
        paper_bgcolor='white',
        plot_bgcolor='white', 
        margin=dict(l=100, r=100, t=100, b=100)
    )

    fig.update_traces(
        marker=dict(line=dict(color='black', width=0.5)),
        textposition="outside",
        texttemplate="%{percent:.2%} (%{value})",
        hovertemplate="%{label}<br>%{percent:.2%} (%{value})",
        hoverlabel=dict(
            font_size=14,
            font_family="Arial"
        )
    )    
    st.plotly_chart(fig)
    
def get_asis_chart_property(text):
    return {
        'title': {
            'text': text,
            'font': {'size': 18, 'color': 'black'}
        },
        'tickfont': {'size': 14, 'color': 'black'},
        'showgrid': True,
        'gridcolor': 'lightgray',
    }

def plot_bar_chart(names, values, title, orientation='v'):
    fig = px.bar(x=values, y=names, orientation=f"{orientation}", title=title, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(
        title=get_chart_title_poperty(),
        xaxis=get_asis_chart_property('Number of Participants'),
        yaxis=get_asis_chart_property('Age Groups'),
        autosize=True,
        showlegend=True,
        legend=get_chart_legend_property(),
        height=680,  
        font=dict(
            size=16, 
            color='black',
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=100, r=100, t=100, b=100)
    )
    fig.update_traces(
        marker=dict(line=dict(color='black', width=0.5)), 
        texttemplate="%{x}",
        hovertemplate="%{y}: %{x}",
        hoverlabel=dict(
            font_size=14,
            font_family="Arial"
        )   
    )
    st.plotly_chart(fig)

def display_table(names, values, title, display_percentage_column=False):
    df = pd.DataFrame({"name": names, "value": values})
    custom_column_config= {
        "name": st.column_config.TextColumn(
            "Name",
            width="large"),
        "value": st.column_config.TextColumn(
            "Count",
            width="medium")
    }
    
    if display_percentage_column:
        total = df['value'].sum()
        df['percentage'] = (df['value'] / total) * 100
        df['percentage'] = df['percentage'].map(lambda x: f"{x:.2f}%")
        
        custom_column_config["percentage"] = st.column_config.Column(
            "Percentage",
            width="medium"
        )
            
    st.write(f"### {title}")
    st.dataframe(
        df,
        column_config = custom_column_config,
        hide_index=True
    )

def create_tabs(tabs_func):
    tab_names = list(tabs_func.keys())
    tabs = st.tabs(tab_names)
    for tab, name in zip(tabs, tab_names):
        with tab:
            tabs_func[name](name)

def plot_view(data, plots):
    for plot in plots:
        key, title, chart_type = plot[:3]
        name_mapping = plot[3] if len(plot) == 4 else None
        names, values = get_data(data, key, name_mapping)
        if chart_type == 'pie':
            plot_pie_chart(names, values, title)
        elif chart_type == 'horizontal_bar':
            plot_bar_chart(names, values, title, 'h')
        elif chart_type == 'vertical_bar':
            plot_bar_chart(names, values, title)

def table_view(data, plots):
    for plot in plots:
        key, title, chart_type = plot[:3]
        name_mapping = plot[3] if len(plot) == 4 else None
        names, values = get_data(data, key, name_mapping)
        display_table(names, values, title, chart_type == 'pie')
        
def study_dashboard_page(tab_name):
    data = load_data()
    if not data:
        st.write("No data available")
        return
    
    number_of_participants = data.get('number_of_participants')
    number_of_recordings = data.get('number_of_recordings')
    total_hours_of_recordings = data.get('total_hours_of_recordings')
    if isinstance(total_hours_of_recordings, float):
        total_hours_of_recordings = round(total_hours_of_recordings, 2)
    
    # Create a 3-column layout for the metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Number of Participants", number_of_participants)
    col2.metric("Number of Recordings", number_of_recordings)
    col3.metric("Total Hours of Recordings", total_hours_of_recordings)

    # Define plots to be displayed
    plots = [
        ('control', 'Control vs. Non-Control Participants', 'pie', {'Yes': 'Control', 'No': 'Non-Control'}),
        ('gender_identity', 'Gender Identity of Participants', 'pie'),
        ('sexual_orientation', 'Sexual Orientation of Participants', 'pie'),
        ('race', 'Race of Participants', 'pie'),
        ('ethnicity', 'Ethnicity of Participants', 'pie'),
        ('age_groups','Age Breakdown of Participants', 'horizontal_bar'),
        ('primary_language', 'Primary Language of Participants', 'pie'),
        ('disorder_types', 'Disorder Types', 'pie'),
        ('voice_disorders_category', 'Voice Disorder Breakdown', 'pie'),
        ('neurological_and_neurodegenerative_disorders_category', 'Neurological and Neurodegenerative Disorder Breakdown', 'pie'),
        ('mood_and_psychiatric_disorders_category', 'Mood and Psychiatric Disorder Breakdown', 'pie'),
        ('respiratory_disorders_category', 'Respiratory Disorder Breakdown', 'pie'),
        ('questionnaire_collected', 'Questionnaire Collection Breakdown', 'pie'),
        ('acoustic_task_collected', 'Acoustic Task Collection Breakdown', 'pie')
    ]

    on = st.toggle("📊 Chart View", True)
    if on:
        plot_view(data, plots)
    else:
        table_view(data, plots)

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

def main():  
    # Define the version variable
    version = "0.5.0"
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