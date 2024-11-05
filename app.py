import streamlit as st
import time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set page title
st.set_page_config(page_title="Elephant Toothpaste Reaction")

# Add title
st.title("Elephant Toothpaste Reaction")

# Add static images
col1, col2 = st.columns(2)
with col1:
    beaker_img = Image.open("beaker.png")
    st.image(beaker_img, caption="H2O2")
with col2:
    cylinder_img = Image.open("cylinder.png")
    st.image(cylinder_img, caption="KI")

# Function to animate the beaker bending
def animate_beaker_bend(frame):
    beaker_img = Image.open("beaker.png")
    beaker_img = beaker_img.rotate(frame * 10)
    return st.image(beaker_img, caption="H2O2", use_column_width=True)

# Function to animate the foam jumping
def animate_foam_jump(frame):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Generate random foam particles
    x = np.random.uniform(0, 10, 100)
    y = np.random.uniform(0, 10, 100)
    size = np.random.uniform(0.5, 2, 100)
    color = np.random.uniform(0, 1, (100, 3))

    # Update the foam particles
    ax.scatter(x, y, s=size * frame, c=color)

    return st.pyplot(fig)

# Add start experiment button
if st.button("Start Experiment"):
    # Animate the pouring of the solution
    beaker_animation = st.empty()
    for i in range(18):
        beaker_animation(animate_beaker_bend(i))
        time.sleep(0.1)

    # Animate the reaction
    foam_animation = st.empty()
    foam_ani = FuncAnimation(plt.figure(), animate_foam_jump, frames=np.linspace(1, 10, 50), interval=50, blit=False)
    foam_animation(foam_ani)
    time.sleep(3)

    # Display the chemical equation
    st.markdown("**Chemical Equation:**")
    st.latex(r"2H_2O_2 (aq) \to 2H_2O (l) + O_2 (g)")
    st.write("*Note: The optional addition of food coloring and liquid soap can enhance the visual effect.*")

st.markdown("Click the 'Start Experiment' button to repeat the reaction!")
