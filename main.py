#local imports
from sessionstates.averagerating import average_rating_page
from sessionstates.averagespread import average_spread_page
from sessionstates.currency import currency_page
from sessionstates.contract_duration import contract_duraction_page
from sessionstates.geographiclocation import geo_location_page
from sessionstates.ebitda import ebitda
from sessionstates.esg import ESG_page
from sessionstates.exposurepage import exposure_page
from sessionstates.creditrating import credit_rating_page
from sessionstates.interestraterisk import interest_rate_risk_page
from sessionstates.lmamodel import LMA_model_page
from sessionstates.pagenotfound import page_not_found
from sessionstates.results_page import results_page
from sessionstates.stableincome import stable_income_page
from sessionstates.util import initialize_properties_if_required, get_desired_rule
import streamlit as st

#functions that belong to main.py
def view_desired_page():
    # Based on the rules that are not filled in, display the current page
    desired_rule = get_desired_rule()
    # print("rule name: ", rule_name)
    print(st.session_state.rules)
    match desired_rule:
        case "currency_no_danger":
            currency_page()
        case "it_is_a_safe_country":
            geo_location_page()
        case "EBITDA_compliant":
            ebitda()
        case "good_exposure":
            exposure_page()
        case "sufficient_credit_rating":
            credit_rating_page()
        case "sufficient_average_rating":
            average_rating_page()
        case "no_interest_rate_risk":
            interest_rate_risk_page()
        case "average_spread_okay":
            average_spread_page()
        case "LMA_model_correct":
            LMA_model_page()
        case "ESG_correct":
            ESG_page()
        case "valid_duration_contract":
            contract_duraction_page()
        case "company_has_stable_income":
            stable_income_page()
        case "results":
            results_page()
        case default:
            return page_not_found()

#set general streamlit configurations
st.set_page_config(
    page_title = "Project Martijn",
    layout='wide')

#initialize all outcomes of rules to be None (because there is no data)
initialize_properties_if_required()

#view the desired page
view_desired_page()