import streamlit as st
from tabs.utils import create_html_table

def show_table(key, button_text, show_table, csv_file_path, caption):
    # Initialize session state for table visibility
    show_table_prop = f'{show_table}_{key}'
    
    if  show_table_prop not in st.session_state:
        st.session_state[show_table_prop] = False
   
    if st.button(button_text, key):
        st.session_state[show_table_prop] = not st.session_state[show_table_prop]

    # Conditionally display the table
    if st.session_state[show_table_prop]:
        create_html_table(csv_file_path, caption, [], 0)

# Define the content of the Study Metadata page
def study_metadata_page(tab_name):
    
    st.markdown(
    """
    Official Title:  Bridge2AI-Voice

    Design: Study Type - Observational
    
    Enrollment Count (Anticipated by 2027): 10,000
    
    Design Observation Model
    - Cohort
    
    Design Time Perspective
    - Cross-sectional
    
    Biospecimens: Respiratory, Voice and speech samples
    
    Biospecimens Description<br>
    The Bridge2AI-Voice dataset contains samples from conventional acoustic tasks including respiratory sounds, cough sounds, and free speech prompts, capturing voice, speech and language data relating to health. Participants who consent are asked to perform speaking tasks and complete self-reported demographic and medical history questionnaires, as well as disease-specific validated questionnaires. Participants who consent also permit investigators to access medical information through EHR platforms in order to perform gold standard validation of diagnoses and symptoms  
    
    <ins>Eligibility</ins>

    Sex<br>
    All

    Gender Based<br>
    No

    Minimum Age<br>
    2 - 17 for pediatric participants and 18+ for adult cohorts.

    Maximum Age<br>
    120 years 

    Healthy Volunteers<br>
    Yes 

    Inclusion Criteria<br>""", unsafe_allow_html=True)

    show_table(1, 'See Collection Methods - Table 1', 'show_table_1', "tables/Disease_cohort_inclusion_exclusion_criteria.csv", 'Table 1 - Disease cohort inclusion/exclusion criteria and validation methods')

    st.markdown(
    """
    Exclusion Criteria<br>
    Does not read or speak English (Please note, the Spanish protocols and Data collection will be included in future releases)<br>""", unsafe_allow_html=True)

    show_table(2, 'See Collection Methods - Table 1', 'show_table_1', "tables/Disease_cohort_inclusion_exclusion_criteria.csv", 'Table 1 - Disease cohort inclusion/exclusion criteria and validation methods')
    
    st.markdown(
    """
    Study Population<br>
    The current v.2.0.0 dataset contains only adult populations. As the study progresses, a pediatric cohort will be introduced. Inclusion/exclusion criteria and additional information regarding the dataset and study metadata will be updated at that time. In addition, the current dataset contains fluent English speakers but will expand to include data collection in Spanish.

    Sampling Method<br>
    Non-Probability Sample<br>
    Identification Information<br>
    Organization Study ID<br>
    OT2OD032720<br>
    
    Organization Study Type<br>
    U.S. National Institutes of Health (NIH) Grant/Contract Award Number
    
    Secondary ID<br>
    <table style="border: none;">
    <tr>
    <td><b>ID</b></td>
    <td><b>Link</b></td>
    </tr>
    <tr>
    <td>OT2OD032720</td>
    <td><a href="https://reporter.nih.gov/search/4XtcXzBGEkWQlwG5v8odBA/project-details/10858564">https://reporter.nih.gov/search/4XtcXzBGEkWQlwG5v8odBA/project-details/10858564</a></td>
    </tr>
    </table>
    
    Collaborators 
    - University of South Florida 
    - Weill Cornell Medicine 
    - Oregon Health & Science University
    - Massachusetts Institute of Technology 
    - University of Toronto 
    - Mount Sinai Hospital
    - Hospital for Sick Children
    - Simon Fraser University 
    - The Hastings Center 
    - Washington University in St. Louis 
    - University of Florida
    - Vanderbilt University Medical Center

    URL 
    How to cite
    If you use this dataset for any purpose, please cite the resources specified in the Bridge2AI-Voice documentation for version 2.0.0 of the dataset at (URL)
    
    Bridge2AI-Voice Consortium (2024). Flagship Voice Dataset from the Bridge2AI-Voice Project (2.0.0) [Dataset]. 

    Contact
    For any questions, suggestions, or feedback related to this dataset, please email info@b2ai-voice.org
    
    Acknowledgement
    Bridge2AI-Voice is supported by NIH grant OT2OD032720 through the NIH Bridge2AI Common Fund program.
    """, unsafe_allow_html=True)
    
