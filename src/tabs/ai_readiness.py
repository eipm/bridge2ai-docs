import streamlit as st
# from tabs.utils import coming_soon_message
from tabs.utils import create_html_table
from tabs.utils import create_html_table_span_col_row

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
  
        </style>
        <table>
            <caption style="caption-side: top; text-align: left; font-weight: bold; font-size: 1.2em;">
                Precision Public Health (Voice) - Current Rating
            </caption>
            <tr>
                <th colspan="2">Criterion</th>
                <th>Criterion met? (Y=1; N=0)</th>
                <th>Total Score for Criterion (%)</th>
            </tr>
            <tr>
                <td rowspan="4">FAIRness (0)</td>
                <td>Findable (0.a)</td>
                <td>1</td>
                <td rowspan="4">100</td>
            </tr>
            <tr>
                <td>Accessible (0.b)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Interoperable (0.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Reusable (0.d)</td>
                <td>1</td>
            </tr>
            <tr>
                <td rowspan="4">Provenance (1)</td>
                <td>Transparent (1.a)</td>
                <td>1</td>
                <td rowspan="4">100</td>
            </tr>
            <tr>
                <td>Traceable (1.b)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Interpretable (1.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Key actors identified (1.d)</td>
                <td>1</td>
            </tr>
            <tr>
                <td rowspan="5">Characterization (2)</td>
                <td>Semantics (2.a)</td>
                <td>1</td>
                <td rowspan="5">80</td>
            </tr>
            <tr>
                <td>Statistics (2.b)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Standards (2.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Potential Sources of Bias (2.d)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Data Quality (2.e)</td>
                <td>0</td>
            </tr>
            <tr>
                <td rowspan="3">Pre-model explainability (3)</td>
                <td>Data documentation templates (3.a)</td>
                <td>1</td>
                <td rowspan="3">100</td>
            </tr>
            <tr>
                <td>Fit for purpose (3.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Verifiable (3.d)</td>
                <td>1</td>
            </tr>
            <tr>
                <td rowspan="4">Ethics (4)</td>
                <td>Ethically acquired (4.a)</td>
                <td>1</td>
                <td rowspan="4">100</td>
            </tr>
            <tr>
                <td>Ethically managed (4.b)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Ethically disseminated (4.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Secure (4.d)</td>
                <td>1</td>
            </tr>
            <tr>
                <td rowspan="4">Sustainability (5)</td>
                <td>Persistent (5.a)</td>
                <td>1</td>
                <td rowspan="4">50</td>
            </tr>
            <tr>
                <td>Domain-appropriate (5.b)</td>
                <td>0</td>
            </tr>
            <tr>
                <td>Well-governed (5.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Associated (5.d)</td>
                <td>0</td>
            </tr>
            <tr>
                <td rowspan="4">Computability (6)</td>
                <td>Standardized (6.a)</td>
                <td>1</td>
                <td rowspan="4">75</td>
            </tr>
            <tr>
                <td>Computational Accessibility (6.b)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Portable (6.c)</td>
                <td>1</td>
            </tr>
            <tr>
                <td>Contextualized (6.d)</td>
                <td>0</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True
    )
    
    # st.markdown(
    #     """
    #         <table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
    #         style='border-collapse:collapse;mso-table-layout-alt:fixed;mso-yfti-tbllook:
    #         1696;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
    #         <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.25pt'>
    #         <td width=167 valign=bottom style='width:125.6pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><o:p>&nbsp;</o:p></p>
    #         </td>
    #         <td width=243 valign=bottom style='width:181.9pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><o:p>&nbsp;</o:p></p>
    #         </td>
    #         <td width=106 valign=bottom style='width:79.75pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><o:p>&nbsp;</o:p></p>
    #         </td>
    #         <td width=108 valign=bottom style='width:80.75pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><o:p>&nbsp;</o:p></p>
    #         </td>
    #         </tr>
    #         <tr style='mso-yfti-irow:1;height:14.25pt'>
    #         <td width=624 colspan=4 valign=bottom style='width:6.5in;border:none;
    #         border-bottom:solid black 1.0pt;mso-border-bottom-alt:solid black .5pt;
    #         background:#FEF2CB;padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><a name="OLE_LINK3"></a><a
    #         name="OLE_LINK4"><span style='mso-bookmark:OLE_LINK3'><b><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>Precision Public Health (Voice) - </span></b></span></a><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><b><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:blue'>Current Rating</span></b><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:2;height:14.25pt'>
    #         <td width=410 colspan=2 style='width:307.5pt;border:solid black 1.0pt;
    #         border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><a
    #         name="OLE_LINK1"></a><a name="OLE_LINK2"><span style='mso-bookmark:OLE_LINK1'><b><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>Criterion</span></b><o:p></o:p></span></a></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><b><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>Criterion met? (Y=1; N=0)</span></b><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=108 style='width:80.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-left-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><b><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>Total Score for Criterion (%)</span></b><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:3;height:57.0pt'>
    #         <td width=167 rowspan=4 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span class=SpellE><span style='font-size:
    #         11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:Calibri;
    #         color:black'>FAIRness</span></span></span></span></span></span><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'> (0)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Findable
    #         (0.a)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=108 rowspan=4 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>100</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:4;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Accessible
    #         (0.b)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:5;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Interoperable
    #         (0.c)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:6;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Reusable
    #         (0.d)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:7;height:57.0pt'>
    #         <td width=167 rowspan=4 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Provenance
    #         (1)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='mso-bookmark:OLE_LINK2'><span
    #         style='mso-bookmark:OLE_LINK1'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Transparent
    #         (1.a)</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         <td width=108 rowspan=4 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-bottom-alt:solid black .25pt;mso-border-right-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>100</span><o:p></o:p></span></span></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='mso-bookmark:OLE_LINK2'><span style='mso-bookmark:OLE_LINK1'></span></span></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:8;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Traceable
    #         (1.b)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:9;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Interpretable
    #         (1.c)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:10;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Key actors identified
    #         (1.d)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:11;height:71.25pt'>
    #         <td width=167 rowspan=5 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:71.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Characterization
    #         (2)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:71.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Semantics
    #         (2.a)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:71.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=108 rowspan=5 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-bottom-alt:solid black .25pt;mso-border-right-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:71.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>80</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:12;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Statistics
    #         (2.b)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:13;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Standards
    #         (2.c)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:14;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Potential
    #         Sources of Bias (2.d)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:15;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Data
    #         Quality (2.e)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>0</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:16;height:42.75pt'>
    #         <td width=167 rowspan=3 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:42.75pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Pre-model
    #         explainability (3)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:42.75pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Data
    #         documentation templates (3.a)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:42.75pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=108 rowspan=3 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-bottom-alt:solid black .25pt;mso-border-right-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:42.75pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>100</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:17;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Fit for purpose
    #         (3.c)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:18;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Verifiable
    #         (3.d)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:19;height:57.0pt'>
    #         <td width=167 rowspan=4 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Ethics (4)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Ethically
    #         acquired (4.a)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=108 rowspan=4 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-bottom-alt:solid black .25pt;mso-border-right-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>100</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:20;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Ethically
    #         managed (4.b)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:21;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Ethically
    #         disseminated (4.c)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:22;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Secure
    #         (4.d)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:23;height:57.0pt'>
    #         <td width=167 rowspan=4 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Sustainability
    #         (5)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Persistent
    #         (5.a)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=108 rowspan=4 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-bottom-alt:solid black .25pt;mso-border-right-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>50</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:24;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Domain-appropriate
    #         (5.b)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>0</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:25;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Well-governed
    #         (5.c)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:26;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Associated
    #         (5.d)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>0</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:27;height:57.0pt'>
    #         <td width=167 rowspan=4 style='width:125.6pt;border-top:none;border-left:
    #         solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
    #         mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .25pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Computability
    #         (6)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:57.0pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Standardized
    #         (6.a)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=108 rowspan=4 style='width:80.75pt;border-top:none;border-left:
    #         none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
    #         mso-border-left-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
    #         mso-border-bottom-alt:solid black .25pt;mso-border-right-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:57.0pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>75</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:28;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Computational
    #         Accessibility (6.b)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:29;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Portable
    #         (6.c)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>1</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         <tr style='mso-yfti-irow:30;mso-yfti-lastrow:yes;height:14.25pt'>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=243 style='width:181.9pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
    #         solid black .5pt;mso-border-right-alt:solid black .5pt;padding:0in 5.4pt 0in 5.4pt;
    #         height:14.25pt'>
    #         <p class=MsoNormal><span style='mso-bookmark:OLE_LINK4'><span
    #         style='mso-bookmark:OLE_LINK3'><span style='font-size:11.0pt;font-family:
    #         "Calibri",sans-serif;mso-fareast-font-family:Calibri;color:black'>Contextualized
    #         (6.d)</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         <td width=106 style='width:79.75pt;border-top:none;border-left:none;
    #         border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
    #         solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
    #         padding:0in 5.4pt 0in 5.4pt;height:14.25pt'>
    #         <p class=MsoNormal align=center style='text-align:center'><span
    #         style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'><span
    #         style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
    #         Calibri;color:black'>0</span><o:p></o:p></span></span></p>
    #         </td>
    #         <span style='mso-bookmark:OLE_LINK4'><span style='mso-bookmark:OLE_LINK3'></span></span>
    #         </tr>
    #         </table>
    #     """,
    #     unsafe_allow_html=True
    # )
    # df = pd.DataFrame(
    # np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
    # )

    # st.table(df)

    # MOVE TO "SECTION: Collection methods"  
    csv_file_path = "src/tabs/tables/Disease_cohort_inclusion_exclusion_criteria.csv"
    caption = 'Table 1.  Disease cohort inclusion/exclusion criteria and validation methods'
    create_html_table(csv_file_path, caption)

    csv_file_path = "src/tabs/tables/Acoustic_Tasks_Protocol.csv"
    caption = 'Table 2. Acoustic Tasks in Protocol'
    create_html_table(csv_file_path, caption)

    csv_file_path = "src/tabs/tables/Validated_Questionnaires.csv"
    caption = 'Table 3 Validated Questionnaires integrated into App'
    create_html_table(csv_file_path, caption)
    
