import streamlit as st
import time

# Title
st.title("Baking Soda and Vinegar Reaction")

# Initial Setup
st.subheader("Initial Setup")

# Description of Setup
st.write(
    "Below is a beaker half-filled with a pale red solution labeled **CH₃COOH** (vinegar). "
    "Above the beaker, there is a spoon filled with white powder labeled **NaHCO₃** (baking soda)."
)

# Visual Representation (static images or placeholders)
st.image("path_to_beaker_image.jpg", caption="Beaker with CH₃COOH (Vinegar)", use_column_width=True)
st.image("path_to_spoon_image.jpg", caption="Spoon with NaHCO₃ (Baking Soda)", use_column_width=True)

# Button to Start the Experiment
if st.button("Start Experiment"):
    st.write("Pouring the baking soda into the vinegar...")

    # Simulate the reaction step-by-step
    with st.spinner("Reacting..."):
        time.sleep(2)  # Delay to simulate the pouring

    st.success("Reaction Complete!")
    
    # Show Reaction Animation (you can add more complex animations if needed)
    st.write("A dramatic reaction occurs, with bubbles overflowing the beaker!")
    st.balloons()  # Simple celebratory animation
    
    # Chemical Equation
    st.subheader("Chemical Equation")
    st.latex(r"NaHCO_3 (s) + CH_3COOH (aq) \rightarrow CO_2 (g) + H_2O (l) + NaCH_3COO (aq)")

# Footer Note
st.write("The reaction produces carbon dioxide gas, causing the overflow of bubbles.")
