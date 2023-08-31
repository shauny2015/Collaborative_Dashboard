import streamlit as st
from PIL import Image

# FMR logo on top - will adjust align later
st.image('https://www.fidelity.com/bin-public/060_www_fidelity_com/images/fidelity-logo-nav.png')
# Titles and headers
st.title("Fidelity AMT Learning Days")
st.header('Profile and Learning Objectives Submission Form')
st.caption('This tool will assist in finding associates with similar learning interests, enabling collaboration and the set up of study groups')
st.subheader('Please enter your details')

#init session state
if "ideasList" not in st.session_state:
    st.session_state.ideasList = []

# Input fields
userName = st.text_input("Your Name", "")
userEmail = st.text_input("Your email","")
userIdea = st.text_area("Your Ideas", "")

# Submit button
if st.button("Submit"):
    if userName and userIdea:
        st.success("Thank you for submitting your idea!")
        st.session_state.ideasList.append(f"{userName} : {userIdea}")
    else:
        st.warning("Please fill in both your name and ideas.")
 #display ideas back to the user

if st.session_state.ideasList:
    st.title("Ideas")
    for idea in st.session_state.ideasList:
        st.write(idea)
