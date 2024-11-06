import streamlit as st
import time

def setup_styles():
    """Configure custom CSS styles for the application"""
    st.markdown("""
    <style>
        /* Title styling with gradient animation */
        .experiment-title {
            font-family: 'Arial', sans-serif;
            font-size: 2.5em;
            text-align: center;
            background: linear-gradient(
                90deg,
                #ff6b6b,
                #4ecdc4,
                #45b7d1,
                #96c93d
            );
            background-size: 300% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient-flow 6s ease infinite;
        }
        
        @keyframes gradient-flow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Container for experiment visualization */
        .experiment-area {
            position: relative;
            height: 500px;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin: 20px 0;
        }

        /* Beaker styling */
        .beaker {
            position: relative;
            width: 160px;
            height: 200px;
            border: 4px solid #666;
            border-radius: 5px 5px 15px 15px;
            background: rgba(255, 255, 255, 0.9);
            overflow: hidden;
        }

        /* Solution in beaker */
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 192, 203, 0.4);
            transition: all 0.5s ease;
        }

        /* Chemical formula label */
        .chemical-label {
            position: absolute;
            bottom: -25px;
            width: 100%;
            text-align: center;
            font-weight: bold;
            color: #333;
        }

        /* Spoon styling */
        .spoon {
            position: absolute;
            right: 45%;
            top: 20%;
            transform-origin: right center;
            transition: transform 1s ease;
        }

        .spoon-handle {
            width: 100px;
            height: 15px;
            background: #999;
            border-radius: 8px;
        }

        .spoon-bowl {
            position: absolute;
            right: -20px;
            top: -12px;
            width: 40px;
            height: 40px;
            background: #999;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
            font-size: 0.8em;
        }

        /* Animation classes */
        .pour {
            transform: rotate(45deg);
        }

        /* Reaction effects */
        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: float-up 2s ease-out forwards;
        }

        @keyframes float-up {
            0% {
                transform: translateY(0) scale(1);
                opacity: 0.8;
            }
            100% {
                transform: translateY(-400px) scale(0);
                opacity: 0;
            }
        }

        /* Chemical equation styling */
        .equation {
            text-align: center;
            font-size: 1.2em;
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

def create_bubbles():
    """Generate random bubble elements for the reaction animation"""
    bubbles = ""
    for i in range(15):
        size = np.random.randint(10, 30)
        left = np.random.randint(10, 150)
        delay = np.random.random() * 0.5
        bubbles += f"""
            <div class="bubble" style="
                width: {size}px;
                height: {size}px;
                left: {left}px;
                animation-delay: {delay}s;
            "></div>
        """
    return bubbles

def render_experiment(is_pouring=False, show_reaction=False):
    """Render the experiment visualization with optional animations"""
    bubbles = create_bubbles() if show_reaction else ""
    spoon_class = "pour" if is_pouring else ""
    
    experiment_html = f"""
    <div class="experiment-area">
        <div class="beaker">
            <div class="solution"></div>
            <div class="chemical-label">CH₃COOH</div>
            {bubbles}
        </div>
        <div class="spoon {spoon_class}">
            <div class="spoon-handle"></div>
            <div class="spoon-bowl">NaHCO₃</div>
        </div>
    </div>
    """
    return experiment_html

def main():
    # Set page config
    st.set_page_config(page_title="Chemistry Experiment", layout="wide")
    
    # Setup custom styles
    setup_styles()
    
    # Display title
    st.markdown('<h1 class="experiment-title">Baking Soda and Vinegar Reaction</h1>', unsafe_allow_html=True)
    
    # Create placeholder for experiment visualization
    experiment_container = st.empty()
    
    # Initial render
    experiment_container.markdown(render_experiment(), unsafe_allow_html=True)
    
    # Create button
    if st.button("Start Experiment"):
        # Pour animation
        experiment_container.markdown(render_experiment(is_pouring=True), unsafe_allow_html=True)
        time.sleep(1)
        
        # Reaction animation
        experiment_container.markdown(render_experiment(is_pouring=True, show_reaction=True), unsafe_allow_html=True)
        time.sleep(2)
        
        # Show chemical equation
        st.markdown("""
        <div class="equation">
            <strong>Chemical Equation:</strong><br>
            NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    import numpy as np
    main()
