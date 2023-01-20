import streamlit as st
import data
from sessionstates import util

final_rule = data.final_rule
rules = data.rules

def write_rule(rule_name):
    style = "color: #cc0f0f"
    # if not rule_is_correct:
    #     style = "body {color: #a7f146;}"
    st.write("<style>", style, "</style>", rule_name, unsafe_allow_html=True)
    # if not rule_is_correct:
    #     rule = False

def check_correctness_all_rules():
    for rule_str in final_rule:
        if st.session_state.rules[rule_str] != final_rule[rule_str]:
            write_rule(rules[rule_str]["incorrect_message"])
            return False
        write_rule(rules[rule_str]["correct_message"])
    return True

def results_page():
    #   This page draws a conclusion and lets the user know
    st.title("Conclusion")
    conclusion = "Conclusion: the loan should"

    #steps:
    #   Check all main rules for correctness according to final_rule
    #   If any rule does not comply with the final rule, then the conclusion is
    #   that the loan should not be granted.
    #   If all rules are accoring to the final rule model, then the conclusion
    #   is that the loan could be granted
    if not check_correctness_all_rules():
        conclusion += " not"
    conclusion += " be granted"
    
    st.write(conclusion)