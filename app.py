import streamlit as st
from ui_var import render_side_bar, render_main_ui

st.set_page_config(page_title="Meal Planner App", layout="wide") # sets the page name on browser


render_main_ui()
render_side_bar()
