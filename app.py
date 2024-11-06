from main import retrieve_answer
import streamlit as st


st.title("Medical Q&A Chatbot")

# User input
user_question = st.text_input("Enter your medical question:")

if st.button("Get Answer"):
    answer = retrieve_answer(user_question)
    st.write("**Answer:**", answer)