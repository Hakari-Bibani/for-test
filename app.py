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

        .half-fill {
            width: 100%;
            height: 50%;
            background: rgba(255, 182, 193, 0.8);
            position: absolute;
            bottom: 0;
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
            left: 40px;  /* Shifted slightly to the left */
            top: 50px;
            transform-origin: right center;
            transition: transform 1s;
        }

        .spoon-content {
            font-size: 14px;
            color: #555;
            position: absolute;
            left: 30px;  /* Adjusted to ensure the ball falls centrally */
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

        .reaction {
            width: 100px;
            height: 75px; /* Adjusted height for half-fill */
            position: absolute;
            bottom: 0;
        }

        .bubble {
            width: 10px;
            height: 10px;
            background: #ffffff;
            border-radius: 50%;
            position: absolute;
            animation: rise 3s infinite ease-in;
            opacity: 0.8;
        }

        @keyframes rise {
            0% { transform: translateY(0); opacity: 0.8; }
            100% { transform: translateY(-150px); opacity: 0; }
        }

        .bubbles-container {
            position: relative;
            width: 100%;
            height: 100%;
        }

        .bubble:nth-child(1) { left: 10%; animation-delay: 0s; }
        .bubble:nth-child(2) { left: 30%; animation-delay: 0.5s; }
        .bubble:nth-child(3) { left: 50%; animation-delay: 1s; }
        .bubble:nth-child(4) { left: 70%; animation-delay: 1.5s; }
        .bubble:nth-child(5) { left: 90%; animation-delay: 2s; }

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
                    <div class="label">CH₃COOH</div>
                    <div class="half-fill"></div>  <!-- Half-filled beaker -->
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
                    <div class="label">CH₃COOH</div>
                    <div class="half-fill"></div>
                </div>
                <div class="spoon pouring">
                    <div class="spoon-content">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1)  # Pause before showing the reaction

        # Step 2: Show the reaction with multiple bubbles
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">CH₃COOH</div>
                    <div class="half-fill"></div>
                    <div class="bubbles-container">
                        <div class="bubble"></div>
                        <div class="bubble"></div>
                        <div class="bubble"></div>
                        <div class="bubble"></div>
                        <div class="bubble"></div> <!-- Multiple bubbles -->
                    </div>
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
