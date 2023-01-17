import json
import streamlit as st
import data
from sessionstates import util

questions = data.questions

def ebitda():
    st.title("Calculating the EBITDA")

    # ebitda = st.text_input(questions["EBITDA_page"]["EBITDA_question"]["prompt"])
    # st.write("---")
    # leverage = st.text_input(questions["EBITDA_page"]["leverage_question"]["prompt"])
    # st.write("given ebitda: ", ebitda)
    # st.write("given leverage: ", leverage)

    util.ask_initial_questions("EBITDA_page")

    util.next_page_button("EBITDA_compliant")
    
