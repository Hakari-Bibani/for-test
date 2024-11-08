import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from itertools import cycle
import time

# Set page title
st.set_page_config(page_title="Acid-Base Titration")

# Create a title with moving text effect
st.title("Acid-Base Titration")
st.markdown("<style>@keyframes bounce {0% {transform: translateY(0);} 50% {transform: translateY(-10px);} 100% {transform: translateY(0);}}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='animation: bounce 1s infinite;'>Acid-Base Titration</h1>", unsafe_allow_html=True)

# Display the burette and flask
col1, col2 = st.columns(2)
with col1:
    st.image("burette.png", width=200)
with col2:
    st.image("conical_flask.png", width=200)

# Titration animation
if st.button("Start Experiment"):
    # Simulate adding NaOH to HCl
    ph = 1.0
    ph_values = []
    while ph < 14:
        # Simulate adding NaOH drop by drop
        for _ in range(10):
            ph += 0.1
            ph_values.append(ph)
            st.markdown(f"<span style='font-size:20px;'>🔴 Adding NaOH drop</span>", unsafe_allow_html=True)
            time.sleep(0.2)
        # Simulate the color change
        st.markdown(f"<span style='font-size:20px;color:green;'>✨ Color change!</span>", unsafe_allow_html=True)
        time.sleep(1)

    # Plot the pH curve
    fig, ax = plt.subplots()
    ax.plot(ph_values)
    ax.set_xlabel("Time")
    ax.set_ylabel("pH")
    ax.set_title("pH Titration Curve")
    st.pyplot(fig)
