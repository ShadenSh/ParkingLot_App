import streamlit as st
import pandas as pd
import numpy as np


st.title('Parking Lot Monitoring')
text1="""This web app aims to track vacant parking slots in Elmotnby Street in Haifa. Developed by Shaden Sharif as part of the "Projects" course in the CS department at the University of Haifa."""
text2="""For real-time tracking of vacant parking slots on Al Motnby Street in Haifa, please open the sidebar and navigate to 'Al-motnbyStreet'."""

st.markdown(f"#### {text1}")
st.image('Images/HaifaCity.jpeg',caption='Haifa City, source:https://www.touristisrael.com/haifa/33404/' , width=950)
#st.write('This web app aims to track vacant parking slots in Elmotnby Street in Haifa.')
#st.write('Developed by Shaden Sharif as part of the "Projects" course in the CS department at the University of Haifa.')

#st.write('For real-time tracking of vacant parking slots on El Motnby Street in Haifa, please open the sidebar and navigate to "elmotnbyStreet".')
st.markdown(":car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car:")
st.markdown(f"### {text2}")
st.markdown(":car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car::car:")
