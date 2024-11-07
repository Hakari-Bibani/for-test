import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Set up the page configuration
st.set_page_config(page_title="Acid-Base Titration WebApp", layout="centered")

# Title with a simple moving effect using emojis
st.title("🌊 Acid-Base Titration Simulation 🌡️")

# Introduction and description
st.markdown("""
Welcome to the interactive Acid-Base Titration web app! Here, you will simulate the titration process by adding NaOH drop by drop into a solution of HCl in a conical flask. Let's see how the pH changes and observe the color change at the equivalence point.
""")

# Setup description
st.subheader("Setup")
st.markdown("""
- **NaOH in the Burette**: Sodium hydroxide (NaOH) solution is in the burette, ready to be added to the acid.
- **HCl in the Conical Flask**: Hydrochloric acid (HCl) with phenolphthalein indicator is in the conical flask. The solution is colorless initially.
""")

# Button to start the experiment
if st.button("Start Experiment"):
    # Simulate adding NaOH drop by drop with a progress bar
    st.subheader("Adding NaOH Drop by Drop...")
    progress_bar = st.progress(0)
    drop_text = st.empty()

    # Simulating the titration process
    for i in range(101):
        progress_bar.progress(i)
        if i < 50:
            drop_text.text("Adding NaOH... pH is increasing slightly (solution is still colorless).")
        elif i < 90:
            drop_text.text("Adding NaOH... pH is increasing rapidly (solution is turning faint pink).")
        else:
            drop_text.text("Adding NaOH... Approaching the end point (solution is pink).")
        time.sleep(0.05)  # Pause to simulate time taken for each drop

    st.success("Color change observed! Reached the equivalence point.")

    # Simulating pH change for the titration curve
    volume_naoh = np.linspace(0, 25, 100)  # Volume of NaOH added
    pH = np.array([1 + 13 * (v / 25) for v in volume_naoh])  # Simulated pH values

    # Plotting the titration curve
    st.subheader("Titration Curve")
    fig, ax = plt.subplots()
    ax.plot(volume_naoh, pH, label="pH vs Volume of NaOH", color="blue")
    ax.axhline(y=7, color='r', linestyle='--', label="End Point (pH 7)")
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    ax.set_title("pH vs Volume of NaOH Added")
    ax.legend()
    st.pyplot(fig)

    st.markdown("### Experiment Complete! The titration curve above shows how the pH changes as NaOH is added to HCl.")

# Manual titration control using a slider
st.subheader("Manual Titration Control")
volume_added = st.slider("Adjust the Volume of NaOH Added (mL)", 0, 25, 0)
current_pH = 1 + 13 * (volume_added / 25)  # Calculate current pH based on volume added
st.write(f"**Current pH:** {current_pH:.2f}")

# Descriptive updates based on pH value
if current_pH < 7:
    st.write("The solution is still acidic and colorless.")
elif current_pH == 7:
    st.write("The equivalence point has been reached! The solution turns faint pink.")
else:
    st.write("The solution is now basic and pink in color.")
