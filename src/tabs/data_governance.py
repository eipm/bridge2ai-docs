import streamlit as st

def data_governance_page(tab_name):
    st.header("Accessing the Dataset")
    st.markdown("""
    The feature-only and raw audio datasets are available under distinct agreements appropriate for the sensitivity of their respective content.
    * Registered Access (features-only data):
        * Register on PhysioNet and confirm your identity ([Registered Access License](https://physionet.org/about/duas/bridge2ai-voice-registered-access-agreement/)).
        * Sign the Bridge2AI-Voice Registered Access Agreement, which outlines the terms and conditions for data use
    * Controlled Access (raw audio data):
        * Complete the Data Access Request Form (DARF)
        * Complete the Data Use Agreement (DUA)
        * Submit your application to the Data Access Compliance Office for review

    Upon approval, ensure a Data Use and Transfer Agreement (DTUA) is signed by an authorized official at your institution
    """)
    
    st.subheader("Memorandum: Ethical Justification for Controlled Access to Raw Voice Data Samples")

    st.markdown("""Click the button below to download a copy of the memorandum explaining the reasoning behind the governance structur.""")

    try:
        with open("docs/v1.0-Memorandum on Raw Voice Data Samples.pdf", "rb") as pdf_file:
            pdf_data = pdf_file.read()
        
        st.download_button(
            label="Download - Memorandum PDF",
            type="primary",
            help="Download the Memorandum on Raw Voice Data Samples",
            icon=":material/download:",
            data=pdf_data,
            file_name="v1.0-Memorandum on Raw Voice Data Samples.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.error("PDF file not found. Please check the file path.")
    
    st.header("Oversight")

    with st.expander('''**Has the clinical study been reviewed and approved by at least one human subjects’ protection review board?**''', expanded=False):
        st.write('''Submitted, approved by USF Single IRB and subsites IRB through the Single IRB Process''')

    with st.expander('''**Is this clinical study for a drug product?**''', expanded=False):
        st.write('''No''')

    with st.expander('''**Is this clinical study for a medical device?**''', expanded=False):
        st.write('''No''')
    
    with st.expander('''**Was a data monitoring committee appointed for this study?**''', expanded=False):
        st.write('''No''')

    st.header("De-Identification Levels")

    st.write("""Level of de-identification from this dataset Identifiable information (under HIPAA and under the Common Rule) as well as data considered as sensitive have been removed from this dataset.""", unsafe_allow_html=False)

    with st.expander('''**Does this dataset remove direct identifiers?**''', expanded=False):
        st.write('''Yes''')

    with st.expander('''**Does this dataset apply the HIPAA de-identification rules?**''', expanded=False):
        st.write('''Yes''')

    with st.expander('''**Does this dataset rebase and/or replace dates by integers?**''', expanded=False):
        st.write('''Yes''')

    with st.expander('''**Does this dataset remove narrative text fields?**''', expanded=False):
        st.write('''Yes''')

    with st.expander('''**Does this dataset achieve K-anonymization (k>=2)?**''', expanded=False):
        st.write('''No''')

    st.subheader("De-identification Details")

    st.write("""All direct identifiers were removed, as these would reveal the identity of the research participant. These include name, civic address, and social security numbers. Indirect identifiers were removed where these created a significant risk of causing participant re-identification, for example through their combination with other public data available on social media, in government registries, or elsewhere. These include select geographic or demographic identifiers, as well as some information about household composition or cultural identity. Non-identifying elements of data that revealed highly sensitive information, such as information about household income, mental health status, traumatic life experiences, and the like were also removed. All raw voice data was removed, as this data has the potential to cause to individual re-identification or to be used for illicit or unauthorized purposes.  """, unsafe_allow_html=False)

    st.header("Consent")

    st.subheader("Consent Type", divider="violet")

    with st.expander('''**Does this dataset allow only the non-commercial use of the data?**''', expanded=False):
        st.write('''No''')

    with st.expander('''**Does this dataset allow only the use of the data in a specific geographic location?**''', expanded=False):
        st.write('''No''')

    with st.expander('''**Does this dataset allow only the use of the data for a specific type of research?**''', expanded=False):
        st.write('''No''')

    with st.expander('''**Does this dataset allow only the use of the data for genetic research?**''', expanded=False):
        st.write('''No''')

    with st.expander('''**Does this dataset allow only the use of the data for research that does not involve the development of methods or algorithms?**''', expanded=False):
        st.write('''No''')

    st.subheader("Consent Details", divider="violet")

    st.write("""Research data that does not contain your direct identifiers will be shared with external researchers for future research through a secure database. Data that poses a low risk of causing individual re-identification will be shared in registered access with the general public. Data that would pose a heightened risk of re-identification if shared in full open access will be shared through a controlled access mechanism with authorized researchers.""", unsafe_allow_html=False)        
