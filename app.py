import streamlit as st
import time

# Streamlit page configuration
st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="centered")

# Dynamic title with animation
st.title("🧪 Elephant Toothpaste Reaction")
st.write("A fun and colorful chemistry experiment simulation!")

# Beaker and Cylinder Setup
col1, col2 = st.columns(2)

# Display the setup: H₂O₂ and KI solution
col1.image("beaker_h2o2.png", caption="H₂O₂ Solution", width=150)  # Placeholder for H₂O₂ beaker image
col2.image("cylinder_ki.png", caption="30% KI Solution", width=150)  # Placeholder for KI cylinder image

# Button to Start Experiment
start_button = st.button("Start Experiment")

if start_button:
    # Step 1: Display Pouring Effect
    st.write("Pouring H₂O₂ into the KI solution...")
    time.sleep(1)  # Pause to simulate pouring

    # Step 2: Show Reaction and Foam Animation
    st.write("🎉 The reaction begins!")
    st.image("foam_sequence_1.png", width=250)  # Start of foam sequence image
    time.sleep(1)
    st.image("foam_sequence_2.png", width=300)  # Mid foam sequence image
    time.sleep(1)
    st.image("foam_sequence_3.png", width=350)  # Full eruption foam image

    # Display the Chemical Equation
    st.write("**Chemical Equation:** 2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")

    # Optional Ingredients Note
    st.write("📝 **Note:** For a more colorful reaction, you can add food coloring to the H₂O₂. "
             "Adding liquid soap will help trap the oxygen, creating even more foam!")
