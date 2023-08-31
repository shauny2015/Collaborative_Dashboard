import streamlit as st


st.title("Idea Submission Form")
st.header('Study day ideas')


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
