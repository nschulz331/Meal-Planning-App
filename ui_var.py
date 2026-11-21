import streamlit as st 

def render_main_ui(): #the main ui 
    st.title("Meal Planning App")


def render_side_bar():
    # meal specifics, (meal amount units ext.
    st.sidebar.header("Your Profile and Settings") #header

    #meal amount config 

    meal_amount_requested_mode = st.sidebar.selectbox("Pick one", ["Slider", "Number Value"])
    if meal_amount_requested_mode == "Slider":
        meal_amount_requested = st.sidebar.slider("Choose How Many Meals Are Planned", 0, 20)
    else:
        if meal_amount_requested_mode == "Number Value":
            meal_amount_requested = st.sidebar.number_input("Chose How Many  Meals Are Planned", 0, 20)  
        else:
            st.sidebar.write("Please enter how many meals you want")

    #units for food variable setting
    units_for_food_ingrediants = st.sidebar.selectbox("Units", ["kilogram ( kg )", "gram ( g )"])


    st.write(meal_amount_requested,"This is how many meals will be made") #remove this after,  only for debug
    st.write(units_for_food_ingrediants,"this is how the meals will be calculated in ") #remove this after, only for debug