import streamlit as st
import pandas as pd
import plotly.express as px
import json

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

def create_pie_chart(names, values, title, height=400, colors = px.colors.qualitative.Set1, legend_props={'y': -0.3, 'entry_width': 0.5, 'font_size': 11}):  
    fig = px.pie(
        names=names, values=values,
        category_orders={'names': names}, 
        color_discrete_sequence=colors,
        hole=0.5) # donut chart
    
    title_setting = {
            'text': title,
            'font': {
                'size': 14,
                'color': 'black',
                'family': 'Times New Roman'
            },
            'x': 0,
            # 'y': 0.98,
            'y': 0.99,
            'xanchor': 'left',
            'yanchor': 'top',
        }  

    fig.update_layout(
        autosize=True,
        showlegend=True,
        paper_bgcolor='white',
        plot_bgcolor='white', 
        margin=dict(l=0, r=0, t=25, b=0),
        height=height,
        title=title_setting,
        legend=dict(
            x=0, 
            y=legend_props['y'],
            xanchor='left',
            yanchor='bottom',
            orientation='h',
            traceorder='normal', 
            font=dict(size=legend_props['font_size'], color="black",family='Times New Roman', lineposition='none'),
            itemwidth=30,
            itemsizing='trace',
            valign='top',
            entrywidthmode='fraction',
            entrywidth=legend_props['entry_width'],
            indentation= -5,
            tracegroupgap=0
        )
    )

    fig.update_traces(
        marker=dict(line=dict(color='black', width=0.5)),
        textposition="inside",
        textfont=dict(size=14, color='black'),
        texttemplate="%{percent:.2%}<br>(%{value})",
        hovertemplate="%{label}<br>%{percent:.2%} (%{value})",
        domain=dict(x=[0, 1], y=[0, 1]),
        hoverlabel=dict(
            font_size=14,
            font_color='black'
        )
    )
    
    return fig   

def get_asis_chart_property(text, font_size=10):
    return {
        'title': {
            'text': text,
            'font': {
                'size': font_size,
                'color': 'black',
                'family': 'Times New Roman'
            }
        },
        'tickfont': {
            'size': font_size,
            'color': 'black',
            'family': 'Times New Roman'
        },
        'showgrid': True,
        'gridcolor': 'lightgray',
    }

