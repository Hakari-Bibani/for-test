import streamlit as st
import time

def run_chemical_reaction_app():
    # Custom CSS with improved styling and animations
    st.markdown("""
    <style>
        /* Modern gradient title animation */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
        .title {
            font-family: 'Poppins', sans-serif;
            font-size: 2.5em;
            text-align: center;
            background: linear-gradient(120deg, #ff6b6b, #4ecdc4, #45b7d1, #96e6a1);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient-shift 8s ease infinite;
        }
        @keyframes gradient-shift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Container styling */
        .experiment-container {
            width: 100%;
            height: 500px;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #f8f9fa;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Improved beaker design */
        .beaker {
            width: 160px;
            height: 200px;
            position: relative;
            background: rgba(255, 255, 255, 0.9);
            border: 4px solid #2c3e50;
            border-radius: 10px 10px 20px 20px;
            overflow: hidden;
        }

        /* Liquid in beaker */
        .liquid {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 182, 193, 0.7);
            transition: all 0.5s ease;
        }

        /* Spoon design */
        .spoon {
            position: absolute;
            right: calc(50% - 120px);
            top: 30%;
            transform-origin: right center;
            transition: transform 1.5s ease;
        }

        .spoon-handle {
            width: 100px;
            height: 15px;
            background: #95a5a6;
            border-radius: 15px;
        }

        .spoon-bowl {
            position: absolute;
            left: -40px;
            top: -15px;
            width: 45px;
            height: 45px;
            background: #bdc3c7;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 12px;
            color: #2c3e50;
        }

        /* Animation classes */
        .pouring {
            transform: rotate(45deg);
        }

        /* Reaction effects */
        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s ease-in infinite;
            opacity: 0;
        }

        @keyframes rise {
            0% {
                transform: translateY(0) scale(1);
                opacity: 0;
            }
            50% {
                opacity: 0.8;
            }
            100% {
                transform: translateY(-400px) scale(2);
                opacity: 0;
            }
        }

        /* Chemical formula styling */
        .chemical-equation {
            font-family: 'Times New Roman', serif;
            font-size: 1.2em;
            text-align: center;
            margin-top: 20px;
            padding: 15px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 class='title'>Baking Soda and Vinegar Reaction</h1>", unsafe_allow_html=True)

    # Create container for the experiment
    experiment_container = st.empty()

    def create_bubbles():
        bubbles = ""
        for i in range(15):
            size = np.random.randint(10, 30)
            left = np.random.randint(10, 150)
            delay = np.random.random() * 2
            bubbles += f"""
                <div class="bubble" style="
                    width: {size}px;
                    height: {size}px;
                    left: {left}px;
                    animation-delay: {delay}s;
                "></div>
            """
        return bubbles

    def render_experiment(pouring=False, show_reaction=False):
        bubbles = create_bubbles() if show_reaction else ""
        
        experiment_container.markdown(f"""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="liquid"></div>
                    <div style="position: absolute; bottom: 10px; width: 100%; text-align: center; color: #2c3e50;">
                        CH₃COOH
                    </div>
                    {bubbles}
                </div>
                <div class="spoon {'pouring' if pouring else ''}">
                    <div class="spoon-handle"></div>
                    <div class="spoon-bowl">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Initial render
    render_experiment()

    # Add the start button
    if st.button("Start Experiment"):
        # Animation sequence
        render_experiment(pouring=True)
        time.sleep(1)
        render_experiment(pouring=True, show_reaction=True)
        time.sleep(0.5)
        
        # Show chemical equation
        st.markdown("""
            <div class="chemical-equation">
                NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    import numpy as np
    run_chemical_reaction_app()
