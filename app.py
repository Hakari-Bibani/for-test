import streamlit as st
import time

def run_experiment():
    # Set page configuration
    st.set_page_config(page_title="Chemical Reaction", layout="centered")
    
    # Custom CSS with simplified animations
    st.markdown("""
    <style>
        /* Title styling */
        .title {
            text-align: center;
            color: #2c3e50;
            font-size: 2.5em;
            margin: 20px 0;
            background: linear-gradient(45deg, #3498db, #2ecc71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 20px;
        }
        
        /* Experiment container */
        .experiment-container {
            width: 100%;
            height: 300px;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        
        /* Beaker styling */
        .beaker {
            width: 120px;
            height: 180px;
            border: 4px solid #333;
            border-radius: 5px 5px 15px 15px;
            position: relative;
            background: transparent;
            overflow: hidden;
        }
        
        /* Solution in beaker */
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 182, 193, 0.6);
        }
        
        /* Spoon styling */
        .spoon {
            position: absolute;
            right: calc(50% - 100px);
            top: 30%;
            transform-origin: right center;
        }
        
        .spoon-normal {
            transform: rotate(0deg);
            transition: transform 1s ease;
        }
        
        .spoon-pour {
            transform: rotate(45deg);
            transition: transform 1s ease;
        }
        
        .spoon-handle {
            width: 80px;
            height: 8px;
            background: #666;
            border-radius: 4px;
        }
        
        .spoon-bowl {
            position: absolute;
            left: -20px;
            top: -10px;
            width: 30px;
            height: 30px;
            background: #666;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 0.8em;
        }
        
        /* Reaction animation */
        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s ease-out infinite;
        }
        
        @keyframes rise {
            0% {
                transform: translateY(0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translateY(-200px) scale(0);
                opacity: 0;
            }
        }
        
        /* Label styling */
        .label {
            position: absolute;
            bottom: -25px;
            width: 100%;
            text-align: center;
            font-weight: bold;
        }
        
        /* Equation styling */
        .equation {
            text-align: center;
            font-size: 1.2em;
            margin: 20px 0;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display title
    st.markdown('<h1 class="title">Baking Soda and Vinegar Reaction</h1>', unsafe_allow_html=True)

    # Container for experiment visualization
    exp_container = st.empty()

    def show_initial_state():
        exp_container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="solution"></div>
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon spoon-normal">
                    <div class="spoon-handle"></div>
                    <div class="spoon-bowl">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def show_pouring():
        exp_container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="solution"></div>
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon spoon-pour">
                    <div class="spoon-handle"></div>
                    <div class="spoon-bowl">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def show_reaction():
        bubbles = "".join([
            f'<div class="bubble" style="left: {i*20}%; bottom: 50%; width: 10px; height: 10px; animation-delay: {i*0.2}s"></div>'
            for i in range(5)
        ])
        
        exp_container.markdown(f"""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="solution"></div>
                    {bubbles}
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon spoon-pour">
                    <div class="spoon-handle"></div>
                    <div class="spoon-bowl">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Show initial state
    show_initial_state()

    # Button to start experiment
    if st.button("Start Experiment"):
        # Animation sequence
        show_pouring()
        time.sleep(1)
        show_reaction()
        time.sleep(0.5)
        
        # Show chemical equation
        st.markdown("""
            <div class="equation">
                NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_experiment()