def create_bar_chart(names, values, title, orientation='v', height=400, colors = px.colors.qualitative.Set1):
    fig = px.bar(
        x=values, 
        y=names, 
        orientation=f"{orientation}",
        color_discrete_sequence=colors)
   
    fig.update_layout(
        xaxis=get_asis_chart_property('Number of Participants'),
        yaxis=get_asis_chart_property('Age Groups'),
        autosize=True,
        showlegend=True,
        paper_bgcolor='white',
        plot_bgcolor='white',
        height=height,
        margin=dict(l=0, r=5, t=25, b=5),
        title={
            'text': title,
            'font': {
                'size': 14,
                'color': 'black',
                'family': 'Times New Roman'
            },
            'x': 0,
            'y': 0.98,
            'xanchor': 'left',
            'yanchor': 'top',
        }
    )
    fig.update_traces(
        marker=dict(line=dict(color='black', width=0.5)),
        textfont=dict(size=14, color='black'), 
        texttemplate="%{x}",
        hovertemplate="%{y}: %{x}",
        hoverlabel=dict(
            font_size=14,
            font_color='black'
        )
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

def create_plots(data, plots, cols_per_row=4):
    num_plots = len(plots)
    rows = (num_plots + cols_per_row - 1) // cols_per_row  # Calculate number of rows needed
    chart_height = 450  # Height of the charts
    # Set colors for the charts
    colors = px.colors.qualitative.Set2
    for row in range(rows):
        cols = st.columns(cols_per_row, gap="small", vertical_alignment="top")
        for col_index in range(cols_per_row):
            plot_index = row * cols_per_row + col_index
            if plot_index < num_plots:
                plot = plots[plot_index]
                key, title, chart_type, legend_props = plot[:4]
                # Optional name mapping for charts
                name_mapping = plot[4] if len(plot) == 5 else None
        
                if key and title and chart_type:
                    labels, values = get_data(data, key, name_mapping)

                if num_plots <= rows*cols_per_row+col_index:
                    if chart_type is None:
                        cols[col_index].empty()
                    else:
                        if chart_type == 'pie':
                            fig = create_pie_chart(labels, values, title, chart_height, colors, legend_props)
                        elif chart_type == 'horizontal_bar':
                            fig = create_bar_chart(labels, values, title, 'h', chart_height, colors)

                        elif chart_type == 'vertical_bar':
                            fig = create_bar_chart(labels, values, title, chart_height, colors)
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
        ("Total of Questionnaires", total_questionnaire_collected),
        ("Total of Acoustic Tasks", total_acoustic_task_collected),    
        ("Total Hours of Recordings", total_hours_of_recordings)
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
    columns = st.columns([2,2,1])
    # Define columns for questionnaires and acoustic tasks
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

    for index, (key, title) in enumerate(collected_data):
        names, values = get_data(data, key)
        df = pd.DataFrame({"name": names, "value": values})
        with columns[index]:
            st.dataframe(df,column_config = column_configs[key], hide_index=True)

def study_dashboard_page(tab_name):
    data = load_data()
    if not data:
        st.write("No data available")
        return
    
    # Demographic plots
    # params: key, title, chart_type, legend_props, name_mapping
    # key: key in the JSON object
    # title: title of the chart
    # chart_type: type of the chart (pie, horizontal_bar, vertical_bar, table)
    # legend_props: properties for the legend
    demographic_plots = [
        ('control', 'Control vs. Non-Control', 'pie', {'y': -0.26, 'entry_width': 1, 'font_size': 11}, {'Yes': 'Control', 'No': 'Non-Control'}),
        ('gender_identity', 'Gender Identity', 'pie', {'y': -0.26, 'entry_width': 0.5, 'font_size': 11}, {'Non-binary or genderqueer gender identity': 'Non-binary/genderqueer gender identity'}),
        ('sexual_orientation', 'Sexual Orientation', 'pie', {'y': -0.26, 'entry_width': 0.33, 'font_size': 11}),
        ('race', 'Race', 'pie', {'y': -0.26, 'entry_width': 0.5, 'font_size': 11}, {'American Indian or Alaska Native': 'American Indian/Alaska Native', 'Native Hawaiian or other Pacific Islander': 'Native Hawaiian/other Pacific Islander', 'Canadian Indigenous or Aboriginal': 'Canadian Indigenous/Aboriginal'}),
        ('ethnicity', 'Ethnicity', 'pie', {'y': -0.26, 'entry_width': 1, 'font_size': 11}),
        ('primary_language', 'Primary Language', 'pie', {'y': -0.26, 'entry_width': 1, 'font_size': 11}),
        ('age_groups','Age', 'horizontal_bar', None, {'90 and above': '90 and<br>above'})
    ]                     

    # Disorder plots
    # params: key, title, chart_type, legend_props, name_mapping
    # key: key in the JSON object
    # title: title of the chart
    # chart_type: type of the chart (pie, horizontal_bar, vertical_bar, table)
    # legend_props: properties for the legend
    disorder_plots = [
        ('disorder_types', 'Disorder Types', 'pie', {'y': -0.3, 'entry_width': 0.45, 'font_size': 11}, {'Neurological and Neurodegenerative Disorders': 'Neurological and Neurodegenerative<br>Disorders'}),
        ('voice_disorders_category', 'Voice Disorder', 'pie', {'y': -0.3, 'entry_width': 0.5, 'font_size': 11}, {'Lesions of the vocal cord (nodule, polyp, cyst)': 'Lesions of the vocal cord','Spasmodic Dysphonia / Laryngeal Tremor': 'Spasmodic Dysphonia/Laryngeal Tremor'}),
        ('neurological_and_neurodegenerative_disorders_category', 'Neurological and Neurodegenerative Disorder', 'pie', {'y': -0.3, 'entry_width': 1, 'font_size': 11}),
        ('mood_and_psychiatric_disorders_category', 'Mood and Psychiatric Disorder', 'pie', {'y': -0.63, 'entry_width': 0.5, 'font_size': 10}, {'Attention-Deficit / Hyperactivity Disorder (ADHD)': 'Attention-Deficit/Hyperactivity Disorder', 'Insomnia / Sleep Disorder': 'Insomnia/Sleep Disorder'}),
        ('respiratory_disorders_category', 'Respiratory Disorder', 'pie', {'y': -0.3, 'entry_width': 0.5, 'font_size': 11}, {'Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)': 'Airway Stenosis'}),
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
    # Create the demographic plots
    # params: data, plots, cols_per_row
    create_plots(data, demographic_plots, 3)
    
    # Disorders Section
    st.subheader("Disorder Breakdown")
    # Create the disorder plots
    # params: data, plots, cols_per_row
    create_plots(data, disorder_plots, 3)

    # Data Collection Section
    st.subheader("Data Collection")
    data_collection_section(data, collected_data)