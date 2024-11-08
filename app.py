import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.patches import Ellipse, Polygon, Rectangle

# Function to draw the titration setup with a burette and conical flask
def draw_titration_setup(volume, drop_visible):
    fig, ax = plt.subplots(figsize=(4, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 35)
    ax.axis("off")

    # Draw the burette
    ax.add_patch(Rectangle((4.5, 20), 1, 10, edgecolor="black", facecolor="none", lw=2))
    ax.text(5, 31, "Burette (NaOH)", ha="center", fontsize=10)

    # Draw the liquid level in the burette
    liquid_level = 30 - volume  # Adjust the level based on volume
    ax.add_patch(Rectangle((4.5, 20 + liquid_level / 3), 1, 10 - liquid_level / 3, edgecolor="none", facecolor="blue"))

    # Draw the conical flask
    flask_body = Polygon([(3, 1), (7, 1), (5.5, 5), (4.5, 5)], closed=True, edgecolor="black", facecolor="none", lw=2)
    ax.add_patch(flask_body)
    ax.text(5, 0.5, "Conical Flask (HCl)", ha="center", fontsize=10)

    # Draw the HCl solution in the conical flask
    ax.add_patch(Polygon([(4.6, 1.5), (6.4, 1.5), (5.8, 4.2), (4.2, 4.2)], closed=True, edgecolor="none", facecolor="lightcoral"))

    # Draw a drop if visible
    if drop_visible:
        ax.plot(5.5, 19, "o", color="blue", markersize=10)

    return fig

# Set up the title
st.title("Acid Base Titration Simulation")

# Create a start button for the experiment
if st.button("Start Experiment"):
    st.write("### Titration in Progress...")

    # Simulate the titration process
    pH_values = []
    volume_added = np.linspace(0, 25, 100)  # Simulating 25 mL of NaOH added in increments
    equivalence_point = 13  # Assuming the equivalence point occurs at around 13 mL

    # Simulate the pH change and the animation
    for i, volume in enumerate(volume_added):
        if volume < equivalence_point:
            pH = 1 + (volume / equivalence_point) * 6  # pH gradually increases
        else:
            pH = 7 + (volume - equivalence_point) / (25 - equivalence_point) * 7  # Rapid increase after equivalence

        pH_values.append(pH)
        drop_visible = (i % 5 == 0)  # Show a drop every 5 iterations

        # Draw the setup and display it
        fig = draw_titration_setup(volume, drop_visible)
        st.pyplot(fig)
        time.sleep(0.1)  # Pause for animation effect

    # Plot the pH curve
    st.write("### pH vs Volume Added")
    plt.figure()
    plt.plot(volume_added, pH_values, label="pH Curve")
    plt.axvline(equivalence_point, color="r", linestyle="--", label="Equivalence Point")
    plt.xlabel("Volume of NaOH Added (mL)")
    plt.ylabel("pH")
    plt.title("Titration Curve")
    plt.legend()
    st.pyplot(plt)
