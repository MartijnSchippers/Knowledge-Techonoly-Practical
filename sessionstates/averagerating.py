
import streamlit as st
from sessionstates import util


def average_rating_page():
    st.title("Calculating average rating")

    util.ask_initial_questions("average_rating")

    util.next_page_button("sufficient_average_rating")