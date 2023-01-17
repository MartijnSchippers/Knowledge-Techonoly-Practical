import streamlit as st
from sessionstates import util

def LMA_model_page():
    st.title("LMA model")

    #question name
    util.ask_initial_questions("LMA_model_page")

    #rule name
    util.next_page_button("LMA_model_correct")