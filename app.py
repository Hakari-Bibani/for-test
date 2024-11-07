import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Function to simulate the titration process
def animate_titration():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    line, = ax.plot([], [], lw=2)

    # Example data to simulate pH change as NaOH is added
    volume_naoh = np.linspace(0, 10, 100)
    pH_values = [3 + (i / 10) for i in range(100)]  # Simplified example

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(volume_naoh[:frame], pH_values[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(volume_naoh), init_func=init, blit=True)
    return fig

# Streamlit UI
st.title("Titration Animation: Adding NaOH to HCl Solution")

# Generate and display the animation
fig = animate_titration()
st.pyplot(fig)
