import streamlit as st
from sessionstates import util

def stable_income_page():
    st.title("Quality of income and clientbase")

    #question name
    util.ask_initial_questions("stable_income_question")

    #rule name
    util.next_page_button("company_has_stable_income")