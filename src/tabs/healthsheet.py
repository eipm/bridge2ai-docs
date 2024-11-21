import streamlit as st

# Define the content of the Health Sheet page
def healthsheet_page(tab_name):

    st.header("**General Information**")

    st.markdown('''
        **Provide a 2-sentence summary of this dataset.**

        The Bridge2AI Voice dataset aims to enable the development, benchmarking, or validation of clinically applicable machine-learning models for diagnosing a wide range of health conditions using voice data, including vocal pathologies, neurological, psychiatric, respiratory, and pediatric voice disorders. This dataset contains voice recordings and key metadata and is structured to be Findable, Accessible, Interoperable, and Reusable (FAIR).
    '''
    )

    with st.expander("**Has the dataset been audited before? If yes, by whom and what are the results?**", expanded=False):
        st.write('''The dataset has been audited internally for missingness and consistency by the data release team. A missingness table is included with the dataset. Certain aspects of the data (e.g., transcription) were generated using off the shelf models that have not been audited for correctness.''')

    st.header("**Dataset Versioning**")

    with st.expander("**Does the dataset get released as static versions or is it dynamically updated?**", expanded=False):
        st.write('''Static''')

    with st.expander("**Does the current version/subversion of the dataset come with predefined task(s), labels, and recommended data splits (e.g., for training, development/validation, testing)? If yes, please provide a high-level description of the introduced tasks, data splits, and labeling, and explain the rationale behind them. Please provide the related links and references. If not, is there any resource (website, portal, etc.) to keep track of all defined tasks and/or associated label definitions? (please note that more detailed questions w.r.t labeling is provided in further sections)**", expanded=False):
        st.write('''Yes, the current version of the dataset comes with predefined tasks and labeling. The tasks are primarily designed for training machine-learning models for disease detection and classification using voice data. Labels include diagnostic categories such as vocal pathologies, neurological disorders, psychiatric conditions, and respiratory disorders. However, there are no predefined recommended data splits for training, validation, or testing. Researchers are encouraged to create their own data splits based on their specific requirements. More details regarding task definitions and labeling can be found in the dataset.''')

    st.header("**Motivation**")

    with st.expander("**For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.**", expanded=False):
        st.write('''The Bridge2AI Voice dataset was created to address a gap in the availability of large-scale, diverse, and well-documented voice data for use in clinical machine-learning applications. Previous studies on machine learning-based voice diagnosis produced promising results, but their sample sizes were too small, or they lacked the key metadata needed for training robust, clinically useful models. The dataset aims to bridge this gap by providing an ethically sourced, large, and diverse dataset to develop, benchmark, or validate clinically applicable AI/ML models. The goal is to facilitate the use of voice as a non-invasive, cost-effective biomarker for the screening, diagnosis, and monitoring of a wide range of health conditions.''')

    with st.expander("**What are the applications that the dataset is meant to address? (e.g., administrative applications, software applications, research)**", expanded=False):
        st.write('''The Bridge2AI Voice dataset is primarily intended for research applications, specifically in the development of AI and machine-learning models for healthcare. It aims to support clinical research in disease screening, diagnosis, and monitoring through voice biomarkers. The dataset can be used for AI model pretraining, finetuning, benchmarking, or validation.''')

    with st.expander("**Are there any types of usage or applications that are discouraged from using this dataset? If so, why?**", expanded=False):
        st.write('''Yes, there are restrictions on the use of this dataset, as detailed in the Registered Data Access Agreement. These restrictions reflect the B2AI-Voice Consortium’s commitment to advancing ethical and trustworthy research practices that respect and protect the rights and interests of research participants. Accordingly, the dataset is intended solely for commercial and non-commercial research purposes by Authorized Researchers. Specifically, the dataset is not to be used a) to attempt to re-identify research participants, nor any actions that could reasonably lead to re-identification; and b) for any purpose that could foreseeably cause harm or stigmatization to research participants, their families, communities, or specific populations. Lastly, intellectual property protections, database rights, or related rights may not be used in a manner that restricts or limits access to any part of the dataset or to any conclusions derived from it. This restriction ensures that future use of the dataset remains unrestricted, in alignment with the Open Science principles upheld by the B2AI-Voice Consortium. Specifically, the dataset should not be used for non-research applications, such as hiring decisions, insurance premium adjustments, or any form of surveillance that could lead to discrimination or harm. These limitations are intended to prevent unethical or biased outcomes that could negatively impact individuals based on their health conditions or voice characteristics.''')

    with st.expander("**Who created this dataset (e.g., which team, research group), and on behalf of which entity (e.g., company, institution, organization)?**", expanded=False):
        st.write('''Voice as a Biomarker of Health is being co-led by Dr Yaël Bensoussan, MD, MSc from USF Health Morsani College of Medicine and Olivier Elemento, PhD from Weill Cornell Medicine, who are co-principal investigators for the project, which is funded by the NIH Common Fund within the Bridge2AI Program. The project also includes lead investigators from 10 other universities in North America; Alexandros Sigaras, MSc and Anaïs Rameau, MD, MPhil (Weill Cornell Medicine), Maria Powell, CCC-SLP, PhD (Vanderbilt University Medical Center), Ruth Bahr, CCC-SLP, PhD (USF Health Morsani College of Medicine), Jennifer Sui, MD (Hospital for Sick Children), Philip Payne, PhD (Washington University in St. Louis), David Dorr, MD (Oregon Health & Science University), Jean-Christophe Bélisle-Pipon, PhD (Simon Fraser University), Vardit Ravitsky , PhD (The Hastings Center), Satrajit Ghosh, PhD (Massachusetts Institute of Technology), Frank Rudzizc, PhD (University of Toronto), Jordan Lerner-Ellis, PhD (Sinai Health) and Don Bolser, PhD (University of Florida).There are over 50 other investigators, clinicians, scholars and trainees who have contributed to the development of this dataset. Please see full list of collaborators here: [The Bridge2AI-Voice Consortium (2024)](https://b2ai-voice.org/wp-content/uploads/2024/11/FOR-WEBSITE-Year-2-Bridge2AI-Voice-Consortium-Authors.docx)''')

    with st.expander("**Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number. If the funding institution differs from the research organization creating and managing the dataset, please state how.**", expanded=False):
        st.write('''The NIH Common Fund<br>[3TF- OT2ActfOD032720Projectf01S1](https://reporter.nih.gov/search/ES3d7yibyESXrX-rp6g1Ng/project-details/10858564)''', unsafe_allow_html=True)
        
    with st.expander("**What is the distribution of backgrounds and experience/expertise of the dataset curators/generators?**", expanded=False):
        st.write('''The curators and generators of the Bridge2AI Voice dataset come from a diverse range of backgrounds and areas of expertise, reflecting the interdisciplinary nature of the project. The team includes:
1. <ins>Clinicians and Healthcare Professionals:</ins> Practicing doctors and healthcare workers involved in the direct collection of clinical data and providing practical insights into the medical relevance of the dataset.  
2. <ins>Biomedical Researchers:</ins> Experts in clinical medicine, neurology, and psychiatry, contributing deep knowledge of the medical conditions being studied. 
3. <ins>Machine Learning and AI Specialists:</ins> Researchers and engineers with expertise in machine learning, artificial intelligence, and data science, focusing on developing models and algorithms for analyzing voice data. 
4. <ins>Data Scientists and Statisticians:</ins> Professionals skilled in data curation, preprocessing, and statistical analysis, ensuring the dataset is robust and suitable for machine learning applications. 
5. <ins>Social Scientists and Ethicists:</ins> Experts in ethics, sociology, and human subjects research, ensuring the dataset is ethically sourced and meets standards for privacy and consent. 
6. <ins>Engineers and Technologists:</ins> Individuals with experience in software development, systems engineering, and data infrastructure, contributing to the technical aspects of data collection, storage, and dissemination. 
''', unsafe_allow_html=True)

    st.header("**Data Composition**")

    with st.expander("**What do the instances that comprise the dataset represent (e.g., documents, images, people, countries)? Are there multiple types of instances? Please provide a description.**", expanded=False):
        st.write('''Each instance represents a person.''')

    with st.expander("**How many instances are there in total (of each type, if appropriate) (breakdown based on schema, provide data stats)?**", expanded=False):
        st.write('''There are currently around 307 instances.''')

    with st.expander("**How many patients/subjects does this dataset represent? Answer this for both the preliminary dataset and the current version of the dataset.**", expanded=False):
        st.write('''307''')

    with st.expander("**Does the dataset contain all possible instances, or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable). Answer this question for the preliminary version and the current version of the dataset in question.**", expanded=False):
        st.write('''It is a sample of larger ongoing collection. The data is not representative because it was collected at a limited number of geographic locations. We hope to make it more representative by shifting to remote collection and designing our recruiting approach in a way that controls for more variables.''')

    with st.expander("**What data modality does each patient data consist of? If the data is hierarchical, provide the modality details for all levels (e.g., text, image, physiological signal). Break down all levels and specify the modalities and devices.**", expanded=False):
        st.write('''Audio recordings, questionnaire responses.''')

    with st.expander("**What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.**", expanded=False):
        st.write('''Raw audio and questionnaire response data, as well as extracted audio features.''')

    with st.expander("**Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable).**", expanded=False):
        st.write('''Yes, some questions are optional. There may be data collection irregularities that caused some information to be missing from individual instances. Each individual answered a common set of questions and then responded to a primary diagnostic category relevant additional questions.''')

    with st.expander("**Are relationships between individual instances made explicit? (e.g., They are all part of the same clinical trial, or a patient has multiple hospital visits, and each visit is one instance)? If so, please describe how these relationships are made explicit.**", expanded=False):
        st.write('''No, they are unrelated.''')

    with st.expander("**Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description. (e.g., losing data due to battery failure, or in survey data subjects skip the question, radiological sources of noise).**", expanded=False):
        st.write('''Yes, different sites have different collection configurations. The collection protocol changed over the course of the study.''')

    with st.expander("**Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description. (e.g., losing data due to battery failure, or in survey data subjects skip the question, radiological sources of noise).**", expanded=False):
        st.write('''Yes, different sites have different collection configurations. The collection protocol changed over the course of the study.''')

    with st.expander("**Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, other datasets)? If it links to or relies on external resources:**", expanded=False):
        st.write('''
            **a. Are there guarantees that they will exist, and remain constant, over time?**<br>NA<br>
            **b. Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?**<br>NA<br>
            **c. Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.**<br>It is self-contained.
            ''', unsafe_allow_html=True)
        
    with st.expander("**Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications that is confidential)? If so, please provide a description.**", expanded=False):
        st.write('''No''')

    with st.expander("**Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise pose any safety risk (such as psychological safety and anxiety)? If so, please describe why.**", expanded=False):
        st.write('''This dataset includes the transcription of free speech tasks. While the inclusion of information of that type is unlikely, it cannot be completely avoided, as research participants are responsible for their choice of language.''')

    with st.expander("**If the dataset has been de-identified, were any measures taken to avoid the re-identification of individuals? Examples of such measures: removing patients with rare pathologies or shifting time stamps.**", expanded=False):
        st.write('''This dataset has been deidentified through removal of all audio data and certain sensitive fields identified by a team of ethicists.''')

    with st.expander("**Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)? If so, please provide a description.**", expanded=False):
        st.write('''Yes:<br><ins>racial or ethnic origins</ins>: The dataset includes race information.<br>
        <ins>sexual orientations</ins>: The dataset includes sexual orientation information.<br>
        <ins>financial or health data</ins>: The dataset includes socioeconomic and health information.''', unsafe_allow_html=True)

    st.header("**Devices and Contextual Attributes in Data Collection**")

    with st.expander("**For data that requires a device or equipment for collection or the context of the experiment, answer the following additional questions or provide relevant information based on the device or context that is used (for example)**", expanded=False):
        st.write('''Data is collected on iPads (9th or 10th generation), iPad Air (5th generation) using an Avid AE-36 microphone and an Apple dongle to connect it to the iPad.''')

    st.header("**Challenge in tests and confounding factors**")

    with st.expander("**Which factors in the data might limit the generalization of potentially derived models? Is this information available as auxiliary labels for challenge tests? For instance:**", expanded=False):
        st.write('''**a. Number and diversity of devices included in the dataset.**<br>Distinct iPad devices were used at each site.<br>
            **b. Data recording specificities, e.g., the view for a chest x-ray image.**<br>The data were recorded with a head mounted headset with a microphone that could be at slightly different distances. The clinical diagnosis, depending on the disorder, was performed by one clinician or based on an EHR record or prescription.<br>
            **c. Number and diversity of recording sites included in the dataset.**<br>There are 5 recording sites included in the dataset.<br>
            **d. Distribution shifts over time.**<br>Changes in diagnostic criteria or practices could be a source of distribution shift.''', unsafe_allow_html=True)
        
    with st.expander("**What confounding factors might be present in the data?**", expanded=False):
        st.write('''Noise artifacts, variations in diagnostic practices, inaccurate questionnaire responses, under reporting.''')

    with st.expander("**What confounding factors might be present in the data?**", expanded=False):
        st.write('''Noise artifacts, variations in diagnostic practices, inaccurate questionnaire responses, under reporting.<br> 
                **a. Interactions between demographic or historically marginalized groups and data recordings, e.g., were women patients recorded in one site, and men in another?**<br>Groups that have less trust in the medical system, AI, or are less proximal to the collection sites would have been less likely to be recruited.<br>
                **b. Interactions between the labels and data recordings, e.g. were healthy patients recorded on one device and diseased patients on another?**<br>Participants were screened for different disorders based on site, so they also had their data collected with different devices.''', unsafe_allow_html=True)

    st.header("**Collection and use of demographic information**")

    with st.expander("**Does the dataset identify any demographic sub-populations (e.g., by age, gender, sex, ethnicity)?**", expanded=False):
        st.write('''Age, Gender, Sex, Ethnicity, Socioeconomic status''')

    st.header("**Pre-processing / de-identification**")

    with st.expander("**Was there any pre-processing for the de-identification of the patients? Provide the answer for the preliminary and the current version of the dataset.**", expanded=False):
        st.write('''Yes, the data were extracted from the raw audio to limit re-identification and only the extracted features are being released with the dataset.''')

    with st.expander("**Was there any pre-processing for cleaning the data? Provide the answer for the preliminary and the current version of the dataset.**", expanded=False):
        st.write('''No''')

    with st.expander("**Was the “raw” data (post de-identification) saved in addition to the preprocessed/cleaned data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data.**", expanded=False):
        st.write('''Yes, it is saved and is not accessible publicly.''')

    with st.expander("**Were instances excluded from the dataset at the time of preprocessing? If so, why? For example, instances related to patients under 18 might be discarded.**", expanded=False):
        st.write('''No''')

    st.header("**Labeling and subjectivity of labeling**")

    with st.expander('''**Is there an explicit label or target associated with each data instance? Please respond for both the preliminary dataset and the current version.**''', expanded=False):
        st.write('''<b>a. If yes:</b><br>
<ul>
    <li><b>What are the labels provided?</b></li>
    <li><b>Who performed the labeling? For example, was the labeling done by a clinician, ML researcher, university or hospital?</b></li>
</ul>
Diagnostic labels are the result of a clinical assessment of the participant. At each site, a local clinician provided the diagnosis based on a clinical interview and appropriate work-up. For the psychiatric disorders cohort, this assessment was determined by using the participants EHR record or using an active prescription, which was done outside of data collection by an appropriately licensed clinician.
<br>
<b>b. What labeling strategy was used?</b><br>
Gold standard label available in the data (diagnosed by a clinician).<br>
<b>c. Human-labeled data:</b><br>
<ul>
    <li><b>How many labelers were considered?</b><br>Single labeler per data</li>
    <li><b>What is the demographic of the labelers? (countries of residence, of origin, number of years of experience, age, gender, race, ethnicity, etc.)</b><br>Typically, the clinician at site of data collection, or external to (for prior diagnostic assessment)</li>
    <li><b>What guidelines did they follow?</b><br>Per Bridge2AI Protocols and ICD-10 codes.</li>
    <li><b>How many labelers provide a label per instance?</b><br>1</li>
</ul>''', unsafe_allow_html=True)
        
    with st.expander('''**What are the human-level performances in the applications that the dataset is supposed to address?**''', expanded=False):
        st.write('''It varies greatly''')

    with st.expander('''**Is the software used to preprocess/clean/label the instances available? If so, please provide a link or other access point.**''', expanded=False):
        st.write('''Yes. [https://github.com/sensein/b2aiprep](https://github.com/sensein/b2aiprep), [https://github.com/sensein/senselab](https://github.com/sensein/senselab)''')

    with st.expander('''**Is there any guideline that the future researchers are recommended to follow when creating new labels/defining new tasks?**''', expanded=False):
        st.write('''The process for any new labels should be described alongside any release of a model or publication. This process should include exact variables used for this determination.''')

    st.header("**Collection Process**")

    with st.expander('''**Were any REB/IRB approval (e.g., by an institutional review board or research ethics board) received? If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.**''', expanded=False):
        st.write('''Yes''')

    with st.expander('''**How was the data associated with each instance acquired? Was the data directly observable (e.g., medical images, labs, or vitals), reported by subjects (e.g., survey responses, pain levels, itching/burning sensations), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.**''', expanded=False):
        st.write('''The data was directly observable and reported by subjects. Clinical diagnoses were verified by clinicians reviewing audio and/or imaging data, looking at electronic health records, or medication prescriptions.''')

    with st.expander('''**What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)? How were these mechanisms or procedures validated? Provide the answer for all modalities and collected data. Has this information been changed through the process? If so, explain why.**''', expanded=False):
        st.write('''The data has been collected on an iPad app.''')

    with st.expander('''**Who was involved in the data collection process (e.g., patients, clinicians, doctors, ML researchers, hospital staff, vendors, etc.) and how were they compensated (e.g., how much were contributors paid)?**''', expanded=False):
        st.write('''Research teams, which may include medical, graduate, or undergraduate students, coordinated with clinicians/doctors to identify appropriate participants. These clinicians and doctors were listed under IRB as co-investigators, and were added to the consortium, so that that their names are to be included on consortium-level publications that emerge from the research. Hospital staff were not involved in scheduling but assisted in the logistics of coordinating data collection.
                 <br><br>Participants were compensated for their time through electronic gift cards. Participants currently receive \$40 for a data collection session that takes less than 90 minutes, and \$80 for a session that takes over 90 minutes, for no more than a total of 3 sessions and maximum compensation of \$120.''', unsafe_allow_html=True)

    with st.expander('''**Over what timeframe was the data collected?**''', expanded=False):
        st.write('''The data was collected over a period of 12 months.''')

    with st.expander('''**Does the dataset relate to people?**''', expanded=False):
        st.write('''Yes''')

    with st.expander('''**Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., hospitals, app company)?**''', expanded=False):
        st.write('''Directly''')

    with st.expander('''**Were the individuals in question notified about the data collection?**''', expanded=False):
        st.write('''Yes, participants went through an IRB-approved consent process.''')

    with st.expander('''**Did the individuals in question consent to the collection and use of their data?**''', expanded=False):
        st.write('''Yes, all participants have been duly informed and agreed to the collection and the use of their data via prospective informed consent.''')

    with st.expander('''**If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?**''', expanded=False):
        st.write('''Consenting participants are informed that they may withdraw from the study at any point. If a participant chooses to withdraw during or before the voice data collection, their data will not be included in the database. Participants are informed that research data (including voice recordings) cannot be removed from the database once the voice data collection process is completed.''')

    with st.expander('''**In which countries was the data collected?**''', expanded=False):
        st.write('''USA and Canada''')

    with st.expander('''**Has an analysis of the potential impact of the dataset and its use on data subjects been conducted?**''', expanded=False):
        st.write('''No''')

    st.header("**Inclusion Criteria-Accessibility in data collection**")

    with st.expander('''**Is there any language-based communication with patients (e.g.: English, French)? If yes, describe the choices of language(s) for communication. (for example, if there is an app used for communication, what are the language options?)**''', expanded=False):
        st.write('''English language was used for communication with study participants.<br>The only language option for v1.0.0 is English. Spanish versions of the protocol are under development.''', unsafe_allow_html=True)

    with st.expander('''**What are the accessibility measurements and what aspects were considered when the study was designed and implemented?**''', expanded=False):
        st.write('''The protocol asks about disabilities. Collection accessibility was facilitated through the normal means of the collection sites, including reading questions to participants when needed.''')

    st.header("**Uses**")

    with st.expander('''**Has the dataset been used for any tasks already? If so, please provide a description.**''', expanded=False):
        st.write('''A restricted version of the dataset containing raw audio has been used in the Bridge2AI Summer School and hackathon.''')

    with st.expander('''**Does using the dataset require the citation of the paper or any other forms of acknowledgement? If yes, is it easily accessible through google scholar or other repositories**''', expanded=False):
        st.write('''>Bensoussan, Yael, et al. "Developing Multi-Disorder Voice Protocols: A team science approach involving clinical expertise, bioethics, standards, and DEI." Proc. Interspeech 2024. 2024. [https://www.isca-archive.org/interspeech_2024/bensoussan24_interspeech.html](https://www.isca-archive.org/interspeech_2024/bensoussan24_interspeech.html)''')

    with st.expander('''**Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point. (besides Google scholar)**''', expanded=False):
        st.write('''No''')

    with st.expander('''**Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other undesirable harms (e.g., financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?**''', expanded=False):
        st.write('''Yes, this dataset has skews based on disorder category, site, and other demographic factors. Users should consider the multivariate distribution when assessing utility for different questions.''')

    with st.expander('''**Are there tasks for which the dataset should not be used? If so, please provide a description.**''', expanded=False):
        st.write('''Yes, there are certain applications that are discouraged from using this dataset. Specifically, the dataset should not be used for non-clinical applications such as hiring decisions, insurance premium adjustments, or any form of surveillance that could lead to discrimination or harm. These discouraged uses are intended to prevent unethical or biased outcomes that could negatively impact individuals based on their health conditions or voice characteristics. The dataset is intended strictly for research that prioritize patient safety, privacy, and ethical use.''')

    st.header("**Dataset Distribution**")

    with st.expander('''**Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?**''', expanded=False):
        st.write('''The dataset will be distributed broadly to individuals outside of the entity who created the dataset.''')

    with st.expander('''**How will the dataset be distributed (e.g., tarball on website, API, GitHub)? Does the dataset have a digital object identifier (DOI)?**''', expanded=False):
        st.write('''The dataset will be distributed through a data publishing platform accessible at [https://healthdatanexus.ai/](https://healthdatanexus.ai/)<br><br>
                 This platform provides publicly accessible metadata regarding the dataset with a DOI for persistent resolution. The dataset itself requires registered access.''', unsafe_allow_html=True)

    with st.expander('''**When was/will the dataset be distributed?**''', expanded=False):
        st.write('''The data was published and made available at the end of November, 2024.''')

    with st.expander('''**Assuming the dataset is available, will it be/is the dataset distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.**''', expanded=False):
        st.write('''
                Users of the dataset must agree to terms laid out in the registered access agreement. The terms relating to intellectual property are repeated here for informational purposes only:

                <p style="margin-left:30px;">INTELLECTUAL PROPERTY RIGHTS. You understand and acknowledge that the Data may be protected by copyright and other rights, including other intellectual property rights. Duplication, as reasonably required to carry out Your Research Project with the Data, is nonetheless permitted. Sale of all or part of the Data on any media is not permitted. You recognize that nothing in this Agreement shall operate to transfer to You any intellectual property rights in or relating to the Data. You agree not to make intellectual property claims on the Data. You agree not to use intellectual property protection in ways that would prevent or block access to, or use of, any element of these Data, or conclusions drawn directly from the Data. You can elect to perform further research that would add intellectual and resource capital to the Data and decide to obtain intellectual property rights on these downstream discoveries. You agree to implement licensing policies that will not obstruct further research. You agree to respect the Fort Lauderdale Agreement.</p>

                There are no fees associated with these restrictions.''', unsafe_allow_html=True)
        
    with st.expander('''**Have any third parties imposed IP-based or other restrictions on the data associated with the instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.**''', expanded=False):
        st.write('''No IP-based restrictions have been imposed by third parties.''')

    with st.expander('''**Do any export controls or other regulatory restrictions apply to the dataset or to individual instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.**''', expanded=False):
        st.write('''No export controls apply to the dataset.''')

    st.header("**Maintenance**")

    with st.expander('''**Who is supporting/hosting/maintaining the dataset?**''', expanded=False):
        st.write('''The dataset is supported by the NIH via the Bridge2AI project.<br>
                    The dataset is hosted by the [Health Data Nexus](https://healthdatanexus.ai/), a data publishing platform maintained by the Temerty Center for Artificial Intelligence Research and Education in Medicine (T-CAIREM) based at the University of Toronto. The Health Data Nexus maintains the technical infrastructure hosting dataset and provides continued access to interested researchers.
                ''', unsafe_allow_html=True)
        
    with st.expander('''**How can the owner/curator/manager of the dataset be contacted (e.g. email address)?**''', expanded=False):
        st.write('''The platform team may be contacted through: contact@healthdatanexus.ai<br>
                    The curator of the data may be contacted through: info@b2ai-voice.org''', unsafe_allow_html=True)
        
    with st.expander('''**Is there an erratum? If so, please provide a link or other access point.**''', expanded=False):
        st.write('''There is no erratum. A changelog for each dataset version is published online with the dataset metadata.''')

    with st.expander('''**Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)? If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?**''', expanded=False):
        st.write('''Yes, further versions of the dataset will be released on a semi-annual (twice a year). These updates will be distributed as new versions of the dataset on the Health Data Nexus platform. Users will be notified through news items on the platform as well as through standard communication channels.''')

    with st.expander('''**If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)? If so, please describe these limits and explain how they will be enforced.**''', expanded=False):
        st.write('''Once data is contributed, the data will be retained as long as it is useful for research purposes, possibly indefinitely.''')

    with st.expander('''**Will older versions of the dataset continue to be supported/hosted/maintained? If so, please describe how and for how long. If not, please describe how its obsolescence will be communicated to users.**''', expanded=False):
        st.write('''By default, older versions of the dataset will continue to be supported, hosted, and made available to researchers. Each version of the dataset has a unique DOI. The dataset publishers reserve the right to remove access to older versions.''')

    with st.expander('''**If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?**''', expanded=False):
        st.write('''For dataset extensions and augmentations, it is possible for others to publish a derivative dataset on the Health Data Nexus which references the original source. These derivative datasets may be made available under the same conditions as the source data.<br><br>
                    For augmentations to the code used to produce the data, the open-source repositories have discussion forums and issue pages which allow for public discussion of data preprocessing. The repository also has a mechanism (“pull requests”) for contributing improvements to the data preprocessing code.''', unsafe_allow_html=True)