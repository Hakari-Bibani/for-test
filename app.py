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

        .burette-label {
            position: absolute;
            top: 10px;
            left: calc(50% + 15px);
            font-size: 14px;
            color: #2c3e50;
            font-weight: bold;
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
            height: 50%; /* Half-filled */
            background-color: #ff6666;
            position: absolute;
            bottom: 0;
            animation: wave 2s infinite ease-in-out;
            transition: background-color 1s;
        }

        .beaker-label {
            position: absolute;
            top: 350px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 14px;
            color: #2c3e50;
            font-weight: bold;
        }

        @keyframes wave {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(5px); }
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
            animation: drop-animation 2s forwards;
        }

        @keyframes drop-animation {
            0% { top: 10px; opacity: 1; }
            90% { top: 180px; opacity: 1; }
            100% { top: 200px; opacity: 0; }
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
                <div class="burette-label">Burette filled with NaOH</div>
            </div>
            <div class="beaker">
                <div class="solution"></div>
                <div class="beaker-label">HCl</div>
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
                <div class="burette-label">Burette filled with NaOH</div>
                <div class="drop"></div>
                <div class="drop" style="animation-delay: 0.5s;"></div>
                <div class="drop" style="animation-delay: 1s;"></div>
            </div>
            <div class="beaker">
                <div class="solution"></div>
                <div class="beaker-label">HCl</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(2)  # Wait for the drops to fall

        # Step 2: Change the color of the solution in the beaker
        container.markdown("""
        <div class="experiment-container">
            <div class="burette">
                <div class="burette-tab"></div>
                <div class="burette-label">Burette filled with NaOH</div>
            </div>
            <div class="beaker">
                <div class="solution color-change"></div>
                <div class="beaker-label">HCl</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Initial rendering
    render_initial_state()

    # Button to start the experiment
    if st.button("Start Experiment"):
        animate_titration()

        # Plotting the real pH curve for strong acid and base titration
        st.write("## Titration pH Curve")
        volume = np.linspace(0, 25, 100)
        pH = np.where(volume < 12.5, 
                      1 + (6 * (volume / 12.5)),  # pH increases gradually from 1 to 7
                      7 + (7 * ((volume - 12.5) / 12.5)))  # pH increases steeply from 7 to 13
        fig, ax = plt.subplots()
        ax.plot(volume, pH, label='pH Curve', color='blue')
        ax.axhline(y=7, color='gray', linestyle='--', label='Neutral pH (End Point)')
        ax.axvline(x=12.5, color='red', linestyle='--', label='Volume at End Point')
        ax.set_xlabel("Volume of NaOH (mL)")
        ax.set_ylabel("pH")
        ax.set_title("pH vs. Volume of NaOH")
        ax.set_ylim(0, 14)  # Set pH range from 0 to 14
        ax.legend()
        st.pyplot(fig)

        # Display results
        st.write("### Results")
        st.write("- The pH curve represents the titration of a strong acid (HCl) with a strong base (NaOH).")
        st.write("- The end point is at pH 7, where neutralization occurs.")
        st.write("- The pH increases rapidly after the neutralization point due to the excess NaOH added.")

if __name__ == "__main__":
    run_experiment()
