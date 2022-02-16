import streamlit as st
from hr_analytics_functions import *

st.sidebar.image('https://miro.medium.com/max/512/0*0V-xtrNNok_YAp_k', width=250)
st.sidebar.header('HR Analytics: Job Change of Data Scientists')
st.sidebar.markdown('Prediction who will move to a new job')


menu = st.sidebar.radio(
    "Menu:",
    ("Intro", "Data", "Analysis", "Pivot Tables", "Classification Model"),
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Project Submitted By: Farrukh Wajahat Ullah and Vaseem Shuaib')
st.sidebar.write('Github Repositories:')
st.sidebar.write('[Farrukh Github Repository Link](https://github.com/Farrukh-Ullah/Python-programming-project-UNIVR)')
st.sidebar.write('[Vaseem Github Repository Link](https://github.com/Ne04ever/Intern_classification)')
if menu == 'Intro':
    set_home()
elif menu == 'Data':
    set_data()
elif menu == 'Analysis':
    set_analysis()
elif menu == 'Pivot Tables':
    set_Piyottbl()
elif menu == 'Classification Model':
    set_classmod()
