import json
import streamlit as st

questions = json.load(open("data/questions.json", 'r'))
properties = json.load(open("data/properties.json", "r"))
rules = json.load(open("data/rules.json", "r"))
final_rule = json.load(open("data/final_rule.json"))