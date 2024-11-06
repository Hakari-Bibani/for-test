import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Baking Soda and Vinegar Reaction")

# Initial Setup
st.subheader("Initial Setup")

# Beaker and Spoon Visualization
st.write("Imagine a beaker half-filled with a pale red solution labeled *CH₃COOH* (vinegar) and a spoon with a light gray powder labeled *NaHCO₃* (baking soda) above it.")

# Placeholder for animation
beaker_placeholder = st.empty()

# Animation Button
if st.button("Start Experiment"):
    # Simulate the reaction animation step-by-step
    for i in range(5):
        with beaker_placeholder.container():
            st.write("Pouring...")
            time.sleep(0.5)
        if i == 4:
            st.write("Reacting... 💥💨")
            time.sleep(1)
            break

    # Visual Representation of Reaction
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x) * np.exp(-0.1 * x) + np.random.normal(0, 0.1, len(x))
    ax.plot(x, y)
    ax.set_title("Reaction Simulated in 2D Format")

    st.pyplot(fig)

st.subheader("Reaction Outcome")

# Display the chemical equation
st.latex(r"NaHCO_3 (s) + CH_3COOH (aq) \rightarrow CO_2 (g) + H_2O (l) + NaCH_3COO (aq)")

# Ending Note
st.write("The rapid reaction releases carbon dioxide gas, causing the bubbly overflow!")
