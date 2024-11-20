import streamlit as st
from tabs.utils import create_html_table

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
    lt, cent, rt = st.columns([1,3,1], gap="small")
    with cent:
        st.image(image_path, use_container_width=True)

    # Add Table
    st.markdown(
        """        
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid !important;
            padding: 4px;
            text-align: left;
        }
        
        table .center-align {
            text-align: center;
        }
  
        </style>
        <table>
            <caption style="caption-side: top; text-align: left; font-weight: bold; font-size: 1.2em;">
                Table 4 - Precision Public Health (Voice) - Current Rating
            </caption>
            <tr>
                <th colspan="2">Criterion</th>
                <th>Criterion met? (Y=1; N=0)</th>
                <th>Total Score for Criterion (%)</th>
            </tr>
            <tr>
                <td rowspan="4">FAIRness (0)</td>
                <td>Findable (0.a)</td>
                <td class="center-align">1</td>
                <td rowspan="4" class="center-align">100</td>
            </tr>
            <tr>
                <td>Accessible (0.b)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Interoperable (0.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Reusable (0.d)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td rowspan="4">Provenance (1)</td>
                <td>Transparent (1.a)</td>
                <td class="center-align">1</td>
                <td rowspan="4" class="center-align">100</td>
            </tr>
            <tr>
                <td>Traceable (1.b)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Interpretable (1.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Key actors identified (1.d)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td rowspan="5">Characterization (2)</td>
                <td>Semantics (2.a)</td>
                <td class="center-align">1</td>
                <td rowspan="5" class="center-align">80</td>
            </tr>
            <tr>
                <td>Statistics (2.b)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Standards (2.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Potential Sources of Bias (2.d)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Data Quality (2.e)</td>
                <td class="center-align">0</td>
            </tr>
            <tr>
                <td rowspan="3">Pre-model explainability (3)</td>
                <td>Data documentation templates (3.a)</td>
                <td class="center-align">1</td>
                <td rowspan="3" class="center-align">100</td>
            </tr>
            <tr>
                <td>Fit for purpose (3.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Verifiable (3.d)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td rowspan="4">Ethics (4)</td>
                <td>Ethically acquired (4.a)</td>
                <td class="center-align">1</td>
                <td rowspan="4" class="center-align">100</td>
            </tr>
            <tr>
                <td>Ethically managed (4.b)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Ethically disseminated (4.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Secure (4.d)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td rowspan="4">Sustainability (5)</td>
                <td>Persistent (5.a)</td>
                <td class="center-align">1</td>
                <td rowspan="4" class="center-align">50</td>
            </tr>
            <tr>
                <td>Domain-appropriate (5.b)</td>
                <td class="center-align">0</td>
            </tr>
            <tr>
                <td>Well-governed (5.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Associated (5.d)</td>
                <td class="center-align">0</td>
            </tr>
            <tr>
                <td rowspan="4">Computability (6)</td>
                <td>Standardized (6.a)</td>
                <td class="center-align">1</td>
                <td rowspan="4" class="center-align">75</td>
            </tr>
            <tr>
                <td>Computational Accessibility (6.b)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Portable (6.c)</td>
                <td class="center-align">1</td>
            </tr>
            <tr>
                <td>Contextualized (6.d)</td>
                <td class="center-align">0</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True
    )
