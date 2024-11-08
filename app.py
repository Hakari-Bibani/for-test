import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

st.set_page_config(page_title="Acid-Base Titration", layout="wide")

# App title with moving effect
st.title("Acid-Base Titration")
st.markdown("<span style='font-size: 24px; font-weight: bold; animation: movement 2s infinite;'>Acid-Base Titration</span>", unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_images():
    burette = Image.open("burette.png")
    beaker = Image.open("beaker.png")
    return burette, beaker

burette, beaker = load_images()

# Display burette and beaker
col1, col2 = st.columns(2)
with col1:
    st.image(burette, width=200)
with col2:
    st.image(beaker, width=200)

# Add a button to start the experiment
if st.button("Start Experiment"):
    # Animate the addition of NaOH to HCl
    for i in range(50):
        col1.image(burette, width=200)
        col2.image(beaker, width=200)
        time.sleep(0.1)
    
    # Change the color of the beaker
    col2.image(beaker.convert("RGBA"), width=200)

    # Plot the pH vs volume of NaOH added
    x = np.linspace(0, 20, 100)
    y = 7 - np.log10(x)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y)
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    ax.set_title("pH Titration Curve")
    st.pyplot(fig)
