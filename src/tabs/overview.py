import streamlit as st

def overview_page(tab_name):
    st.info("Training opportunities for using the dataset: [https://www.b2aivoicescholars.org/](https://www.b2aivoicescholars.org/)")
    st.markdown(
        """
        Bridge2AI-Voice is a Precision Public Health grand challenge project funded by the NIH Common Fund Bridge2AI 
        Program. Bridge2AI-Voice seeks to create a flagship, standardized, and ethically sourced dataset of 10,000 
        voices linked to health information to fuel research and discovery in voice biomarkers. 
 
        Our group aims to promote integration of voice as a biomarker of health in clinical care. To do so, we will 
        generate a large multi-institutional, ethically sourced, and diverse voice dataset linked to multimodal health 
        biomarkers to fuel voice AI research. Data collection is performed via a novel app (The Bridge2AI-Voice App) 
        available as smartphone application linked to electronic health records (EHR). The app collected breathing sounds, 
        voice, speech and linguistic tasks but also a considerable amount of health information through surveys and 
        validated questionnaires. Other multimodal data collected includes imaging, genomics and respiratory function 
        tests amongst others. The consortium is also addressing the growing ethical, legal, and social challenges surrounding 
        voice AI, including risks of voice re-identification, vulnerabilities like voice AI hacking, concerns around voice 
        data sharing and privacy, and the influence of gender and racial diversity on the development and application of 
        these technologies.
        
        Our developed best ethical practices through ethical inquiry have guided the development of voice collection 
        protocol as well as data dissemination practices.     
        
        As voice is increasingly being recognized as a biomarker of health by the tech world and voice AI is gaining attention 
        from multi-nationals such as Google, Amazon, Mozilla and Apple amongst others, many important issues related to patient 
        privacy protection, ethical and fair representation of population, and clinical accuracy are arising. As a 
        multidisciplinary group of academic experts, we aim to influence and guide the world of voice AI by ensuring patient 
        protection through ethical and fairness principles and create safe innovative infrastructures to disseminate ethically 
        sourced data for the future generations of voice AI researchers.
 
        Based on the existing literature and ongoing research in different fields of voice research, our group has identified 
        5 disease cohort categories for which voice changes have been associated to specific diseases with well-recognized 
        unmet needs and for which our data acquisition efforts are focused: 
        - Voice Disorders
        - Neurological and Neurodegenerative Disorders 
        - Mood and Psychiatric Disorders 
        - Respiratory disorders 
        - Pediatric Voice and Speech Disorders 
 
        **Please Note:** The public data releases do not contain pediatric data. It also does not contain an equal distribution 
        of these categories of diseases. Further releases will contain additional data.
        """
    )
    
    st.markdown(
        """
        ## Data Access
        
        ### Access audio recordings

        Instructions for accessing the data are provided on the [data access page](https://wustl-catalog.instructure.com/courses/643/pages/how-to-access-the-data) of the Bridge2AI learning module.

        #### Derived dataset

        A derived dataset containing spectrograms and combined phenotypic data is available on PhysioNet under a permission access mechanism.
        Registration on PhysioNet and signing of a data use agreement will enable access. The latest version of the dataset is available at the following URL:
        """
    )
    st.link_button("Bridge2AI-Voice: An ethically-sourced, diverse voice dataset linked to health information", type="primary", url="https://doi.org/10.13026/37yb-1t42",  help="Bridge2AI-Voice: An ethically-sourced, diverse voice dataset linked to health information", icon=":material/login:")
    
    st.markdown(
        """
        #### Dataset including raw audio

        Raw audio is available under a controlled access mechanism.

        """
    )
    st.link_button("Bridge2AI-Voice: An ethically-sourced, diverse voice dataset linked to health information (Audio included)", type="primary", url="https://physionet.org/content/b2ai-voice-audio/",  help="Bridge2AI-Voice: An ethically-sourced, diverse voice dataset linked to health information (Audio included)", icon=":material/login:")
                   
    st.markdown(
        """
        ### Older Versions
        
        An earlier version of the feature only dataset is available on HealthDataNexus, which provides cloud-compute alongside the dataset rather than allowing data downloads.
        """
    )

    st.link_button("Request Data Access to v1.0 via Health Data Nexus", type="primary", url="https://healthdatanexus.ai/content/b2ai-voice/1.0/",  help="Register for Data Access via Health Data Nexus", icon=":material/login:")
