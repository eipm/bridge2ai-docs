import streamlit as st

def data_pre_processing_page(tab_name):
    st.markdown(
        """
        The raw audio files and the questionnaire data exported from REDCap were converted to follow the [Brain Imaging Data Structure v1.9.0](https://bids-specification.readthedocs.io/en/v1.9.0/). The folder structure for the dataset is as follows:

        ```
        b2ai-voice-audio

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
            │   └── audio
            │       ├── sub-<participant_id>_ses-<session_id>_task-<task_name>.wav
            │       ├── sub-<participant_id>_ses-<session_id>_task-<task_name>.json
            └── ses-<session_id>
                └── voice
                    ├── sub-<participant_id>_ses-<session_id>_task-<task_name>.wav
                    ├── sub-<participant_id>_ses-<session_id>_task-<task_name>.json
        ```

        **Speech tasks included**
        - ABC's
        - Animal fluency
        - Cape V sentences
        - Caterpillar Passage
        - Caterpillar Passage (Pediatrics)
        - Cinderella Story
        - Counting
        - Diadochokinesis
        - Favorite Foods
        - Favorite Show/Movies
        - Identifying Pictures
        - Months
        - Naming Animals
        - Naming Foods
        - Outside of School
        - Picture description
        - Picture Description (Pediatrics)
        - Productive Vocabulary
        - Prolonged vowel
        - Rainbow Passage
        - Random Item Generation
        - Ready For School
        - Repeat Words
        - Repeat Sentences
        - Role Naming
        - Story recall
        - Word-color Stroop

        ## AI-Ready derived datasets

        The features only dataset provides AI ready derivations from the raw audio. Features extracted include:
        -	OpenSmile eGeMaps features per audio file
        -	Parselmouth/Praat speech features for any speech tasks
        -	Speech intelligibility metrics for speech tasks
        Time varying features
        -	Torchaudio-based pitch contour, spectrograms, mel spectrogram, and MFCCs

        The waveform-derived features are stored using two formats:
        1.	A fixed feature format that includes static features extracted from the entire waveform
        2.	A temporal format that varies for each audio file depending on the length of recording.

        The questionnaire features are combined into a single table (phenotype.tsv). This can be used for cohort selection.

        **Methods of De-identification for v2.0.0**
        All direct identifiers were removed, as these would reveal the identity of the research participant. These include name, civic address, and social security numbers. Indirect identifiers were removed where these created a significant risk of causing participant re-identification, for example through their combination with other public data available on social media, in government registries, or elsewhere. These include select geographic or demographic identifiers, as well as some information about household composition or cultural identity. Non-identifying elements of data that revealed highly sensitive information, such as information about household income, mental health status, traumatic life experiences, and the like were also removed.

        Raw audio transcripts were reviewed and any audio recordings which contained potentially identifying information were removed from the release.

        All sensitive fields are removed from the dataset at this stage. These correspond to data elements encoded as sensitive (Column name: "Identifier?") listed in the [RedCap data dictionary (CSV)](https://github.com/eipm/bridge2ai-redcap/blob/main/data/bridge2ai_voice_project_data_dictionary.csv).

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
        -	[b2aiprep](https://github.com/sensein/b2aiprep): organizing and preprocessing the dataset
        -	[SenseLab](https://github.com/sensein/senselab): processing audio files for research tasks
        """
    )
