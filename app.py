import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.patches import Ellipse, Rectangle

# Function to draw the titration setup with a burette and conical flask
def draw_titration_setup(volume, drop_visible):
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 30)
    ax.axis("off")

    # Draw the burette
    burette = Rectangle((4.5, 10), 1, 15, edgecolor="black", facecolor="lightblue", lw=2)
    ax.add_patch(burette)
    ax.text(5, 26, "Burette (NaOH)", ha="center", fontsize=10)

    # Draw the liquid level in the burette
    liquid_level = 25 - volume  # Adjust the level based on volume
    ax.add_patch(Rectangle((4.5, 10 + liquid_level / 2), 1, 15 - liquid_level / 2, edgecolor="none", facecolor="blue"))

    # Draw the conical flask
    flask = Ellipse((5, 2), 6, 4, edgecolor="black", facecolor="none", lw=2)
    ax.add_patch(flask)
    ax.text(5, 0.5, "Conical Flask (HCl)", ha="center", fontsize=10)

    # Draw the HCl solution in the conical flask
    ax.add_patch(Ellipse((5, 2), 4, 1.5, edgecolor="none", facecolor="lightcoral"))

    # Draw a drop if visible
    if drop_visible:
        ax.plot(5, 9, "o", color="blue", markersize=10)

    return fig

# Set up the title with a wave effect
st.markdown(
    """
    <style>
    @keyframes wave {
        0% { transform: translateY(0px); }
        25% { transform: translateY(-5px); }
        50% { transform: translateY(0px); }
        75% { transform: translateY(5px); }
        100% { transform: translateY(0px); }
    }
    .wave-text {
        display: inline-block;
        animation: wave 2s infinite;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    <div class="wave-text">Acid Base Titration</div>
    """,
    unsafe_allow_html=True
)

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
