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
            background-color: #ff6666;
        }

        .drop {
            width: 6px;
            height: 10px;
            background-color: blue;
            border-radius: 50%;
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            animation: drop-animation 3s forwards;
        }

        @keyframes drop-animation {
            0% { top: 10px; opacity: 1; }
            90% { top: 100px; opacity: 1; }
            100% { top: 100px; opacity: 0; }
        }

        .color-change {
            animation: color-change 1s forwards;
        }

        @keyframes color-change {
            0% { background-color: #ff6666; }
            100% { background-color: #ffcc00; }
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
            <div class="burette"></div>
            <div class="beaker"></div>
        </div>
        """, unsafe_allow_html=True)

    # Animation when the button is pressed
    def animate_titration():
        container.markdown("""
        <div class="experiment-container">
            <div class="burette">
                <div class="drop"></div>
                <div class="drop" style="animation-delay: 0.5s;"></div>
                <div class="drop" style="animation-delay: 1s;"></div>
            </div>
            <div class="beaker color-change"></div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(3)

    # Initial rendering
    render_initial_state()

    # Button to start the experiment
    if st.button("Start Experiment"):
        animate_titration()

        # Plotting the pH curve
        st.write("## Titration pH Curve")
        volume = np.linspace(0, 25, 100)
        pH = 7 + (14 - 0) * (1 - np.exp(-0.3 * (volume - 12.5)))
        fig, ax = plt.subplots()
        ax.plot(volume, pH, label='pH Curve')
        ax.axhline(y=7, color='gray', linestyle='--', label='Neutral pH')
        ax.axvline(x=12.5, color='red', linestyle='--', label='End Point')
        ax.set_xlabel("Volume of NaOH (mL)")
        ax.set_ylabel("pH")
        ax.set_title("pH vs. Volume of NaOH")
        ax.set_ylim(0, 14)  # Set pH range from 0 to 14
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    run_experiment()
