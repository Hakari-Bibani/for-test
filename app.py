import streamlit as st
import time
from PIL import Image
import numpy as np
from math import pi, sin, cos

def app():
    st.set_page_config(page_title="Baking Soda and Vinegar Reaction")

    # Show the title with moving effect
    st.title("Baking Soda and Vinegar Reaction")
    st.markdown("<style>@keyframes moveTitle { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); }}</style>", unsafe_allow_html=True)
    st.markdown("<h1 style='animation: moveTitle 5s linear infinite;'>Baking Soda and Vinegar Reaction</h1>", unsafe_allow_html=True)

    # Display the beaker and spoon
    col1, col2 = st.columns(2)
    with col1:
        # Display the beaker
        beaker = Image.open("beaker.png")
        st.image(beaker, width=200, caption="CH3COOH")

    with col2:
        # Display the spoon and NaHCO3 text
        spoon = Image.open("spoon.png")
        st.image(spoon, width=100)
        st.markdown("""
        <div style="display: flex; align-items: center;">
        <div style="margin-right: 10px;">NaHCO₃</div>
        </div>
        """, unsafe_allow_html=True)

    # Add a button to start the experiment
    if st.button("Start Experiment"):
        # Animate the spoon pouring into the beaker
        for i in range(50):
            spoon_x = 100 + 50 * sin(i * pi / 50)
            spoon_y = 200 + 50 * cos(i * pi / 50)
            st.image(spoon, width=100, x_offset=int(spoon_x), y_offset=int(spoon_y))
            time.sleep(0.02)
        
        # Simulate the reaction
        for i in range(50):
            bubble_x = np.random.randint(50, 350)
            bubble_y = np.random.randint(250, 450)
            bubble_size = np.random.randint(10, 30)
            st.markdown(f"<div style='position: absolute; background-color: white; width: {bubble_size}px; height: {bubble_size}px; border-radius: 50%; left: {bubble_x}px; top: {bubble_y}px;'></div>", unsafe_allow_html=True)
            time.sleep(0.02)

        # Display the chemical equation
        st.markdown("""
        <div style='font-size: 24px; font-weight: bold;'>
        NaHCO₃  + CH₃COOH  → CO₂ + H₂O + NaCH₃COO
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
