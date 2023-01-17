import streamlit as st
import data
from sessionstates import util

def exposure_page():
    st.title("Security rights")
    util.ask_initial_questions("exposure_page")
        
    util.next_page_button("good_exposure")