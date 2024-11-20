import streamlit as st
from tabs.utils import create_html_table

def collection_methods_page(tab_name):

    st.markdown(

        """
        Data is collected across five disease categories. Initial data release contains data collected from four of five categories (pediatric data to be incorporated in subsequent dataset releases.

        Participants are recruited across different academic institutions from “high volume expert clinics” based on diagnosis and inclusion/exclusion criteria outlined below **(Table 1)**.

        **High Volume Expert Clinics:** Outpatient clinics within hospital systems or academic institutions that have developed an expertise in a specific disease area and see more than 50 patients per month from the same disease category. Ex: Asthma/COPD pulmonary specialty clinic.

        Data is collected in the clinic with the assistance of a trained researched assistant. Future data collection will also occur remotely, however remote data collection did not occur with initial dataset being released. Voice samples are collected prospectively using a custom software application (Bridge2AI-Voice app) with the Bridge2AI-Voice protocols.

        **Clinical validation:** Clinical validation is performed by qualified physician or practitioner based on established gold standards for diagnosis **(Table 1)**.

        **Acoustic Tasks:** Voice, breathing, cough, and speech data are recorded with the app. A total of 22 acoustic Tasks are recorded through the app **(Table 2)**.

        **Demographic surveys and confounders:** Detailed demographic data and surveys about confounding factors such as smoking and drinking history is collected through the smartphone application. 

        **Validated Questionnaires:** The Bridge2AI-Voice protocols contain validated tools and questionnaires for each disease category within the app for data collection **(Table 3)**.

        **Other Multimodal Data:** The rest of the multimodal data including imaging, genomic data (for the neuro cohort), laryngoscopy imaging and other EHR data is extracted from different sites independently and will be uploaded through the REDCAP database. Please note that no external data is released in this v1.0.0.

        Please see publication for protocol development description: 
        >Bensoussan, Yael, et al. "Developing Multi-Disorder Voice Protocols: A team science approach involving clinical expertise, bioethics, standards, and DEI." Proc. Interspeech 2024. 2024. [https://www.isca-archive.org/interspeech_2024/bensoussan24_interspeech.html](https://www.isca-archive.org/interspeech_2024/bensoussan24_interspeech.html).

        The supporting REDCap Data Dictionary, Metadata and Instrument PDF’s are available at [https://github.com/eipm/bridge2ai-redcap](https://github.com/eipm/bridge2ai-redcap) .

        When using the REDCap Data Dictionary and Metadata please cite:
        
        >Bensoussan, Y., Ghosh, S. S., Rameau, A., Boyer, M., Bahr, R., Watts, S., Rudzicz, F., Bolser, D., Lerner-Ellis, J., Awan, S., Powell, M. E., Belisle-Pipon, J.-C., Ravitsky, V., Johnson, A., Zisimopoulos, P., Tang, J., Sigaras, A., Elemento, O., Dorr, D., … Bridge2AI-Voice. (2024). eipm/bridge2ai-redcap. Zenodo. [https://zenodo.org/doi/10.5281/zenodo.12760724](https://zenodo.org/doi/10.5281/zenodo.12760724).
        

        Protocols can be found in the Bridge2AI-Voice documentation for v1.0.0 of the dataset at [https://kind-lab.github.io/vbai-fhir/protocol.html](https://kind-lab.github.io/vbai-fhir/protocol.html).

        """
    )

    csv_file_path = "tables/Disease_cohort_inclusion_exclusion_criteria.csv"
    caption = 'Table 1 - Disease cohort inclusion/exclusion criteria and validation methods'
    create_html_table(csv_file_path, caption)

    csv_file_path = "tables/Acoustic_Tasks_Protocol.csv"
    caption = 'Table 2 - Acoustic Tasks in Protocol'
    create_html_table(csv_file_path, caption)

    csv_file_path = "tables/Validated_Questionnaires.csv"
    caption = 'Table 3 - Validated Questionnaires integrated into App'
    create_html_table(csv_file_path, caption)
