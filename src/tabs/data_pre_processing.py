import streamlit as st

def data_pre_processing_page(tab_name):
    st.markdown(
        """
        The raw audio files and the questionnaire data exported from REDCap were converted to a BIDS-like structure as 
        shown in the figure below. This dataset organization is based on Brain Imaging Data Structure v1.9.0. All 
        questionnaires are represented with metadata available through FHIR (GitHub:  [https://kind-lab.github.io/vbai-fhir/protocol.html](https://kind-lab.github.io/vbai-fhir/protocol.html) ) 
        and ReproSchema ([https://github.com/sensein/b2ai-redcap2rs](https://github.com/sensein/b2ai-redcap2rs)).

        ```
        bridge2ai-voice-dataset
        ├── CHANGES.md
        ├── README.md
        ├── dataset_description.json
        ├── participants.json
        ├── participants.tsv
        ├── phenotype
        │   ├── <measurement_tool_name>.json
        │   └── <measurement_tool_name>.tsv
        └── sub-<participant_id>
            ├── ses-<another_session_id>
            │   ├── beh
            │   │   ├── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_metadata.json
            │   │   └── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_response.json
            │   └── voice
            │       ├── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_audio.wav
            │       ├── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_metadata.json
            ├── ses-<session_id>
            │   ├── beh
            │   │   ├── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_metadata.json
            │   │   └── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_response.json
            │   └── voice
            │       ├── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_audio.wav
            │       ├── sub-<participant_id>_ses-<session_id>_task-<task_name>_run-<index>_metadata.json
            └── sessions.tsv
        ```

        The dataset is then processed using b2aiprep to extract features from each waveform. The settings for
        extraction can be found [here](https://github.com/sensein/b2aiprep/blob/93b9a1ed46b256cfd77a8c15b6e58d489f8ff2bb/src/b2aiprep/prepare/prepare.py#L105):
        The features extracted include:
        - OpenSmile eGeMaps features per audio file
        - Parselmouth/Praat speech features for any speech tasks
        - Speech intelligibility metrics for speech tasks
        Time varying features (using Torchaudio)
        - Pitch contour
        - Spectrograms
        - Mel spectrogram, and 
        - MFCCs

        **Speech tasks included**
        - Animal fluency
        - Cape V sentences
        - Caterpillar Passage
        - Cinderella Story
        - Diadochokinesis
        - Picture description
        - Productive Vocabulary
        - Prolonged vowel
        - Rainbow Passage
        - Random Item Generation
        - Story recall
        - Word-color Stroop

        **Feature-only Dataset**
        To maximize distribution, an AI-Ready feature only dataset is created in which the questionnaire features 
        are combined into a single table. This can be used for cohort selection.

        The waveform-derived features are stored using two formats:
        1.	A fixed feature format that includes static features extracted from the entire waveform
        2.	A temporal format that varies for each audio file depending on the length of recording.

        This dataset can be downloaded through credentialled access without a data access request from Physionet.

        **Methods of De-identification**
        All direct identifiers were removed, as these would reveal the identity of the research participant. These 
        include name, civic address, and social security numbers. Indirect identifiers were removed where these 
        created a significant risk of causing participant re-identification, for example through their combination 
        with other public data available on social media, in government registries, or elsewhere. These include 
        select geographic or demographic identifiers, as well as some information about household composition or 
        cultural identity. Non-identifying elements of data that revealed highly sensitive information, such as 
        information about household income, mental health status, traumatic life experiences, and the like were 
        also removed. 
        
        All raw voice data was removed from the Feature-Only dataset, as this data has the potential to cause 
        individual re-identification or to be used for illicit or unauthorized purposes.
        All sensitive fields are removed from the dataset at this stage. These correspond to data elements encoded 
        as sensitive (Column name: Identifier?) available at: [https://github.com/eipm/bridge2ai-redcap/blob/main/data/bridge2ai_voice_project_data_dictionary.csv](https://github.com/eipm/bridge2ai-redcap/blob/main/data/bridge2ai_voice_project_data_dictionary.csv).

        In addition, all spectrograms, mfcc, and transcriptions from open responses are removed from the feature only dataset.

        **Audit protocol**
        -	Generate missingness tables
        -	Check distributions and outliers
        -	For categorical responses, check against schema
        -	For waveforms:
            -	Check amount of silence
            -	Duration
            -	For speech, check produced speech relative to intended passage

        All processing is done using these toolkits:
        -	B2AIprep (organizing and preprocessing the dataset): [https://github.com/sensein/b2aiprep](https://github.com/sensein/b2aiprep)
        -	SenseLab (processing audio files for research tasks): [https://github.com/sensein/senselab](https://github.com/sensein/senselab)
        """
    )
