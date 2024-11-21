import streamlit as st
from tabs.utils import coming_soon_message
from tabs.utils import create_html_table

# Define the content of the Study Metadata page
def study_metadata_page(tab_name):
    st.markdown(
    """
    Official Title:  Bridge2AI-Voice 

Design: Study Type - Observational 
 
Enrollment Count (Anticipated by 2027):   10,000 
 
Design Observation Model   
•	Cohort  
 
Design Time Perspective   
•	Cross-sectional  
 
Biospecimens:  Respiratory, Voice and speech samples 
 
Biospecimens Description   
The Bridge2AI-Voice dataset contains samples from conventional acoustic tasks including respiratory sounds, cough sounds, and free speech prompts, capturing voice, speech and language data relating to health. Participants who consent are asked to perform speaking tasks and complete self-reported demographic and medical history questionnaires, as well as disease-specific validated questionnaires. Participants who consent also permit investigators to access medical information through EHR platforms in order to perform gold standard validation of diagnoses and symptoms  
 
Eligibility  

Sex  
All  

Gender Based  
No  

Minimum Age  
18 years (this will change when pediatric cohort is introduced, and metadata will be updated to reflect new eligibility criteria) 

Maximum Age  
120 years 

Healthy Volunteers  
Yes 

Inclusion Criteria  
See Table 1

Exclusion Criteria   
Does not read or speak English (Please note, the Spanish protocols and Data collection will be included in future releases)
See Table 1
 
Study Population  
The current v.1.0.0 dataset contains only adult populations. As the study progresses, a pediatric cohort will be introduced. Inclusion/exclusion criteria and additional information regarding the dataset and study metadata will be updated at that time. In addition, the current dataset contains fluent English speakers but will expand to include data collection in Spanish.
  
Sampling Method  
Non-Probability Sample  
Identification Information 
Organization Study ID  
OT2OD032720 
 
Organization Study Type   
U.S. National Institutes of Health (NIH) Grant/Contract Award Number  
 
Secondary ID  
ID  	Link  
OT2OD032720 
 	https://reporter.nih.gov/search/4XtcXzBGEkWQlwG5v8odBA/project-details/10858564 

 
   
Collaborators   
•	University of South Florida 
•	Weill Cornell Medicine 
•	Oregon Health & Science University  
•	Massachusetts Institute of Technology 
•	University of Toronto 
•	Mount Sinai Hospital
•	Hospital for Sick Children
•	Simon Fraser University 
•	The Hastings Center 
•	Washington University in St. Louis 
•	University of Florida
•	Vanderbilt University Medical Center

  
URL 
How to cite  
If you use this dataset for any purpose, please cite the resources specified in the Bridge2AI-Voice documentation for version 1.0.0 of the dataset at (URL)  
 
Bridge2AI-Voice Consortium (2024). Flagship Voice Dataset from the Bridge2AI-Voice Project (1.0.0) [Dataset].   

Contact  
For any questions, suggestions, or feedback related to this dataset, please email info@b2ai-voice.org
 
Acknowledgement  
Bridge2AI-Voice is supported by NIH grant OT2OD032720 through the NIH Bridge2AI Common Fund program.
""")

    # Initialize session state for table visibility
    if 'show_table_1' not in st.session_state:
        st.session_state['show_table_1'] = False
    if 'show_table_2' not in st.session_state:
        st.session_state['show_table_2'] = False
    if 'show_table_3' not in st.session_state:
        st.session_state['show_table_3'] = False

        # Button to toggle table visibility
    if st.button('Table 1'):
        st.session_state['show_table_1'] = not st.session_state['show_table_1']

    # Conditionally display the table
    if st.session_state['show_table_1']:
        csv_file_path = "tables/Disease_cohort_inclusion_exclusion_criteria.csv"
        caption = 'Table 1 - Disease cohort inclusion/exclusion criteria and validation methods'
        create_html_table(csv_file_path, caption, [], 0)

    # Button to toggle table visibility
    if st.button('Table 2'):
        st.session_state['show_table_2'] = not st.session_state['show_table_2']

    # Conditionally display the table
    if st.session_state['show_table_2']:
        csv_file_path = "tables/Acoustic_Tasks_Protocol.csv"
        caption = 'Table 2 - Acoustic Tasks in Protocol'
        create_html_table(csv_file_path, caption)

    # Button to toggle table visibility
    if st.button('Table 3'):
        st.session_state['show_table_3'] = not st.session_state['show_table_3']

    # Conditionally display the table
    if st.session_state['show_table_3']:
        csv_file_path = "tables/Validated_Questionnaires.csv"
        caption = 'Table 3 - Validated Questionnaires integrated into App'
        create_html_table(csv_file_path, caption, ['X'])