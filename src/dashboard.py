import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

def coming_soon_message(tab_name):
    # Your Streamlit application code
    st.title('Bridge2AI Voice Dashboard')
    st.write(f"{tab_name} - Coming soon!")

    # Add an image to the page
    image_path = "images/Wave.png"
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

def create_pie_chart(names, values, title, height=250, colors = px.colors.qualitative.Set1):  
    fig = px.pie(
        names=names, values=values,
        category_orders={'names': list(names)}, 
        color_discrete_sequence=colors,
        hole=0.5) # donut chart
    
    title_setting = {
            'text': title,
            'font': {
                'size': 12,
                'color': 'black'
            },
            'x': 0,
            'y': 0.98,
            'xanchor': 'left',
            'yanchor': 'top',
        }  
    
    if "<br>" in title:
        title_setting['y'] = 0.95
        
    fig.update_layout(
        autosize=True,
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='white', 
        #margin=dict(l=5, r=5, t=5, b=5),
        margin=dict(l=20, r=20, t=20, b=20),
        height=height,
        title=title_setting,
    )

    fig.update_traces(
        marker=dict(line=dict(color='black', width=0.5)),
        textposition="inside",
        textfont=dict(size=12, color='black'),
        texttemplate="%{percent:.2%}<br>(%{value})",
        #texttemplate="%{percent:.2%}",
        hovertemplate="%{label}<br>%{percent:.2%} (%{value})<extra></extra>",
        domain=dict(x=[0, 1], y=[0, 1])
    )
    
    return fig
    
def get_asis_chart_property(text):
    return {
        'title': {
            'text': text,
            'font': {
                'size': 10,
                'color': 'black'
            }
        },
        'tickfont': {
            'size': 10,
            'color': 'black'
        },
        'showgrid': True,
        'gridcolor': 'lightgray',
    }

def create_bar_chart(names, values, title, orientation='v', height=250, colors = px.colors.qualitative.Set1):
    fig = px.bar(
        x=values, 
        y=names, 
        orientation=f"{orientation}",
        color_discrete_sequence=colors)
   
    fig.update_layout(
        xaxis=get_asis_chart_property('Number of Participants'),
        yaxis=get_asis_chart_property('Age Groups'),
        autosize=True,
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='white',
        height=height,
        margin=dict(l=0, r=5, t=25, b=5),
        title={
            'text': title,
            'font': {
                'size': 12,
                'color': 'black'
            },
            'x': 0,
            'y': 0.98,
            'xanchor': 'left',
            'yanchor': 'top',
        }
    )
    fig.update_traces(
        marker=dict(line=dict(color='black', width=0.5)), 
        texttemplate="%{x}",
        hovertemplate="%{y}: %{x}",
    )
    
    return fig

def create_table_chart(names, values, title, headers=('Name', 'Count'), height=250):
    fig = go.Figure(data=[go.Table(
        columnwidth=[3, 1],
        header=dict(
             values=[f"<b>{header}</b>" for header in headers],
            align='left',
            font=dict(size=12, color='black'),
            fill=dict(color='#f2f2f2'),
            line=dict(color='black', width=1)
        ),
        cells=dict(
            values=[names, values],
            align='left',
            font=dict(size=12, color='black'),
            fill=dict(color='white'),
            line=dict(color='black', width=1),
            height=30
        )
    )])
    
    fig.update_layout(
        margin=dict(l=5, r=5, t=25, b=5),
        height=height,
        width=400,
        paper_bgcolor='white',
        plot_bgcolor='white',
        annotations=[
            dict(
                text=title,
                x=0,
                y=1.120,
                xref='paper',
                yref='paper',
                showarrow=False,
                font=dict(size=12, color='black', weight='bold'),
                xanchor='left',
                yanchor='top'
            )
        ]
       
    )
    
    return fig

def getPlotlyConfig():
    return {
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': [
            'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 
            'autoScale2d', 'resetScale2d'
        ]
    }

def create_plots(data, plots, cols_per_row=6):
    num_plots = len(plots)
    rows = (num_plots + cols_per_row - 1) // cols_per_row  # Calculate number of rows needed
    chart_height = 250  # Height of the charts
    # Set colors for the charts
    colors = px.colors.qualitative.Set2
    for row in range(rows):
        cols = st.columns(cols_per_row, gap="small", vertical_alignment="top")
        for col_index in range(cols_per_row):
            plot_index = row * cols_per_row + col_index
            if plot_index < num_plots:
                plot = plots[plot_index]
                key, title, chart_type = plot[:3]
                # Optional name mapping for charts
                name_mapping = plot[3] if len(plot) == 4 else None
        
                if key and title and chart_type:
                    labels, values = get_data(data, key, name_mapping)
                else:
                    labels, values = None, None

                if num_plots <= rows*cols_per_row+col_index:
                    if chart_type is None:
                        cols[col_index].empty()
                    else:
                        if chart_type == 'pie':
                            fig = create_pie_chart(labels, values, title, chart_height, colors)
                        elif chart_type == 'horizontal_bar':
                            wrapped_labels = [name.replace('90 and above', '90 and<br>above') for name in labels]
                            fig = create_bar_chart(wrapped_labels, values, title, 'h', chart_height, colors)
                        elif chart_type == 'vertical_bar':
                            fig = create_bar_chart(labels, values, title, chart_height, colors)
                        elif chart_type == 'table':
                            fig = create_table_chart(labels, values, title, chart_height)

                        cols[col_index].plotly_chart(fig, use_container_width=True, config=getPlotlyConfig())
                else:
                    cols[col_index].empty()
        
