import json
import streamlit as st
import data
from sessionstates import util

questions = data.questions
properties = data.properties
rules = data.rules

def currency_page():
    st.title("Loan giving machine thing [TODO: make a name]")

    #give all initial questions
    util.ask_initial_questions("currency_page")

    #next page button
    util.next_page_button("currency_no_danger")