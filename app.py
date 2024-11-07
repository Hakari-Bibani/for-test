import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Set the title with a moving animation
st.title("🔬 Acid-Base Titration Experiment")

# Experiment setup
st.write("### Setup")
st.write("In this experiment, we are adding NaOH from the burette into HCl in the conical flask.")

# Function to draw the static diagram of the burette and conical flask
def draw_titration_setup():
    fig, ax = plt.subplots(figsize=(4, 8))

    # Draw the Burette
    ax.add_patch(plt.Rectangle((0.9, 6), 0.2, 4, edgecolor='black', facecolor='lightblue', lw=2))  # Burette body
    ax.plot([0.9, 1.1], [10, 10], color='black', lw=2)  # Top line
    ax.plot([1, 1], [6, 5.5], color='black', lw=2)  # Nozzle
    ax.plot([0.95, 1.05], [5.5, 5.5], color='black', lw=2)  # Nozzle opening

    # Draw the drop from the burette
    ax.plot([1, 1], [5.4, 5.3], color='blue', lw=2)  # Drop line
    ax.scatter([1], [5.3], color='blue', s=40)  # Drop

    # Draw the Conical Flask
    ax.plot([0.5, 1.5], [0, -3], color='black', lw=2)  # Left side
    ax.plot([1.5, 0.5], [0, -3], color='black', lw=2)  # Right side
    ax.plot([0.5, 1.5], [-3, -3], color='black', lw=2)  # Base
    ax.add_patch(plt.Polygon([[0.5, -3], [1.5, -3], [1, -0.5]], color='violet', alpha=0.5))  # Liquid in flask

    # Add labels
    ax.text(1.2, 8, "Burette", fontsize=10)
    ax.text(0.7, -3.5, "Conical Flask", fontsize=10)

    # Adjust the plot
    ax.set_xlim(0, 2)
    ax.set_ylim(-5, 11)
    ax.axis('off')  # Hide axes

    return fig

# Display the diagram of the burette and conical flask
st.pyplot(draw_titration_setup())

# Button to start the experiment
if st.button("Start Experiment"):
    # Display a message that the experiment is starting
    st.write("Adding NaOH from the burette to HCl in the conical flask...")

    # Simulate the titration process
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)  # Simulate the addition of each drop
        progress_bar.progress(i + 1)

    # Simulate the color change
    st.write("The solution in the conical flask changes color, indicating the endpoint!")

    # Generate the pH vs. Volume plot
    st.write("### pH vs. Volume Plot")

    # Simulating the titration curve
    volume_NaOH = np.linspace(0, 25, 100)  # Volume of NaOH added (mL)
    pH = 7 + np.arctan((volume_NaOH - 12.5) / 2) * 2 + 2  # Example titration curve

    # Plotting the titration curve
    plt.figure(figsize=(8, 5))
    plt.plot(volume_NaOH, pH, color='blue', lw=2)
    plt.axhline(7, color='gray', linestyle='--', lw=1, label='Neutral pH')
    plt.axvline(12.5, color='red', linestyle='--', lw=1, label='Endpoint')
    plt.xlabel("Volume of NaOH Added (mL)")
    plt.ylabel("pH")
    plt.title("Titration Curve")
    plt.legend()
    st.pyplot(plt)
