import streamlit as st
import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Acid-Base Titration", layout="wide")

# Define function to simulate titration
def titrate(initial_ph, volume_naoh, volume_hcl):
    # Simulate adding NaOH to HCl
    ph = initial_ph
    ph_values = [ph]
    for i in range(int(volume_naoh)):
        ph += 0.1
        ph_values.append(ph)
        time.sleep(0.1)
    
    # Find endpoint
    endpoint = ph_values[-1]
    
    # Plotting
    x = np.arange(len(ph_values))
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, ph_values)
    ax.axvline(x=len(ph_values)-1, color='r', linestyle='--')
    ax.set_xlabel('Volume of NaOH Added (mL)')
    ax.set_ylabel('pH')
    ax.set_title('Acid-Base Titration')
    
    return endpoint, fig

# App layout
st.title("Acid-Base Titration")

# Show animation of adding NaOH
if st.button("Start Experiment"):
    st.subheader("Adding NaOH to HCl")
    
    # Display animation
    image = Image.open('burette.gif')
    st.image(image, use_column_width=True)
    
    # Simulate titration
    endpoint, plot = titrate(2.0, 10, 25)
    
    # Display plot
    st.subheader("Titration Curve")
    st.pyplot(plot)
    
    st.success(f"Endpoint reached at pH {endpoint:.2f}")
