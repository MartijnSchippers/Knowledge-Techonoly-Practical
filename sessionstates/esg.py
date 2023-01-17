import streamlit as st
from sessionstates import util

def ESG_page():
    st.title("ESG model")

    #question name
    util.ask_initial_questions("ESG_policy_in_use")

    #rule name
    util.next_page_button("ESG_correct")