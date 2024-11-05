import streamlit as st
import time

# Define title
st.title("Elephant Toothpaste Reaction")

# Display initial setup with beaker and cylinder using simple text placeholders
st.write("**Reaction Setup:**")
st.write("Beaker with **H₂O₂** solution (half-filled)")
st.write("Cylinder with **KI** solution (half-filled)")

# Placeholder for updates in the experiment
reaction_placeholder = st.empty()

# Add the Start Experiment button
start_experiment = st.button("Start Experiment")

# Run the experiment sequence if the button is clicked
if start_experiment:
    # Step 1: Simulate pouring H₂O₂ into the cylinder
    reaction_placeholder.write("**Step 1:** Pouring the H₂O₂ solution from the beaker into the cylinder...")
    time.sleep(2)

    # Step 2: Begin reaction, display initial reaction
    reaction_placeholder.write("**Step 2:** Reaction begins! The solution in the cylinder starts to bubble...")
    time.sleep(2)

    # Step 3: Simulate the dramatic foaming reaction
    reaction_placeholder.write("**Step 3:** A huge burst of foam erupts from the cylinder, creating a colorful explosion!")
    time.sleep(2)

    # Step 4: Display the chemical equation
    st.write("**Chemical Equation:**")
    st.latex(r"2 \, \text{H}_2\text{O}_2 (aq) \rightarrow 2 \, \text{H}_2\text{O} (l) + \text{O}_2 (g)")

    # Step 5: Provide an additional note about optional additions
    st.write("**Note:** Adding food coloring and liquid soap to the solution can make the reaction even more colorful and foamy.")

# Option to rerun experiment by clicking "Start Experiment" again
st.write("Click 'Start Experiment' again to repeat the reaction.")
