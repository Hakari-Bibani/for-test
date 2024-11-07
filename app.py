import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set page title
st.set_page_config(page_title="Acid Base Titration")

# Add title with wave animation
st.title("Acid Base Titration")
st.markdown("""<style>
@keyframes wave {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}
h1 {
    animation: wave 10s linear infinite;
}
</style>""", unsafe_allow_html=True)

# Function to simulate titration
def titrate(initial_volume, initial_pH, base_volume, base_concentration):
    # Calculate pH at each step
    volumes = np.linspace(0, base_volume, 100)
    pH = [initial_pH]
    for vol in volumes[1:]:
        new_pH = initial_pH - np.log10(vol * base_concentration / (initial_volume + vol))
        pH.append(new_pH)

    # Find the end point
    end_point = volumes[np.argmin(np.abs(np.array(pH) - 7))]

    return volumes, pH, end_point

# Streamlit app
if st.button("Start Experiment"):
    # Simulate the titration
    initial_volume = 50  # mL
    initial_pH = 2
    base_volume = 20  # mL
    base_concentration = 0.1  # M

    volumes, pH, end_point = titrate(initial_volume, initial_pH, base_volume, base_concentration)

    # Animate the titration
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, base_volume)
    ax.set_ylim(initial_pH - 1, initial_pH + 1)
    ax.set_xlabel("Volume of NaOH (mL)")
    ax.set_ylabel("pH")
    ax.set_title("Acid-Base Titration")
    line, = ax.plot([], [], lw=2)

    def animate(i):
        line.set_data([volumes[i], volumes[i]], [initial_pH, pH[i]])
        return line,

    ani = FuncAnimation(fig, animate, frames=len(volumes), interval=50, blit=True)

    # Show the plot
    st.pyplot(fig)

    # Display the end point
    st.write(f"The end point of the titration is at {end_point:.2f} mL of NaOH.")
