import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import time
from PIL import Image
import base64

# Set page title
st.set_page_config(page_title="Acid-Base Titration")
def app():
    st.set_page_config(page_title="Acid-Base Titration Experiment")
    st.title("Acid-Base Titration Experiment")

# Create a title with moving text effect
st.title("Acid-Base Titration")
st.markdown("<style>@keyframes bounce {0% {transform: translateY(0);} 50% {transform: translateY(-10px);} 100% {transform: translateY(0);}}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='animation: bounce 1s infinite;'>Acid-Base Titration</h1>", unsafe_allow_html=True)
    # Load the HTML animation
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Acid-Base Titration Animation</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }
            .experiment-container {
                position: relative;
                width: 200px;
                height: 400px;
            }
            .burette {
                position: absolute;
                top: 0;
                left: 80px;
                width: 10px;
                height: 300px;
                background-color: #ddd;
                border: 2px solid #aaa;
            }
            .drop {
                position: absolute;
                top: 50px;
                left: 80px;
                width: 6px;
                height: 10px;
                background-color: blue;
                border-radius: 50%;
                animation: drop 4s infinite;
            }
            @keyframes drop {
                0% { top: 50px; opacity: 1; }
                90% { top: 250px; opacity: 1; }
                100% { top: 250px; opacity: 0; }
            }
            .beaker {
                position: absolute;
                bottom: 0;
                left: 50px;
                width: 100px;
                height: 120px;
                border: 2px solid #aaa;
                border-top: none;
                background-color: #ff6666;
                transition: background-color 1s ease;
            }
            .beaker.color-change {
                background-color: #ffcc00;
            }
        </style>
    </head>
    <body>
        <div class="experiment-container">
            <div class="burette"></div>
            <div class="drop"></div>
            <div class="beaker" id="beaker"></div>
        </div>
        <script>
            // Change the color of the beaker after a delay
            setTimeout(() => {
                document.getElementById('beaker').classList.add('color-change');
            }, 4000);
        </script>
    </body>
    </html>
    """

# Placeholder images for burette and flask
st.write("🧪 Burette and Conical Flask")
    # Display the HTML animation
    st.write(f'<div style="text-align: center;">{html_code}</div>', unsafe_allow_html=True)

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
    # Add a start button
    if st.button("Start Experiment"):
        st.write("The experiment is in progress...")
        time.sleep(4)
        st.success("The experiment is complete!")

    # Plot the pH curve
    fig, ax = plt.subplots()
    ax.plot(ph_values)
    ax.set_xlabel("Time")
    ax.set_ylabel("pH")
    ax.set_title("pH Titration Curve")
    st.pyplot(fig)
        # Plot the pH curve
        ph_values = np.linspace(0, 14, 100)
        titration_curve = 14 - ph_values
        st.line_chart(titration_curve)
if __name__ == "__main__":
    app()
