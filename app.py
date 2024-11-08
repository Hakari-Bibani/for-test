import streamlit as st
from streamlit.components.v1 import html
import matplotlib.pyplot as plt
import numpy as np

# Title with animation
st.markdown(
    """
    <div style="text-align: center; font-size: 40px; font-weight: bold; animation: float 2s infinite alternate;">
        Acid-Base Titration
    </div>
    <style>
        @keyframes float {
            0% { transform: translateY(0); }
            100% { transform: translateY(10px); }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Experiment setup with burette and beaker
st.write("## Experiment Setup")
st.write("A thin rectangular burette containing NaOH and a half-filled beaker labeled HCl are shown below.")

# HTML code for burette and beaker animation
experiment_html = """
<div class="experiment-container">
    <div class="burette">
        <div class="label">NaOH</div>
        <div class="drop"></div>
    </div>
    <div class="beaker">
        <div class="label">HCl</div>
    </div>
</div>
<style>
    .experiment-container {
        position: relative;
        width: 250px;
        height: 400px;
        margin: auto;
    }
    .burette {
        position: absolute;
        top: 0;
        left: 90px;
        width: 20px;
        height: 300px;
        background-color: #ddd;
        border: 2px solid #aaa;
        border-radius: 5px;
    }
    .burette .label {
        position: absolute;
        bottom: -20px;
        left: -10px;
        font-size: 12px;
        font-weight: bold;
    }
    .drop {
        position: absolute;
        top: 50px;
        left: 7px;
        width: 6px;
        height: 10px;
        background-color: blue;
        border-radius: 50%;
        opacity: 0;
    }
    .beaker {
        position: absolute;
        bottom: 0;
        left: 50px;
        width: 150px;
        height: 100px;
        background-color: #ff6666;
        border: 2px solid #aaa;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
        overflow: hidden;
        transition: background-color 1s ease;
    }
    .beaker .label {
        position: absolute;
        top: -20px;
        left: 60px;
        font-size: 12px;
        font-weight: bold;
    }
</style>
<script>
    function startExperiment() {
        const drop = document.querySelector('.drop');
        const beaker = document.querySelector('.beaker');

        // Make the drop visible and animate it
        drop.style.opacity = '1';
        drop.style.animation = 'drop 4s forwards';

        // Change the color of the beaker after 4 seconds
        setTimeout(() => {
            beaker.style.backgroundColor = '#ffcc00'; // Color change to represent neutralization
        }, 4000);
    }
    @keyframes drop {
        0% { top: 50px; opacity: 1; }
        90% { top: 250px; opacity: 1; }
        100% { top: 250px; opacity: 0; }
    }
</script>
"""

# Button to start the experiment
if st.button("Start Experiment"):
    # Display the HTML animation
    html(experiment_html + '<script>startExperiment();</script>', height=500)

# Plot the pH curve
st.write("## Titration pH Curve")
# Simulate pH curve data
volume = np.linspace(0, 25, 100)
pH = 7 + (14 - 7) * (1 - np.exp(-0.2 * (volume - 12.5)))

# Plotting
fig, ax = plt.subplots()
ax.plot(volume, pH, label='pH Curve')
ax.axhline(y=7, color='gray', linestyle='--', label='Neutral pH')
ax.axvline(x=12.5, color='red', linestyle='--', label='End Point')
ax.set_xlabel("Volume of NaOH (mL)")
ax.set_ylabel("pH")
ax.set_title("pH vs. Volume of NaOH")
ax.legend()

st.pyplot(fig)
