# import json
# import sys
# import data

# properties = data.properties
# questions = data.questions
# rules = data.rules

# currency = properties["currency"]

# currency_names = []
# for property in currency:
#     currency_names.append(property)
#     print(property, properties["currency"][property]["stability"])

def printQuestionsPage():
    # Prints all question of the current page, included all different types and options
    for qIdx, question_str in enumerate(questions["currency_page"]):#["currency_question"]):
        question = questions["currency_page"][question_str]
        print(question["type"])
        match question["type"]:
            case "radio":
                options = question["options"]
                prompt = question["prompt"]
                print(prompt)
                for str in options:
                    print(str, options[str])

def printQuestionsNormalLoop(question_name_page):
    for question_str in questions[question_name_page]:                          #loop through all questions
        question = questions[question_name_page][question_str]                  #set question object
        print(question_str)
            
def printRules():
    #prints all rules and its options
    for rules_str in rules:
        properties = rules[rules_str]
        for property in properties:
            value = properties[property]
            print(value[0], value[1])
            comparison_sign = value[0]
            match comparison_sign:
                case "==":
                    print("== case")
                case ">":
                    print("> case")
                case "<":
                    print("< case")

def test_dict():
    coin_dict = {'Euro': 10, 'Bri-ish pound': 10, 'Venezueloan bolivar': 2}
    print("EUro has value: ", coin_dict['Euro'])

def get_desired_page(json_data):
    #1: for each rule, if one of it's properties is not in the session_state
    #   then that belonging page where the question is asked, is the desired page
    #   TODO: if all rules are done, the final page with outcome should be the desired page
    print("get desired page is requested")
    for rules_str in rules:
        for property_str in rules[rules_str]:
            if (json_data[property_str] == None):
                print(property_str)

def update_rule(jdata, rule_str):
    #   update the rules in the session_state according to its properties
    rule = True
    for property_str in rules[rule_str]:
        current_value = jdata[property_str]
        threshold_value = rules[rule_str][property_str]['value']
        operator = rules[rule_str][property_str]['operator']
        match operator:
            case ">":
                if current_value < threshold_value:
                    rule = False
            case "<":
                if current_value > threshold_value:
                    rule = False
            case "==":
                if current_value != threshold_value:
                    rule = False
                    
    print("rule status: ", rule)
    
def loop_properties():
    jdata = {
        "properties" :
                [
                    {
                        "shared_pledges_property" : True,
                        "bank_account_pledge_property" : True,
                        "substancial_material_pledge_property" : False
                    },
                    {
                        "shared_pledges_property" : False,
                        "bank_account_pledge_property" : True,
                        "substancial_material_pledge_property" : True,
                        "substancial_material_loan_giver_property" : True
                    }
                ]
    }

    for i in jdata["properties"]:
        for prop in i:
            print(i[prop])

# jdata = {'coin_stability': 10, 'safe_country': 1, 'EBTIDA_property': 11, 'leverage_property': 3, 'private_loan_property': None, 'strong_agreements_property': None, 'issue_rating_property': None}
# update_rule(jdata, "EBITDA_compliant")
loop_properties()
print("program working and well")