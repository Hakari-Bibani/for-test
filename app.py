import streamlit as st
import time

# Title for the experiment
st.title("Elephant Toothpaste Reaction")

# Introduction and placeholders for beaker and cylinder
st.write("## Experiment Setup:")
beaker_placeholder = st.empty()
cylinder_placeholder = st.empty()
reaction_placeholder = st.empty()
equation_placeholder = st.empty()
note_placeholder = st.empty()

# Draw initial setup with beaker and cylinder
def setup_experiment():
    with beaker_placeholder.container():
        st.write("### Beaker (H₂O₂ Solution)")
        st.markdown("<div style='text-align: center;'>🧪 H₂O₂ (Pale Blue Solution)</div>", unsafe_allow_html=True)
    with cylinder_placeholder.container():
        st.write("### Cylinder (KI Solution)")
        st.markdown("<div style='text-align: center;'>🥛 KI (Light Grey Solution)</div>", unsafe_allow_html=True)

# Animation to mimic pouring reaction
def pouring_animation():
    beaker_placeholder.empty()  # Clear initial setup
    reaction_placeholder.empty()
    cylinder_placeholder.empty()

    # Display a tilted beaker to simulate pouring
    with beaker_placeholder.container():
        st.markdown("<div style='text-align: center; transform: rotate(-45deg);'>🧪➡️</div>", unsafe_allow_html=True)
    time.sleep(1)

    # Show foam explosion effect
    reaction_placeholder.markdown("<div style='font-size: 80px; text-align: center;'>🌋💥🎉</div>", unsafe_allow_html=True)
    time.sleep(2)

# Reset experiment for another run
def reset_experiment():
    reaction_placeholder.empty()
    equation_placeholder.empty()
    note_placeholder.empty()
    setup_experiment()

# Display initial setup
setup_experiment()

# Start Experiment Button
if st.button("Start Experiment"):
    pouring_animation()
    
    # Show chemical equation after reaction
    equation_placeholder.write("**Chemical Equation:** 2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")
    
    # Note about optional additions
    note_placeholder.info("Optional: Add food coloring or liquid soap for a more colorful foam effect!")

# Reset for repeatable experiment
st.button("Repeat Experiment", on_click=reset_experiment)
