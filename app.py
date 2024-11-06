import streamlit as st
import time

def run_experiment():
    # Custom CSS for styling and animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');
        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 3em;
            color: #007BFF;
            text-align: center;
            margin-bottom: 30px;
            animation: wave 2s infinite;
        }
        @keyframes wave {
            0%, 100% { transform: translateX(0); }
            50% { transform: translateX(10px); }
        }
        .experiment-container {
            position: relative;
            display: flex;
            justify-content: center;
            height: 400px;
        }
        .beaker {
            width: 120px;
            height: 180px;
            border: 3px solid #000;
            border-radius: 5px 5px 10px 10px;
            position: relative;
            background-color: rgba(173, 216, 230, 0.6); /* Pale blue water */
            overflow: hidden;
        }
        .water {
            width: 100%;
            height: 50%;
            background-color: rgba(173, 216, 230, 0.6);
            position: absolute;
            bottom: 0;
        }
        .label-h2o {
            font-size: 14px;
            font-weight: bold;
            color: #007BFF;
            text-align: center;
            margin-top: 5px;
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%);
        }
        .spoon {
            width: 80px;
            height: 20px;
            background: #aaa;
            border-radius: 10px;
            position: absolute;
            top: 60px;
            left: 50%;
            transform: translateX(-50%);
            transform-origin: center right;
            transition: transform 1s;
        }
        .spoon-content {
            font-size: 12px;
            color: #333;
            position: absolute;
            right: -20px;
            top: -10px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #000;
            color: #fff;
            width: 30px;
            height: 30px;
            border-radius: 50%;
        }
        .pouring {
            transform: translateX(-50%) rotate(-45deg);
        }
        .reaction {
            width: 100%;
            height: 0;
            background: radial-gradient(circle, red, orange, yellow, white);
            position: absolute;
            bottom: 0;
            animation: explode 1s ease-out forwards;
        }
        @keyframes explode {
            0% { height: 0; opacity: 1; }
            50% { height: 150px; opacity: 0.8; }
            100% { height: 200px; opacity: 0; }
        }
        .boom-text {
            font-size: 2.5em;
            font-weight: bold;
            color: red;
            text-align: center;
            opacity: 0;
            animation: boom 1s ease-out 1s forwards;
        }
        @keyframes boom {
            0% { transform: scale(0); opacity: 0; }
            100% { transform: scale(1.5); opacity: 1; }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Sodium And Water Reaction</h1>", unsafe_allow_html=True)

    # Container for the experiment setup
    container = st.empty()

    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="water"></div>
                    <div class="label-h2o">H₂O</div>
                </div>
                <div class="spoon">
                    <div class="spoon-content">Na</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def animate_experiment():
        # Step 1: Animate the spoon tilting and dropping particles
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="water"></div>
                    <div class="label-h2o">H₂O</div>
                    <div class="reaction"></div>
                </div>
                <div class="spoon pouring">
                    <div class="spoon-content">Na</div>
                </div>
            </div>
            <div class="boom-text">BOOM!</div>
        """, unsafe_allow_html=True)
        time.sleep(2)  # Pause to display the reaction

    # Initial render
    render_initial_state()

    # Button to start the experiment
    if st.button("Start Experiment"):
        animate_experiment()
        # Display the chemical equation
        st.markdown("""
            **Chemical Equation:**
            2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)
        """)

if __name__ == "__main__":
    run_experiment()