def overview_section(data):
    number_of_participants = data.get('number_of_participants')
    number_of_recordings = data.get('number_of_recordings')
    total_hours_of_recordings = data.get('total_hours_of_recordings')
    total_questionnaire_collected  = pd.json_normalize(data.get('questionnaire_collected')).values.sum()
    total_acoustic_task_collected = pd.json_normalize(data.get('acoustic_task_collected')).values.sum()

    if isinstance(total_hours_of_recordings, float):
        total_hours_of_recordings = round(total_hours_of_recordings, 2)
    
    cards = [
        ("Number of Participants", number_of_participants),
        ("Number of Recordings", number_of_recordings),
        ("Total Hours of Recordings", total_hours_of_recordings),
        ("Total of Questionnaires", total_questionnaire_collected),
        ("Total of Acoustic Tasks", total_acoustic_task_collected)    
    ]
    
    # Create a 5-column layout for the metrics
    columns = st.columns([1, 1, 1, 1, 1])
    for i, col in enumerate(columns):
            name, value = cards[i]
            if name is not None and value is not None:
                col.metric(name, value)
            else:
                col.empty()
                
def data_collection_section(data, collected_data):
    print(data)
    print(collected_data)
    columns = st.columns([2,3])
    
    # Define column configurations for the tables
    column_configs = {
        'questionnaire_collected': {
            "name": st.column_config.TextColumn(
                "Questionnaire",
                width="large"
            ),
            "value": st.column_config.TextColumn(
                "Count",
                width="small"
            )
        },
        'acoustic_task_collected': {
            "name": st.column_config.TextColumn(
                "Acoustic Task",
                width="large"
            ),
            "value": st.column_config.TextColumn(
                "Count",
                width="small"
            )
        }
    }
    
    index = 0   
    for key, title in collected_data:
        names, values = get_data(data, key)
        df = pd.DataFrame({"name": names, "value": values})
        with columns[index]:
            st.dataframe(df,column_config = column_configs[key], hide_index=True)
        index += 1
        
def study_dashboard_page(tab_name):
    data = load_data()
    if not data:
        st.write("No data available")
        return
    
    # Demographic plots
    demographic_plots = [
        ('control', 'Control vs. Non-Control', 'pie', {'Yes': 'Control', 'No': 'Non-Control'}),
        ('gender_identity', 'Gender Identity', 'pie'),
        ('sexual_orientation', 'Sexual Orientation', 'pie'),
        ('race', 'Race', 'pie'),
        ('ethnicity', 'Ethnicity', 'pie'),
        ('primary_language', 'Primary Language', 'pie'),
        ('age_groups','Age', 'horizontal_bar'),
    ]

    # Disorder plots
    disorder_plots = [
        ('disorder_types', 'Disorder Types', 'pie'),
        ('voice_disorders_category', 'Voice Disorder', 'pie'),
        ('neurological_and_neurodegenerative_disorders_category', 'Neurological and Neurodegenerative<br>Disorder', 'pie'),
        ('mood_and_psychiatric_disorders_category', 'Mood and Psychiatric Disorder', 'pie'),
        ('respiratory_disorders_category', 'Respiratory Disorder', 'pie'),
    ]

    # Data collection tables    
    collected_data = [
        ('questionnaire_collected', 'Questionnaire Collection'),
        ('acoustic_task_collected', 'Acoustic Task Collection')
    ]

    # Overview Section
    st.subheader("Overview")
    overview_section(data)
    
    # Demographic Section
    st.subheader("Demographic Breakdown")
    create_plots(data, demographic_plots, 5)
    
    # Disorders Section
    st.subheader("Disorder Breakdown")
    create_plots(data, disorder_plots, 5)

    # Data Collection Section
    st.subheader("Data Collection")
    data_collection_section(data, collected_data)
            
def get_asis_chart_property(text, font_size=10):
    return {
        'title': {
            'text': text,
            'font': {
                'size': font_size,
                'color': 'black'
            }
        },
        'tickfont': {
            'size': font_size,
            'color': 'black'
        },
        'showgrid': True,
        'gridcolor': 'lightgray',
    }

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