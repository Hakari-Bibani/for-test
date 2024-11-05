import streamlit as st
import time
import random
import numpy as np

def main():
    st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="wide")
    
    # Enhanced CSS for animations and styling
    st.markdown("""
        <style>
        @keyframes rise {
            0% { height: 10%; }
            50% { height: 180%; }
            75% { height: 160%; }
            100% { height: 170%; }
        }
        @keyframes pour {
            0% { transform: rotate(0deg) translateX(0); }
            100% { transform: rotate(75deg) translateX(100px); }
        }
        @keyframes bubble {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        @keyframes colorChange {
            0% { background: linear-gradient(45deg, #FF6B6B, #FF6B6B); }
            33% { background: linear-gradient(45deg, #4ECDC4, #4ECDC4); }
            66% { background: linear-gradient(45deg, #45B7D1, #45B7D1); }
            100% { background: linear-gradient(45deg, #FF6B6B, #FF6B6B); }
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            font-size: 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .title {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            animation: gradient 3s ease infinite;
        }
        .foam {
            animation: rise 2s ease-out forwards, colorChange 4s infinite, bubble 2s infinite;
        }
        .pouring {
            animation: pour 1s ease-out forwards;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        """, unsafe_allow_html=True)

    # Animated title
    st.markdown('<p class="title">Elephant Toothpaste Reaction</p>', unsafe_allow_html=True)

    # Create columns for the beakers
    col1, col2 = st.columns([1, 1])

    # Initial state
    if 'reaction_state' not in st.session_state:
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 10

    def draw_beaker(label, color, rotation=0):
        animation_class = "pouring" if st.session_state.reaction_state == 'pouring' else ""
        return f"""
        <div style="position: relative; width: 150px; height: 200px; margin: auto;">
            <div class="{animation_class}" style="
                position: absolute;
                width: 100px;
                height: 150px;
                border: 4px solid #333;
                border-top: none;
                background: transparent;
                transform-origin: bottom right;
                transition: transform 1s;">
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {50 if st.session_state.reaction_state == 'ready' else 10}%;
                    background-color: {color};
                    transition: height 1s;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
                {label}
            </div>
        </div>
        """

    def draw_cylinder(foam_height):
        foam_class = "foam" if st.session_state.reaction_state == 'pouring' else ""
        return f"""
        <div style="position: relative; width: 150px; height: 300px; margin: auto;">
            <div style="
                position: absolute;
                width: 120px;
                height: 250px;
                border: 4px solid #333;
                border-top: none;
                background: transparent;
                overflow: visible;">
                <div class="{foam_class}" style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {foam_height}%;
                    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
                    transition: height 2s;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
                30% KI solution
            </div>
        </div>
        """

    # Display beakers and cylinder
    with col1:
        st.markdown(draw_beaker("H₂O₂", "#ADD8E6"), unsafe_allow_html=True)

    with col2:
        st.markdown(draw_cylinder(st.session_state.foam_height), unsafe_allow_html=True)

    # Center the button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Experiment"):
            st.session_state.reaction_state = 'pouring'
            
            # Simulate pouring and reaction
            time.sleep(1)  # Pour animation
            st.session_state.foam_height = 170  # Foam rises
            st.experimental_rerun()

    # Display chemical equation and information
    if st.session_state.reaction_state == 'pouring':
        st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #f0f0f0; border-radius: 10px;'>
            <h3>Chemical Equation:</h3>
            <p style='font-size: 24px;'>2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        **Reaction Details:**
        - The hydrogen peroxide (H₂O₂) decomposes rapidly when catalyzed by potassium iodide (KI)
        - Oxygen gas is released, creating the dramatic foaming effect
        - The foam contains thousands of tiny oxygen bubbles
        - The reaction is exothermic, releasing heat in the process
        """)

        # Reset button state for next experiment
        time.sleep(2)
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 10
        st.experimental_rerun()

if __name__ == "__main__":
    main()
