import streamlit as st
import data
import random

rules = data.rules
questions = data.questions
properties = data.properties

def ask_initial_questions(question_name_page):
    #   change the st so that all the initial questions are asked
    #   for all questions in a current page, ask them according to their type and options
    #   the answer should be saved by the value of the variable_to_chage property
    #   store the values in a temporary property

    #   DEBUGGIN ONLY:
    # print("properties: " , st.session_state['properties'])

    for question_str in questions[question_name_page]:                          #loop through all questions
        question = questions[question_name_page][question_str]                  #set question object
        match question["type"]:                                                 #cases for all kinds of questions
            case "checkbox":
                ask_checkbox_questions(question)
            case "radio":                                                       #in case a radio is required
                ask_radio_questions(question)
            case "select_box":
                ask_select_box(question)
            case "text_input":
                ask_text_box(question)

def ask_checkbox_questions(question):
    prompt = question["prompt"]
    checkbox = st.checkbox(prompt, key=prompt)                      #key = prompt so each question has a unique key
    state = False
    if checkbox:
        state = True
        ask_subquestion_if_available(question)
    sessionsstate_variable = get_variable_to_change(question)
    st.session_state.properties[sessionsstate_variable] = state

def ask_radio_questions(question):
    options = []
    for option in question["options"]:                              #appending all options
        options.append(option)
    sessionsstate_variable = get_variable_to_change(question)       #name of variable to store answer 
                                                                    #save answer in python temporarily
    answer_str = st.radio(question["prompt"], options)
    st.session_state.properties[sessionsstate_variable] = question["options"][answer_str]

def ask_select_box(question):
    options = []
    for option in question["options"]:                              #appending all options
        options.append(option)
    sessionsstate_variable = get_variable_to_change(question)
    answer_str = st.selectbox(question["prompt"], options)
    st.session_state['properties'][sessionsstate_variable] = question["options"][answer_str]

def ask_subquestion_if_available(question):
    if "subquestion" in question:
        subquestion = question["subquestion"]
        print("there is a subquestion detected")
        ask_checkbox_questions(subquestion)

    

def ask_text_box(question):
    sessionsstate_variable = get_variable_to_change(question)
    answer_str = st.text_input(question["prompt"])
    
    if answer_str == '':
        answer_int = 0
    else:
        answer_int = int(answer_str)
        
    st.session_state['properties'][sessionsstate_variable] = answer_int

def get_desired_rule():
    for main_rule_str in rules:
        if st.session_state.rules[main_rule_str] == None:
            return main_rule_str

def get_variable_to_change(question):
    #   return the variable that the questions database indicates to return
    return question["variable_to_change"]   

def get_random_key():
    return ''.join((random.choice('abcdxyzpqr') for i in range(20)))

def next_page_button(rule_str):
    #   This is the implementation of the 'next' button.
    #   It clears the temporary cache and stores it in the normal values
    #   It should redirect the user to another page, or it should
    #   direct the user to the current page.
    #   get_desired_page() determines the page the user will see
    st.markdown('---')
    if st.button('Next'):
        update_temporary_properties()
        update_rule(rule_str)
        #st.session_state['state'] = get_desired_page()
        st.experimental_rerun()

def initialize_properties_if_required():
    if 'properties' not in st.session_state.keys():
        initialize_properties()
        print("properties reinitialized")
        
def initialize_properties():
    #   set all properties of the user in the session to None.
    #   so there will be no running errors
    st.session_state.properties = {}
    st.session_state.temporary_properties = {}
    st.session_state.rules = {}

    #initialize properties and temporary properties
    for property_str in  properties:
        st.session_state.properties[property_str] = None
        st.session_state.temporary_properties[property_str] = None

    #initialize rules
    for rule_str in rules:
        rule = rules[rule_str]
        #add main rules
        st.session_state.rules[rule_str] = None

        #if a rule consists of multiple rules, then add those rules ass well
        if "rules" in rule.keys():
            for sub_rule_str in rule["rules"]:
                st.session_state.rules[sub_rule_str] = None
    #DEBUGGIN ONLY:
    # print("properties: ", st.session_state, '\n')
    # print("temporary properties: ", st.session_state.temporary_properties, '\n')
    # print("rules: ", st.session_state.rules, '\n')

def update_temporary_properties():
    for property in st.session_state.temporary_properties:
        prop_value = st.session_state.temporary_properties[property]
        #if there is a temporary property that is not None, set the value to non temporary
        #and reset the temporary value to None
        if prop_value != None:
            st.session_state.properties[property] = prop_value
            st.session_state.temporary_properties[property] = None

def update_rule(rule_str):
    #   update the rule in the session_state according to its properties in the
    #   st.session_state.temporary_properties
    rule = check_correctness_rule(rule_str)
    st.session_state['rules'][rule_str] = rule
    #DEBUGGING ONLY:
    # print(st.session_state.rules)

def check_correctness_rule(rule_str):
    #check if the give rule is correct by checking its value from the properties session

    #check for more advanced rules (which have subrules)
    if "rules" in rules[rule_str]:
        sub_rules = rules[rule_str]["rules"]
        for sub_rule_str in sub_rules:
            corr = check_correctness_subrule(sub_rules[sub_rule_str])
            if corr == False:
                return False
        return True
        
    #check for simple rules
    for property_chunk in rules[rule_str]["properties"]:
        corr = check__correctness_rule_properties_chunk(property_chunk)
        if corr == True:
            return True
    return False
            
def check_correctness_subrule(subrule):
    print(" \n subrule: ", subrule)
    for property_chunk in subrule["properties"]:
        corr = check__correctness_rule_properties_chunk(property_chunk)
        if corr == True:
            return True
    return False

def check__correctness_rule_properties_chunk(property_chunk):
    # based on the given the properties, check if the rule is correct
    for property_str in property_chunk:
        current_value = st.session_state.properties[property_str]
        threshold_value = properties[property_str]['value']
        operator = properties[property_str]['operator']
        print("\n value: ", current_value)
        if not (isinstance(current_value, int)):
            return False
        else:
            match operator:
                case ">":
                    if current_value > threshold_value:
                        return True
                case "<":
                    if current_value < threshold_value:
                        return True
                case "==":
                    if current_value == threshold_value:
                        return True
        return False
