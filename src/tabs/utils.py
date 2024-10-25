import streamlit as st

# All tab pages are defined below
def coming_soon_message(tab_name):
    st.title('Bridge2AI Voice Dashboard')
    st.write(f"{tab_name} - Coming soon!")

    image_path = "images/Wave.png"
    st.image(image_path, caption='', use_column_width=True)
