import streamlit as st
from tabs.utils import create_html_table

def collection_methods_page(tab_name):

    st.markdown(

        """
        Data is collected across five disease categories. Initial data release contains data collected from four of five categories.

        Participants are recruited across different academic institutions from “high volume expert clinics” based on diagnosis and inclusion/exclusion criteria outlined below **(Table 1)**.

        **Pediatric Participants:** Pediatric Participants are recruited strictly from the Hospital for Sick Children (Sickkids) and are based on different age groups.

        **High Volume Expert Clinics:** Outpatient clinics within hospital systems or academic institutions that have developed an expertise in a specific disease area and see more than 50 patients per month from the same disease category. Ex: Asthma/COPD pulmonary specialty clinic.

        Data is collected in the clinic with the assistance of a trained research assistant. Future data collection will also occur remotely, however remote data collection did not occur with initial dataset being released. Voice samples are collected prospectively using a custom software application (Bridge2AI-Voice app) with the Bridge2AI-Voice protocols.
        
        For Pediatrics, all data is collected using [reproschema-ui](https://repronim.org/reproschema-ui/) with the Bridge2AI-Voice pediatric protocol.

        **Clinical validation:** Clinical validation is performed by qualified physician or practitioner based on established gold standards for diagnosis **(Table 1)**.

        **Acoustic Tasks:** Voice, breathing, cough, and speech data are recorded with the app for adults, and with reproschema-ui for pediatrics. A total of 22 acoustic Tasks are recorded through the app **(Table 2)**.

        **Demographic surveys and confounders:** Detailed demographic data and surveys about confounding factors such as smoking and drinking history is collected through the smartphone application. 

        **Validated Questionnaires:** The Bridge2AI-Voice protocols contain validated tools and questionnaires for each disease category within the app for data collection **(Table 3)**.

        **Other Multimodal Data:** The rest of the multimodal data including imaging, genomic data (for the neuro cohort), laryngoscopy imaging and other EHR data is extracted from different sites independently and will be uploaded through the REDCAP database. Please note that no external data is released in this v2.0.0.

        Please see publication for protocol development description: 
        >Bensoussan, Yael, et al. "Developing Multi-Disorder Voice Protocols: A team science approach involving clinical expertise, bioethics, standards, and DEI." Proc. Interspeech 2024. 2024. [https://www.isca-archive.org/interspeech_2024/bensoussan24_interspeech.html](https://www.isca-archive.org/interspeech_2024/bensoussan24_interspeech.html).

        The supporting REDCap Data Dictionary, Metadata and Instrument PDFs are available at [https://github.com/eipm/bridge2ai-redcap](https://github.com/eipm/bridge2ai-redcap) .

        When using the REDCap Data Dictionary and Metadata please cite:
        
        >Bensoussan, Y., Ghosh, S. S., Rameau, A., Boyer, M., Bahr, R., Watts, S., Rudzicz, F., Bolser, D., Lerner-Ellis, J., Awan, S., Powell, M. E., Belisle-Pipon, J.-C., Ravitsky, V., Johnson, A., Zisimopoulos, P., Tang, J., Sigaras, A., Elemento, O., Dorr, D., … Bridge2AI-Voice. (2024). eipm/bridge2ai-redcap. Zenodo. [https://zenodo.org/doi/10.5281/zenodo.12760724](https://zenodo.org/doi/10.5281/zenodo.12760724).
        

        Protocols can be found in the Bridge2AI-Voice documentation for v3.0.0 of the dataset for each cohort in the following:
        - [Voice Disorders](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/adults/Voice%20Disorders%20Protocol.md>)
        - [Respiratory](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/adults/Respiratory%20Disorders%20Protocol.md>)
        - [Mood/Psychiatric](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/adults/Mood%20and%20Psychiatric%20Disorders%20Protocol.md>)
        - [Neurological](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/adults/Neurological%20and%20Neurodegenerative%20Disorders%20Protocol.md>)
        - [Controls](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/adults/Generic%20Protocol%20(Controls).md>)
        - [Pediatrics](<https://kind-lab.github.io/vbai-fhir/protocol.html>)
          - [Peds 10+](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/pediatrics/Pediatric%20Disorders%20-%20Ages%2010%2B.md>)
          - [Peds 6-10](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20%5B6-10).md>)
          - [Peds 4-6](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20%5B4-6).md>)
          - [Peds 2-4](<https://github.com/eipm/bridge2ai-redcap/blob/main/docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20%5B2-4).md>)
        """
    )

    csv_file_path = "tables/Disease_cohort_inclusion_exclusion_criteria.csv"
    caption = 'Table 1 - Disease cohort inclusion/exclusion criteria and validation methods'
    
    def map_tasks_to_videos(task):
        tasks_to_link = {
            "Respiration Part A": "https://www.youtube.com/watch?v=Yb4bMj18Iqg",
            "Cough part A": "https://www.youtube.com/watch?v=Yb4bMj18Iqg",
            "Breath Sounds": "https://www.youtube.com/watch?v=i7BhlwNMk28",
            "Voluntary Cough": "https://www.youtube.com/watch?v=2rLMfMjS_R0",
            "Prolonged Vowel": "https://www.youtube.com/watch?v=ZanjPvWkB3M",
            "Maximum Phonation Time": "https://www.youtube.com/watch?v=1limRFPAtPE",
            "Glides": "https://www.youtube.com/watch?v=xKBYdkwEOvU",
            "Loudness": "https://www.youtube.com/watch?v=5ssCSqZPb7Y",
            "Diadochokinesis": "https://www.youtube.com/watch?v=RlY5KMXtZ4o",
            "Rainbow Passage": "https://www.youtube.com/watch?v=Syq_ryCNQKQ",
            "Caterpillar Passage": "https://www.youtube.com/watch?v=jN7bGT-PFXY",
            "Free Speech Part A": "https://www.youtube.com/watch?v=FqK0WeGCAzg",
            "Picture Description": "https://www.youtube.com/watch?v=abjWJEN6jf8",
            "Free Speech Voice": "https://www.youtube.com/watch?v=5QMBSHNLRVI",
            "Story Recall": "https://www.youtube.com/watch?v=cfkU-N5tWe4",
            "Animal Fluency": "https://www.youtube.com/watch?v=4lkEAxDiEE8",
            "Open Response Questions": "https://www.youtube.com/watch?v=THfOnGCaALA",
            "Word-Color Stroop": "https://www.youtube.com/watch?v=IzotHKbYh30",
            "Productive Vocabulary": "https://www.youtube.com/watch?v=TEshcUAlfPA",
            "Cape-V Sentences": "https://www.youtube.com/watch?v=1qbiCdWxuSY",
            "Random Item generation": "https://www.youtube.com/watch?v=ry__w1Mm2aE",
            "Cinderella Story": "https://www.youtube.com/watch?v=eHx-vetG8Fk",
            "ABC’s": None,
            "Ready For School": None,
            "Favorite Show": None,
            "Favorite Food": None,
            "Outside of School": None,
            "Months": None,
            "Counting": None,
            "Naming Animals": None,
            "Naming Food": None,
            "Identifying Pictures": None,
            "Picture Description (Pediatrics)": None,
            "Long Sounds": None,
            "Noisy Sounds": None,
            "Caterpillar Passage (Pediatrics)": None,
            "Repeat Words": None,
            "Role naming": None,
            "Repeat Sentences": None,
            "Silly Sounds": None,
        }

        link = tasks_to_link[task]
        if link:
            return f"{task} [<a href=\"{link}\">Example</a>]"
        else:
            return f"{task}"

    def map_questionnaire_link(q_link):
        return f"<a href=\"{q_link}\">PDF</a>"

    create_html_table(csv_file_path, caption, [], 0)

    csv_file_path = "tables/Acoustic_Tasks_Protocol.csv"
    caption = 'Table 2 - Acoustic Tasks in Protocol'
    create_html_table(csv_file_path, caption,link_formatter={"Task": map_tasks_to_videos})

    csv_file_path = "tables/Validated_Questionnaires.csv"
    caption = 'Table 3 - Validated Questionnaires integrated into App'
    create_html_table(csv_file_path, caption, ['X'],link_formatter={'Example': map_questionnaire_link})
