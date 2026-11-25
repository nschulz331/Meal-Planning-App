import streamlit as st
from ui_var import render_main_ui, render_pantry_ui, render_side_bar

st.set_page_config(page_title="Meal Planner App", layout="wide") # sets the page name on browser


render_main_ui()
meal_amount_requested, units_for_food_ingredients = render_side_bar()
pantry = render_pantry_ui(units_for_food_ingredients)

st.write(meal_amount_requested, "This is how many meals will be made")
st.write(units_for_food_ingredients, "Default pantry unit")
st.write("Pantry ingredients:", pantry)
