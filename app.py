import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Define function to simulate titration
def titrate(initial_ph, acid_volume, base_volume, end_point_ph):
    # Simulate adding base to acid
    ph = initial_ph
    volumes = []
    phs = []
    while ph < end_point_ph:
        base_added = min(0.1, base_volume)
        base_volume -= base_added
        ph = ph + base_added / acid_volume
        volumes.append(base_added)
        phs.append(ph)
    
    return volumes, phs

# Create the app
st.title("Acid Base Titration")

# Add a header with a moving effect
header = st.empty()
for i in range(100):
    header.title(f"Acid Base Titration ({i}%)")

# Set up the experiment parameters
initial_ph = st.number_input("Initial pH of Acid", value=2.0, min_value=0.0, max_value=14.0, step=0.1)
acid_volume = st.number_input("Volume of Acid (mL)", value=50.0, min_value=0.0, step=0.1)
base_volume = st.number_input("Volume of Base (mL)", value=0.0, min_value=0.0, step=0.1)
end_point_ph = st.number_input("End Point pH", value=7.0, min_value=0.0, max_value=14.0, step=0.1)

# Add a button to start the experiment
if st.button("Start Experiment"):
    # Simulate the titration
    volumes, phs = titrate(initial_ph, acid_volume, base_volume, end_point_ph)
    
    # Create the animation
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, max(volumes))
    ax.set_ylim(initial_ph, end_point_ph)
    ax.set_xlabel("Volume of Base Added (mL)")
    ax.set_ylabel("pH")
    line, = ax.plot([], [], lw=2)

    def animate(i):
        line.set_data([volumes[:i], phs[:i]])
        return line,

    ani = FuncAnimation(fig, animate, frames=len(volumes), interval=100, blit=True)

    # Display the animation
    st.write("Titration Animation:")
    st.pyplot(fig)

    # Display the plot
    st.write("pH vs. Volume of Base Added:")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(volumes, phs)
    ax.axvline(x=base_volume, color='r', linestyle='--')
    ax.set_xlabel("Volume of Base Added (mL)")
    ax.set_ylabel("pH")
    ax.set_title("Acid-Base Titration")
    st.pyplot(fig)
