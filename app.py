import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set page configuration
st.set_page_config(page_title="Acid-Base Titration", layout="wide")

# Title with wave animation
title = st.empty()
title_text = "Acid-Base Titration"
title_wave = np.sin(np.linspace(0, 10 * np.pi, len(title_text))) * 5
wave_anim = title.markdown(f'<h1 style="position:relative;left:{title_wave[0]}px;">{title_text[0]}</h1>', unsafe_allow_html=True)

# Experiment button
start_button = st.button("Start Experiment")

if start_button:
    # Animation of adding NaOH to HCl
    titration_anim = st.empty()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 14)
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    
    x = np.linspace(0, 25, 100)
    y = 2 + np.log10(0.1 / (0.1 + x / 1000))
    line, = ax.plot([], [], lw=2)
    
    def animate(i):
        line.set_data(x[:i], y[:i])
        return line,
    
    titration_anim = st.pyplot(fig)
    anim = FuncAnimation(fig, animate, frames=len(x), interval=50, blit=True)
    
    # Display the plot with the endpoint
    st.title("Titration Curve")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y)
    ax.scatter(12.5, 7, color='r', s=100, label='Endpoint')
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    ax.legend()
    st.pyplot(fig)
    
def wave_animation():
    for i in range(len(title_wave)):
        wave_anim.markdown(f'<h1 style="position:relative;left:{title_wave[i]}px;">{title_text[0]}</h1>', unsafe_allow_html=True)
        title.empty()
        title.markdown(f'<h1 style="position:relative;left:{title_wave[i]}px;">{title_text[0]}</h1>', unsafe_allow_html=True)
        st.experimental_rerun()

# Start the wave animation
wave_animation()
