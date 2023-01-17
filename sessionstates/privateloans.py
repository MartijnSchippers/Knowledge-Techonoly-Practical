import json
import streamlit as st
import data

questions = data.questions

def private_loans():
    st.title("Priate loans")
    specific_questions = questions["private_loan_page"]
    st.radio(specific_questions["private_loan_question"]["prompt"], ['yes', 'no'])
    st.radio(specific_questions["strong_agreements_question"]["prompt"], ['yes', 'no'])