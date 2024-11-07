import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

# Set page config
st.set_page_config(page_title="Acid Base Titration", layout="centered")

# Title
st.title("🌊 Acid Base Titration 🌡️")

# Display a brief description
st.markdown("### Simulate the titration of HCl with NaOH. Press 'Start Experiment' to begin!")

# Visuals for NaOH in Burette and HCl in Conical Flask
st.subheader("Setup")
st.markdown("""
1. **NaOH in the Burette**  
   The burette is filled with sodium hydroxide (NaOH) solution.
   
2. **HCl in the Conical Flask**  
   The conical flask contains hydrochloric acid (HCl) with a few drops of phenolphthalein indicator.
""")

# Start Experiment button
if st.button("Start Experiment"):
    # HTML to simulate animation of NaOH being added to HCl
    st.markdown("""
    <div style="text-align: center;">
        <h3>Adding NaOH to HCl...</h3>
        <div style="background-color: lightblue; padding: 20px; border-radius: 10px;">
            <p style="animation: changeColor 5s infinite;">Color Change Simulation</p>
        </div>
        <style>
        @keyframes changeColor {
            0% {color: red;}
            50% {color: pink;}
            100% {color: clear;}
        }
        </style>
    </div>
    """, unsafe_allow_html=True)

    # Simulating pH change
    volume_naoh = np.linspace(0, 25, 100)  # Volume of NaOH added
    pH = np.array([1 + 13 * (v / 25) for v in volume_naoh])  # Simulating pH change

    # Plotting the pH curve
    st.subheader("Titration Curve")
    fig, ax = plt.subplots()
    ax.plot(volume_naoh, pH, label="pH vs Volume NaOH", color="blue")
    ax.axhline(y=7, color='r', linestyle='--', label="End Point (pH 7)")
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    ax.set_title("pH vs Volume of NaOH Added")
    ax.legend()
    st.pyplot(fig)

    st.markdown("### Experiment Complete!")
