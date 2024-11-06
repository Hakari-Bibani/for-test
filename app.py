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
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(45deg, #ff4757, #2ed573, #1e90ff, #ffa502);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient 3s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .experiment-container {
            position: relative;
            display: flex;
            justify-content: center;
            height: 400px;
        }
        .beaker {
            width: 100px;
            height: 150px;
            border: 3px solid #555;
            border-radius: 5px 5px 10px 10px;
            background: rgba(255, 182, 193, 0.6);
            position: absolute;
            bottom: 0;
            overflow: hidden;
        }
        .beaker-fill {
            width: 100px;
            height: 75px;
            background: rgba(255, 182, 193, 0.6);
            position: absolute;
            bottom: 0;
            animation: fill 2s ease-in-out forwards;
        }
        .label {
            font-size: 14px;
            font-weight: bold;
            color: #555;
            text-align: center;
            margin-top: 5px;
        }
        .spoon {
            width: 80px;
            height: 20px;
            background: #d3d3d3;
            border-radius: 10px;
            position: absolute;
            left: 10px; /* Centered above the beaker */
            top: 80px; /* Adjusted position */
            transform-origin: right center;
            transition: transform 1s;
        }
        .spoon-content {
            font-size: 14px;
            color: #555;
            position: absolute;
            right: -30px;
            top: -10px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #d3d3d3;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .pouring {
            transform: rotate(-45deg);
        }
        .small-ball {
            width: 5px;
            height: 5px;
            background-color: #d3d3d3;
            border-radius: 50%;
            position: absolute;
            animation: drop 1s ease-in forwards;
        }
        @keyframes drop {
            0% { top: 10px; opacity: 1; }
            100% { top: 130px; opacity: 0; }
        }
        .reaction {
            width: 100px;
            height: 0;
            background: linear-gradient(to top, #ff4757, #2ed573, #1e90ff);
            border-radius: 50% 50% 0 0;
            position: absolute;
            bottom: 0;
            animation: bubbles 2s ease forwards;
        }
        @keyframes bubbles {
            0% { height: 0; }
            50% { height: 200px; }
            100% { height: 300px; opacity: 0; }
        }
        .small-bubble {
            width: 10px;
            height: 10px;
            background-color: #2ed573;
            border-radius: 50%;
            position: absolute;
            animation: smallBubbles 1s ease-in-out infinite;
        }
        @keyframes smallBubbles {
            0% { bottom: 0; opacity: 0; }
            50% { bottom: 150px; opacity: 1; }
            100% { bottom: 300px; opacity: 0; }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Baking Soda and Vinegar Reaction</h1>", unsafe_allow_html=True)

    # Container for the experiment setup
    container = st.empty()

    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="beaker-fill"></div>
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon">
                    <div class="spoon-content">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def animate_experiment():
        # Step 1: Animate the spoon bending and pouring
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="beaker-fill"></div>
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon pouring">
                    <div class="spoon-content">NaHCO₃</div>
                </div>
                <!-- Small balls simulating NaHCO₃ being poured -->
                <div class="small-ball" style="left: 30px;"></div>
                <div class="small-ball" style="left: 40px; animation-delay: 0.2s;"></div>
                <div class="small-ball" style="left: 50px; animation-delay: 0.4s;"></div>
                <div class="small-ball" style="left: 60px; animation-delay: 0.6s;"></div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1)  # Pause before showing the reaction

        # Step 2: Show the reaction with bubbles
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="beaker-fill"></div>
                    <div class="label">CH₃COOH</div>
                    <div class="reaction"></div>
                    <!-- Add small bubbles -->
                    <div class="small-bubble" style="left: 20px; animation-delay: 0.2s;"></div>
                    <div class="small-bubble" style="left: 40px; animation-delay: 0.5s;"></div>
                    <div class="small-bubble" style="left: 60px; animation-delay: 0.8s;"></div>
                    <div class="small-bubble" style="left: 80px; animation-delay: 1.2s;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Initial render
    render_initial_state()

    # Button to start the experiment
    if st.button("Start Experiment"):
        animate_experiment()
        # Display the chemical equation
        st.markdown("""
            **Chemical Equation:**
            NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
        """)

if __name__ == "__main__":
    run_experiment()
