import streamlit as st

st.title("🎈  My new Streamlit app")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header ("Joyous Celebration")
name = st.text_input("Enter your name")
studymethod = st.selectbox("Studymethod",("Crammer", "Pre-Planner", "Memory Box"))
button = st.button("Diva?")


if button:
    with st.spinner("Loading your diva status"):
        if studymethod =="Crammer":
            st.write(F"{name}, You are Not a diva")
        elif studymethod == "Pre-Planner":
            st.write(f"{name}, You are a diva")
        elif studymethod == "Memory Box":
            st.write(f"{name}, You are almost a diva")