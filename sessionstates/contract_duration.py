import streamlit as st
from sessionstates import util

def contract_duraction_page():
    st.title("Duration of contract")

    #question name
    util.ask_initial_questions("duration_contract_question")

    #rule name
    util.next_page_button("valid_duration_contract")