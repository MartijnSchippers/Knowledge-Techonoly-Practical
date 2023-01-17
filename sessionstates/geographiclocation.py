import json
import streamlit as st
import data
from sessionstates import util

questions = data.questions #json.load(open("questions.json", 'r'))
properties = data.properties#json.load(open("properties.json", "r"))
rules = data.rules#json.load(open("rules.json", "r"))

def geo_location_page():
    st.title("Geographic location")
    
    util.ask_initial_questions("geographic_location_page")

    util.next_page_button("it_is_a_safe_country")