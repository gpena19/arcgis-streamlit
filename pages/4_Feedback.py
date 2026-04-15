import streamlit as st
import streamlit.components.v1 as components

st.title("💬 Feedback & Questions")

st.info("Your input helps improve this climate risk analysis project.")

components.iframe(
    "https://docs.google.com/forms/d/e/1FAIpQLSfjZG4f81WyrOLYzUORbAght2nU6JlBJZFgA91sqQMfKaXzCA/viewform?usp=publish-editor",
    height=800,
    scrolling=True
)