import streamlit as st
import time

# Custom CSS for styling and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');

    .title {
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.8em;
        color: #2c3e50;
        text-align: center;
        background: linear-gradient(45deg, #ff5f6d, #ffc371);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .beaker {
        width: 120px;
        height: 150px;
        background: rgba(255, 200, 200, 0.4);
        border: 3px solid #ddd;
        border-radius: 10px;
        position: relative;
        margin: 20px auto;
        overflow: hidden;
    }

    .solution {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 50%;
        background: palevioletred;
        border-radius: 0 0 10px 10px;
    }

    .spoon {
        position: absolute;
        top: -50px;
        left: 70px;
        width: 100px;
        height: 20px;
        background: lightgray;
        border-radius: 10px;
        transform-origin: right;
        transition: transform 1s ease-in-out;
    }

    .bubbles {
        position: absolute;
        bottom: 10px;
        width: 100%;
        height: 200px;
        animation: bubblesRise 2s forwards;
    }

    @keyframes bubblesRise {
        0% { opacity: 0; transform: translateY(0); }
        100% { opacity: 1; transform: translateY(-200px); }
    }

    .equation {
        font-family: 'Rajdhani', sans-serif;
        text-align: center;
        font-size: 1.2em;
        margin-top: 20px;
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

# Title with animation
st.markdown("<h1 class='title'>Baking Soda and Vinegar Reaction</h1>", unsafe_allow_html=True)

# Create placeholders for the beaker, spoon, and animation
beaker_placeholder = st.empty()
spoon_placeholder = st.empty()
bubbles_placeholder = st.empty()
equation_placeholder = st.empty()

def render_initial_state():
    # Initial beaker and spoon setup
    beaker_placeholder.markdown("""
        <div class='beaker'>
            <div class='solution'></div>
        </div>
    """, unsafe_allow_html=True)

    spoon_placeholder.markdown("""
        <div class='spoon' style='transform: rotate(0deg);'></div>
        <div style='text-align: center; margin-top: -30px; font-weight: bold;'>NaHCO₃</div>
    """, unsafe_allow_html=True)

def animate_experiment():
    # Animate the spoon bending
    spoon_placeholder.markdown("""
        <div class='spoon' style='transform: rotate(45deg);'></div>
        <div style='text-align: center; margin-top: -30px; font-weight: bold;'>NaHCO₃</div>
    """, unsafe_allow_html=True)
    time.sleep(1)

    # Display the bubbles rising from the beaker
    bubbles_placeholder.markdown("""
        <div class='bubbles'>
            <img src='https://i.ibb.co/6ZtYZx2/bubbles.png' style='width:100%;'>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)

    # Show the chemical equation
    equation_placeholder.markdown("""
        <div class='equation'>NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO</div>
    """, unsafe_allow_html=True)

    # Reset after a pause
    time.sleep(2)
    bubbles_placeholder.empty()
    render_initial_state()

# Initial render
render_initial_state()

# Add button to start the experiment
if st.button("Start Experiment"):
    animate_experiment()
