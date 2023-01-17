import streamlit as st
from sessionstates import util

def interest_rate_risk_page():
    st.title("Interest rate risk")

    util.ask_initial_questions("average_spread_page")

    util.next_page_button("interest_rate_risk")