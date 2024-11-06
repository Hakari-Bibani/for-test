import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Set the page title and configure layout
st.set_page_config(page_title="Acid Base Titration", layout="centered")

# Title with moving animation effect
st.title("🌊 Acid Base Titration")

# Instructions and experiment setup
st.markdown("### Experiment Setup")
st.write("We have a setup where **NaOH** is in the burette, and **HCl** is in the conical flask.")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Titration_setup.png/450px-Titration_setup.png", 
         caption="Titration Setup (illustration for reference)")

# Button to start the experiment
if st.button("Start Experiment"):
    st.write("Adding **NaOH** to **HCl**...")

    # Animation of adding NaOH
    progress_bar = st.progress(0)
    animation_text = st.empty()

    for i in range(101):
        time.sleep(0.05)  # Simulate time for adding NaOH
        progress_bar.progress(i)
        animation_text.text(f"NaOH added: {i}%")
    
    st.write("The color of the solution has changed, indicating the end point!")

    # Plot the pH change
    st.write("### Titration Curve")
    volume_NaOH = np.linspace(0, 25, 100)
    pH = 7 + (10 * np.arctan((volume_NaOH - 12.5) / 2))  # Sigmoid curve representing pH change

    plt.figure(figsize=(8, 5))
    plt.plot(volume_NaOH, pH, label="pH vs Volume of NaOH", color="blue")
    plt.axhline(y=7, color='r', linestyle='--', label="Neutral pH")
    plt.axvline(x=12.5, color='g', linestyle='--', label="End Point")
    plt.xlabel("Volume of NaOH (mL)")
    plt.ylabel("pH")
    plt.title("Titration Curve of NaOH and HCl")
    plt.legend()
    plt.grid()

    st.pyplot(plt)

# Footer
st.write("**Note:** This is a simplified simulation of an acid-base titration.")
