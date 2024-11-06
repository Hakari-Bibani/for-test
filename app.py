import streamlit as st
import time

def main():
    # Custom CSS for styling and animations
    st.markdown("""
    <style>
        /* Title styling with gradient animation */
        .title {
            font-size: 2.5em;
            text-align: center;
            background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96E6A1);
            background-size: 300% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient 6s ease infinite;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Container for experiment */
        .experiment-container {
            position: relative;
            width: 100%;
            height: 400px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin: 20px 0;
        }

        /* Beaker styling */
        .beaker {
            position: relative;
            width: 120px;
            height: 160px;
            background: transparent;
            border: 4px solid #333;
            border-radius: 5px 5px 15px 15px;
            overflow: hidden;
        }

        /* Liquid in beaker */
        .liquid {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 182, 193, 0.6);
            transition: all 0.5s ease;
        }

        /* Spoon styling */
        .spoon {
            position: absolute;
            right: calc(50% - 80px);
            top: 40%;
            transform-origin: right center;
            transition: transform 1s ease;
        }

        .spoon-handle {
            width: 100px;
            height: 10px;
            background: #999;
            border-radius: 5px;
        }

        .spoon-bowl {
            position: absolute;
            left: -30px;
            top: -15px;
            width: 40px;
            height: 40px;
            background: #999;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
            font-size: 12px;
        }

        /* Reaction animations */
        @keyframes bubble {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-300px) scale(0); opacity: 0; }
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: bubble 1s ease-out forwards;
        }

        /* Chemical formula styling */
        .chemical-equation {
            text-align: center;
            font-size: 1.2em;
            margin-top: 20px;
            padding: 10px;
            background: #f0f0f0;
            border-radius: 5px;
        }

        /* Label styling */
        .label {
            position: absolute;
            bottom: -25px;
            width: 100%;
            text-align: center;
            font-weight: bold;
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display title
    st.markdown('<h1 class="title">Baking Soda and Vinegar Reaction</h1>', unsafe_allow_html=True)

    # Create container for experiment
    experiment_container = st.empty()

    def create_bubbles():
        bubbles = ""
        for i in range(15):
            size = random.randint(10, 20)
            left = random.randint(10, 90)
            delay = random.uniform(0, 0.5)
            bubbles += f"""
                <div class="bubble" style="
                    width: {size}px;
                    height: {size}px;
                    left: {left}%;
                    animation-delay: {delay}s;
                "></div>
            """
        return bubbles

    def render_experiment(pouring=False, reacting=False):
        spoon_class = "transform: rotate(45deg);" if pouring else ""
        bubbles = create_bubbles() if reacting else ""
        
        experiment_container.markdown(f"""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="liquid"></div>
                    {bubbles}
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon" style="{spoon_class}">
                    <div class="spoon-handle"></div>
                    <div class="spoon-bowl">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Initial render
    render_experiment()

    # Button to start experiment
    if st.button("Start Experiment"):
        # Pour animation
        render_experiment(pouring=True)
        time.sleep(1)
        
        # Reaction animation
        render_experiment(pouring=True, reacting=True)
        time.sleep(2)
        
        # Display chemical equation
        st.markdown("""
            <div class="chemical-equation">
                NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    import random
    main()
