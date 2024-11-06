import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# App title
st.title("Baking Soda and Vinegar Reaction 🌋")

# Initial setup
st.subheader("Initial Setup:")
st.write("Below, you see a beaker filled with a pale red solution, which represents vinegar (CH₃COOH), and a spoon holding baking soda (NaHCO₃).")

# Displaying the initial setup (use placeholders for animations)
fig, ax = plt.subplots()

# Setting up the beaker and spoon representation
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# Drawing the beaker
beaker = plt.Rectangle((3, 1), 4, 5, fill=None, edgecolor='black', linewidth=2)
ax.add_patch(beaker)

# Vinegar solution in the beaker
vinegar = plt.Rectangle((3, 1), 4, 2.5, color='lightcoral')
ax.add_patch(vinegar)

# Spoon with baking soda
spoon, = ax.plot([4, 6], [7, 7], 'lightgray', linewidth=3)  # Spoon handle
baking_soda, = ax.plot(5, 7, 'o', color='lightgray', markersize=10)  # Baking soda blob

# Animation function
def animate(frame):
    if frame < 20:
        spoon.set_ydata([7 - frame * 0.1, 7 - frame * 0.1])  # Bend spoon downwards
        baking_soda.set_ydata(7 - frame * 0.1)  # Move baking soda
    elif frame == 20:
        ax.add_patch(plt.Circle((5, 3.5), 0.1, color='white'))  # Small initial bubble
    elif frame > 20:
        # Simulate bubbles rising and expanding
        for _ in range(5):
            x = np.random.uniform(3.5, 6.5)
            y = np.random.uniform(3, 5.5)
            size = np.random.uniform(0.05, 0.2)
            ax.add_patch(plt.Circle((x, y), size, color='white', alpha=0.6))

# Run animation
anim = FuncAnimation(fig, animate, frames=40, interval=100)

# Show animation
st.pyplot(fig)

# Button to start experiment
if st.button("Start Experiment"):
    st.write("Watch the reaction unfold!")

# Reaction output and equation
st.subheader("Reaction:")
st.write("As the baking soda falls into the vinegar, a vigorous reaction occurs, creating carbon dioxide gas, water, and sodium acetate.")
st.latex(r"NaHCO_3 (s) + CH_3COOH (aq) \rightarrow CO_2 (g) + H_2O (l) + NaCH_3COO (aq)")

# Ending message
st.write("Enjoy the fascinating chemistry behind this classic experiment!")

