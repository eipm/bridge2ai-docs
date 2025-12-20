import streamlit as st

def data_pre_processing_page(tab_name):
    st.markdown(
        """
        The raw audio files and the questionnaire data retrieved from ReproSchema-UI or exported from REDCap were converted to be compliant with the [Brain Imaging Data Structure v1.9.0](https://bids-specification.readthedocs.io/en/v1.9.0/).

        **Pediatric data:** Pediatric data collected through ReproSchema-UI is extracted and transformed into REDCap format, and subsequently converted to the Brain Imaging Data Structure (BIDS).

        The folder structure for the dataset is as follows:

        ```
        b2ai-voice-audio

        ├── CHANGES.md
        ├── README.md
        ├── dataset_description.json
        ├── phenotype
            ├── confounders
            │   ├── confounders.json
            │   └── confounders.tsv
            ├── demographics
            │   ├── demographics.json
            │   └── demographics.tsv
            ├── diagnosis
            │   ├── adhd_adult.json
            │   ├── adhd_adult.tsv
            │   ├── airway_stenosis.json
            │   ├── airway_stenosis.tsv
            │   ├── amyotrophic_lateral_sclerosis.json
            │   ├── amyotrophic_lateral_sclerosis.tsv
            │   ├── anxiety.json
            │   ├── anxiety.tsv
            │   ├── benign_lesions.json
            │   ├── benign_lesions.tsv
            │   ├── bipolar_disorder.json
            │   ├── bipolar_disorder.tsv
            │   ├── cognitive_impairment.json
            │   ├── cognitive_impairment.tsv
            │   ├── control.json
            │   ├── control.tsv
            │   ├── copd_and_asthma.json
            │   ├── copd_and_asthma.tsv
            │   ├── depression.json
            │   ├── depression.tsv
            │   ├── glottic_insufficiency.json
            │   ├── glottic_insufficiency.tsv
            │   ├── laryngeal_cancer.json
            │   ├── laryngeal_cancer.tsv
            │   ├── laryngeal_dystonia.json
            │   ├── laryngeal_dystonia.tsv
            │   ├── laryngitis.json
            │   ├── laryngitis.tsv
            │   ├── muscle_tension_dysphonia.json
            │   ├── muscle_tension_dysphonia.tsv
            │   ├── parkinsons_disease.json
            │   ├── parkinsons_disease.tsv
            │   ├── precancerous_lesions.json
            │   ├── precancerous_lesions.tsv
            │   ├── psychiatric_history.json
            │   ├── psychiatric_history.tsv
            │   ├── ptsd_adult.json
            │   ├── ptsd_adult.tsv
            │   ├── unexplained_chronic_cough.json
            │   ├── unexplained_chronic_cough.tsv
            │   ├── unilateral_vocal_fold_paralysis.json
            │   └── unilateral_vocal_fold_paralysis.tsv
            ├── enrollment
            │   ├── eligibility.json
            │   ├── eligibility.tsv
            │   ├── enrollment_form.json
            │   ├── enrollment_form.tsv
            │   ├── participant.json
            │   └── participant.tsv
            ├── questionnaire
            │   ├── custom_affect_scale.json
            │   ├── custom_affect_scale.tsv
            │   ├── dsm5_adult.json
            │   ├── dsm5_adult.tsv
            │   ├── dyspnea_index.json
            │   ├── dyspnea_index.tsv
            │   ├── gad7_anxiety.json
            │   ├── gad7_anxiety.tsv
            │   ├── leicester_cough_questionnaire.json
            │   ├── leicester_cough_questionnaire.tsv
            │   ├── panas.json
            │   ├── panas.tsv
            │   ├── phq9.json
            │   ├── phq9.tsv
            │   ├── productive_vocabulary.json
            │   ├── productive_vocabulary.tsv
            │   ├── vhi10.json
            │   ├── vhi10.tsv
            │   ├── voice_perception.json
            │   └── voice_perception.tsv
            └── task
                ├── acoustic_task.json
                ├── acoustic_task.tsv
                ├── harvard_sentences.json
                ├── harvard_sentences.tsv
                ├── random_item_generation.json
                ├── random_item_generation.tsv
                ├── recording.json
                ├── recording.tsv
                ├── session.json
                ├── session.tsv
                ├── stroop.json
                ├── stroop.tsv
                ├── voice_perception.json
                ├── voice_perception.tsv
                ├── voice_problem_severity.json
                ├── voice_problem_severity.tsv
                ├── winograd.json
                └── winograd.tsv
        └── sub-<participant_id>
            └── ses-<session_id>
               └── audio
                   ├── sub-<participant_id>_ses-<session_id>_task-<task_name>.wav
                   └── sub-<participant_id>_ses-<session_id>_task-<task_name>.json 
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

        The feature-only dataset provides AI-ready derivations from the raw audio. Features extracted include:
        -	OpenSmile eGeMaps features per audio file
        -	Parselmouth/Praat speech features for any speech tasks
        -	Speech intelligibility metrics for speech tasks
        Time-varying features:
        -   Torchaudio-based pitch contour, spectrograms, mel spectrogram, and MFCCs
        -   Speech Articulatory Coding (sparc)-based features including electromagnetic articulography (EMA) estimates, plus loudness, periodicity, and pitch measures
        -   Phonetic posteriorgrams (PPGs)

        The waveform-derived features are stored using two formats:
        1.	A fixed feature format that includes static features extracted from the entire waveform
        2.	A temporal format that varies for each audio file depending on the length of recording.

        The questionnaire features are collected and distributed in the phenotype folder format shown above. These can be used for cohort selection.

        **Methods of De-identification for v3.0.0**
        All direct identifiers were removed, as these would reveal the identity of the research participant. These include name, civic address, and social security numbers. Indirect identifiers were removed where these created a significant risk of causing participant re-identification, for example through their combination with other public data available on social media, in government registries, or elsewhere. These include select geographic or demographic identifiers, as well as some information about household composition or cultural identity. Non-identifying elements of data that revealed highly sensitive information, such as information about household income, mental health status, traumatic life experiences, and the like, were also removed.

        Raw audio transcripts were reviewed, and any audio recordings that contained potentially identifying information and external voices were removed from the release.

        All sensitive fields were removed from the dataset at this stage. These correspond to data elements encoded as sensitive (column name: "Identifier?") listed in the [REDCap data dictionary (CSV)](https://github.com/eipm/bridge2ai-redcap/blob/main/data/bridge2ai_voice_project_data_dictionary.csv).

        In addition, all spectrograms, MFCCs, Mel spectrograms, transcriptions, EMAs, and PPGs from open-response prompts are removed from the feature-only dataset.

        **Audit protocol**
        -	Generate missingness tables
        -	Check distributions and outliers
        -	For categorical responses, check against schema
        -   For audio tasks, run quality control metrics
        -	For waveforms:
            -	Check amount of silence
            -	Duration
            -	For speech, check produced speech relative to intended passage

        All processing is performed using these toolkits:
        -	[b2aiprep](https://github.com/sensein/b2aiprep): organizing and preprocessing the dataset
        -	[SenseLab](https://github.com/sensein/senselab): processing audio files for research tasks
        """
    )
