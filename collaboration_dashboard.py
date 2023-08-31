import streamlit as st


st.title("Idea Submission Form")
st.header('Study day ideas')

#Ideas list
ideasList = []

# Input fields
userName = st.text_input("Your Name", "")
userIdeas = st.text_area("Your Ideas", "")

# Submit button
if st.button("Submit"):
    if userName and userIdeas:
        st.success("Thank you for submitting your idea!")
        ideasList.append(f"{userIdeas}")
    else:
        st.warning("Please fill in both your name and ideas.")
 #display ideas back to the user

if ideasList:
     st.listbox(ideasList)
