import json
import streamlit as st
import data
from sessionstates import util

questions = data.questions

def credit_rating_page():
    st.title("Credit ratings")

    util.ask_initial_questions("credit_rating")

    util.next_page_button("sufficient_credit_rating")