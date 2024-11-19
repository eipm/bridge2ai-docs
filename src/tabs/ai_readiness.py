import streamlit as st
# from tabs.utils import coming_soon_message

import pandas as pd
import numpy as np

def ai_readiness_page(tab_name):
    st.markdown(
        """
        For detailed descriptions of each criteria, please read: [https://www.biorxiv.org/content/10.1101/2024.10.23.619844v2](https://www.biorxiv.org/content/10.1101/2024.10.23.619844v2)
        """
    )

    # Add Figure
    image_path = "images/ai-readiness-figure-1.png"
    st.image(image_path, use_column_width=True)

    # Add Table
    
    # df = pd.DataFrame(
    # np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
    # )

    # st.table(df)