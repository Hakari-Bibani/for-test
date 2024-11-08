import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

def run_experiment():
    # Custom CSS for styling and animations
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

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        .experiment-container {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            position: relative;
            height: 400px;
            margin-bottom: 20px;
        }

        .burette {
            width: 10px;
            height: 200px;
            background-color: #ddd;
            border: 2px solid #aaa;
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
        }

        .burette-tab {
            width: 20px;
            height: 10px;
            background-color: #aaa;
            position: absolute;
            bottom: -12px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 2px;
        }

        .beaker {
            width: 100px;
            height: 120px;
            border: 3px solid #ddd;
            border-radius: 5px;
            position: absolute;
            top: 220px;
            left: 50%;
            transform: translateX(-50%);
            overflow: hidden;
        }

        .solution {
            width: 100%;
            height: 100%;
            background-color: #ff6666;
            position: absolute;
            bottom: 0;
            transition: background-color 1s;
        }

        .drop {
            width: 6px;
            height: 10px;
            background-color: blue;
            border-radius: 50%;
            position: absolute;
            top: 180px; /* Start near the tab of the burette */
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            animation: drop-animation 2s forwards;
        }

        @keyframes drop-animation {
            0% { top: 180px; opacity: 1; }
            90% { top: 300px; opacity: 1; }
            100% { top: 300px; opacity: 0; }
        }

        .color-change {
            background-color: #ffcc00;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the animated title
    st.markdown("<h1 class='title'>Acid-Base Titration</h1>", unsafe_allow_html=True)

    # Setup for the experiment
    st.write("## Experiment Setup")
    st.write("This experiment involves adding NaOH from the burette to HCl in the beaker.")

    # Container for the animation
    container = st.empty()

    # Initial state
    def render_initial_state():
        container.markdown("""
        <div class="experiment-container">
            <div class="burette">
                <div class="burette-tab"></div>
            </div>
            <div class="beaker">
                <div class="solution"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Animation when the button is pressed
    def animate_titration():
        # Step 1: Show the drops falling
        container.markdown("""
        <div class="experiment-container">
            <div class="burette">
                <div class="burette-tab"></div>
                <div class="drop" style="animation-delay: 0s;"></div>
                <div class="drop" style="animation-delay: 0.5s;"></div>
                <div class="drop" style="animation-delay: 1s;"></div>
            </div>
            <div class="beaker">
                <div class="solution"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(2)  # Wait for the drops to fall

        # Step 2: Change the solution color
        container.markdown("""
        <div class="experiment-container">
            <div class="burette">
                <div class="burette-tab"></div>
            </div>
            <div class="beaker">
                <div class="solution color-change"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Initial rendering
    render_initial_state()

    # Button to start the experiment
    if st.button("Start Experiment"):
        animate_titration()

        # Plotting the pH curve
        st.write("## Titration pH Curve")
        volume = np.linspace(0, 13, 100)  # x-axis from 0 to 13
        pH = 0 + (7 - 0) * (1 - np.exp(-0.3 * (volume - 6.5))) + (14 - 7) * (1 - np.exp(-0.3 * (volume - 6.5)))
        fig, ax = plt.subplots()
        ax.plot(volume, pH, label='pH Curve')
        ax.axhline(y=7, color='gray', linestyle='--', label='Neutral pH (End Point)')
        ax.axvline(x=6.5, color='red', linestyle='--', label='Volume at End Point')
        ax.set_xlabel("Volume of NaOH (mL)")
        ax.set_ylabel("pH")
        ax.set_title("pH vs. Volume of NaOH")
        ax.set_ylim(0, 14)  # Set y-axis from 0 to 14
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    run_experiment()
