import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Function to calculate pH at each step
def calculate_ph(volume_naoh, concentration_naoh, initial_volume_hcl, concentration_hcl):
    moles_hcl = initial_volume_hcl * concentration_hcl
    moles_naoh = volume_naoh * concentration_naoh

    if moles_naoh < moles_hcl:
        # Before equivalence point (excess HCl)
        moles_h_remaining = moles_hcl - moles_naoh
        concentration_h = moles_h_remaining / (initial_volume_hcl + volume_naoh)
        pH = -np.log10(concentration_h)
    elif moles_naoh == moles_hcl:
        # At equivalence point (neutral pH)
        pH = 7.0
    else:
        # After equivalence point (excess NaOH)
        moles_oh_excess = moles_naoh - moles_hcl
        concentration_oh = moles_oh_excess / (initial_volume_hcl + volume_naoh)
        pOH = -np.log10(concentration_oh)
        pH = 14 - pOH

    return pH

# Title of the app
st.title("Titration of NaOH into HCl")

# Initial setup
st.write("This simulation shows the titration of NaOH into HCl and plots the pH change as NaOH is added.")

# Parameters
initial_volume_hcl = 0.05  # 50 mL of HCl in liters
concentration_hcl = 0.1  # Molarity of HCl
concentration_naoh = 0.1  # Molarity of NaOH
max_volume_naoh = 0.1  # Maximum volume of NaOH to add in liters

# Initialize data for plotting
volumes_naoh = np.linspace(0, max_volume_naoh, 100)
pH_values = []

# Animation: Simulate adding NaOH and calculate pH
st.write("Adding NaOH...")
progress_bar = st.progress(0)

for i, volume_naoh in enumerate(volumes_naoh):
    pH = calculate_ph(volume_naoh, concentration_naoh, initial_volume_hcl, concentration_hcl)
    pH_values.append(pH)
    
    # Update progress
    progress_bar.progress((i + 1) / len(volumes_naoh))
    time.sleep(0.05)

# Plotting the titration curve
st.write("Titration Complete. Here is the titration curve:")

plt.figure(figsize=(8, 5))
plt.plot(volumes_naoh * 1000, pH_values, marker='o')  # Convert volume to mL for the plot
plt.title("Titration Curve: NaOH added to HCl")
plt.xlabel("Volume of NaOH added (mL)")
plt.ylabel("pH")
plt.grid(visible=True)
st.pyplot(plt)
