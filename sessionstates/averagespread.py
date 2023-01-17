import streamlit as st
from sessionstates import util

def average_spread_page():
    st.title("Interest rate risk")

    #question name
    util.ask_initial_questions("average_spread_page")

    #rule name
    util.next_page_button("average_spread_okay")