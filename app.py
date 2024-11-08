import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
from streamlit.components.v1 import html

def run_titration_experiment():
    # Custom CSS for enhanced styling and animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');

        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(45deg, #2c3e50, #3498db, #2c3e50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 200% auto;
            animation: gradient 3s linear infinite;
        }

        .experiment-container {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            position: relative;
            height: 500px;
            margin-bottom: 20px;
            overflow: visible;
        }

        .burette {
            width: 20px;
            height: 300px;
            background-color: #ddd;
            border: 2px solid #aaa;
            position: relative;
            margin-top: 20px;
        }

        .burette .label {
            position: absolute;
            bottom: -30px;
            width: 100%;
            text-align: center;
            font-size: 12px;
            color: #2c3e50;
        }

        .beaker {
            width: 100px;
            height: 120px;
            border: 3px solid #ddd;
            border-radius: 5px 5px 10px 10px;
            margin-left: 30px;
            background-color: #ff6666;
            overflow: hidden;
            position: relative;
        }

        .beaker .label {
            position: absolute;
            bottom: -30px;
            width: 100%;
            text-align: center;
            font-size: 12px;
            color: #2c3e50;
        }

        .drop {
            position: absolute;
            top: 0;
            left: 50%;
            width: 6px;
            height: 10px;
            background-color: blue;
            border-radius: 50%;
            opacity: 0;
        }

        .beaker.color-change {
            background-color: #ffcc00;
        }

        @keyframes drop-animation {
            0% { top: 0px; opacity: 1; }
            90% { top: 90px; opacity: 1; }
            100% { top: 90px; opacity: 0; }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title with animation
    st.markdown("<div class='title'>Acid-Base Titration</div>", unsafe_allow_html=True)

    # HTML for experiment setup
    experiment_html = """
    <div class="experiment-container">
        <div class="burette">
            <div class="label">NaOH</div>
            <div class="drop" id="drop"></div>
        </div>
        <div class="beaker" id="beaker">
            <div class="label">HCl</div>
        </div>
    </div>
    <script>
        function startExperiment() {
            const drop = document.getElementById("drop");
            const beaker = document.getElementById("beaker");

            // Animate the drop
            drop.style.opacity = "1";
            drop.style.animation = "drop-animation 2s infinite";

            // Change the color of the beaker after a delay
            setTimeout(() => {
                beaker.classList.add("color-change");
            }, 4000);
        }
    </script>
    """

    # Start button
    if st.button("Start Experiment"):
        # Display the HTML with the animation triggered
        html(experiment_html + "<script>startExperiment();</script>", height=500)
        time.sleep(5)  # Wait for the animation to complete

        # Display the pH titration curve after the animation
        st.write("## Titration pH Curve")
        
        # Generating the simulated pH data
        volume = np.linspace(0, 25, 100)
        pH = 7 + (14 - 7) * (1 - np.exp(-0.2 * (volume - 12.5)))  # pH model

        # Plotting the pH curve
        fig, ax = plt.subplots()
        ax.plot(volume, pH, label='pH Curve')
        ax.axhline(y=7, color='gray', linestyle='--', label='Neutral pH')
        ax.axvline(x=12.5, color='red', linestyle='--', label='End Point')
        ax.set_xlabel("Volume of NaOH (mL)")
        ax.set_ylabel("pH")
        ax.set_title("pH vs. Volume of NaOH")
        ax.legend()

        st.pyplot(fig)

if __name__ == "__main__":
    run_titration_experiment()
