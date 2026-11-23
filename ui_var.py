import streamlit as st
from master_ingredient_list import MASTER_INGREDIENTS

AVAILABLE_UNITS = ["kg", "g"]


def render_main_ui():
    """Render the main page header and primary workspace area."""
    st.title("Meal Planning App")


def render_side_bar():
    """Render sidebar settings for meal count and default pantry units."""
    st.sidebar.header("Your Profile and Settings")

    # Choose whether to pick the meal count with a slider or an exact number box
    input_mode = st.sidebar.selectbox(
        "How do you want to choose meal count?",
        ["Slider", "Number Value"],
        key="meal_count_input_mode",
    )

    # Set a safe default in case an unexpected option ever occurs
    meal_count = 0

    if input_mode == "Slider":
        meal_count = st.sidebar.slider(
            "Choose how many meals are planned",
            min_value=0,
            max_value=20,
            value=0,
            key="meal_count_slider",
        )
    elif input_mode == "Number Value":
        meal_count = st.sidebar.number_input(
            "Choose how many meals are planned",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key="meal_count_number",
        )
    else:
        st.sidebar.warning("Please choose how many meals you want.")

    # Choose the default weight unit used for new pantry items
    default_unit = st.sidebar.selectbox(
        "Default pantry unit",
        options=AVAILABLE_UNITS,
        key="default_pantry_unit",
    )

    return meal_count, default_unit


def render_pantry_ui(default_unit):
    """Render checkboxes and amount inputs for ingredients currently in the pantry."""
    st.sidebar.subheader("Pantry ingredients")

    # Ensure default_unit is valid; fall back to "kg" if something unexpected is passed
    if default_unit not in AVAILABLE_UNITS:
        default_unit = "kg"

    default_unit_index = AVAILABLE_UNITS.index(default_unit)
    pantry = {}

    for ingredient in MASTER_INGREDIENTS:
        is_owned = st.sidebar.checkbox(
            label=ingredient,
            key=f"pantry_owned_{ingredient}",
        )

        # Skip quantity/unit fields unless the user checked this ingredient
        if not is_owned:
            continue

        quantity = st.sidebar.number_input(
            label=f"{ingredient} quantity",
            min_value=0.0,
            max_value=9999.0,
            value=0.0,
            step=0.1,
            key=f"pantry_qty_{ingredient}",
        )

        unit = st.sidebar.selectbox(
            label=f"{ingredient} unit",
            options=AVAILABLE_UNITS,
            index=default_unit_index,
            key=f"pantry_unit_{ingredient}",
        )

        pantry[ingredient] = {
            "quantity": quantity,
            "unit": unit,
        }

    return pantry