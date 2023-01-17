import streamlit as st
import data
from sessionstates import util

# final_rule = data.final_rule
rules = data.rules

def check_correctness(rule_value, state_value, operator):
    match operator:
        case "==":
            if rule_value == state_value:
                return True
            return False
        case ">":
            if state_value > rule_value:
                return True
            return False
        case "<":
            if state_value < rule_value:
                return True
            return False

def write_rule(rule_name, rule_is_correct):
    style = "color: #cc0f0f"
    if not rule_is_correct:
        style = "body {color: #a7f146;}"
    st.write("<style>", style, "</style>", "The rule ", rule_name, " is ", rule_is_correct, unsafe_allow_html=True)
    if not rule_is_correct:
        rule = False

def results_page():
    #   At this stage, all the properties are already filled in
    #   Steps:
    #   For every rule, check every property
    #   Check for every property, if it complies with its values
    #   1 rule not true -> not a good investment
    #   all rules true -> good investment

    st.title("results should be displayed here")
    print(st.session_state)
    mainrule = True
    for rule_str in rules:              #check if rules are correct, to obtain the main rule correctness
        rule = True
        #check if all properties are true accordign to their own needs
        for property_str in rules[rule_str]:
            property = rules[rule_str][property_str]
            operator = property["operator"]
            rule_value = property["value"]
            state_value = st.session_state['properties'][property_str]
            property_correct = check_correctness(rule_value, state_value, operator)

            if not property_correct:
                rule = False
        
        if rule == False:
            mainrule = False

        #write the rule
        write_rule(rule_str, rule)
        
    text = ""
    if (mainrule == False):
        text = "not"
    st.write("Conclusion: it is ", text, "recommended to give this loan")
    #     current_value = st.session_state['properties'][property_str]
    #     threshold_value = rules[rule_str][property_str]['value']
    #     operator = rules[rule_str][property_str]['operator']
    #     if not (isinstance(current_value, int)):
    #         rule = False
    #     else:
    #         match operator:
    #             case ">":
    #                 if current_value < threshold_value:
    #                     rule = False
    #             case "<":
    #                 if current_value > threshold_value:
    #                     rule = False
    #             case "==":
    #                 if current_value != threshold_value:
    #                     rule = False
    # st.session_state['rules'][rule_str] = rule
    # print(st.session_state['rules'])

    #steps:
    #