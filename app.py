import streamlit as st
import time
import random
import numpy as np

def main():
    st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="wide")
    
    # Custom CSS for animations and styling
    st.markdown("""
        <style>
        @keyframes rise {
            0% { height: 50%; }
            100% { height: 200%; }
        }
        @keyframes pour {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(135deg); }
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            font-size: 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
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
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        """, unsafe_allow_html=True)

    # Animated title
    st.markdown('<p class="title">Elephant Toothpaste Reaction</p>', unsafe_allow_html=True)

    # Create two columns for the beakers
    col1, col2 = st.columns(2)

    # Initial state
    if 'reaction_state' not in st.session_state:
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 50

    def draw_beaker(label, color, rotation=0):
        return f"""
        <div style="position: relative; width: 100px; height: 150px; margin: auto;">
            <div style="
                position: absolute;
                width: 80px;
                height: 120px;
                border: 3px solid #333;
                border-top: none;
                background: transparent;
                transform: rotate({rotation}deg);
                transform-origin: bottom right;
                transition: transform 1s;">
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: 50%;
                    background-color: {color};
                    transition: height 2s;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
                {label}
            </div>
        </div>
        """

    def draw_cylinder(foam_height):
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        foam_color = random.choice(colors)
        return f"""
        <div style="position: relative; width: 150px; height: 200px; margin: auto;">
            <div style="
                position: absolute;
                width: 120px;
                height: 180px;
                border: 3px solid #333;
                border-top: none;
                background: transparent;">
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {foam_height}%;
                    background: linear-gradient(45deg, {foam_color}, white);
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
        st.markdown(draw_beaker("H₂O₂", "#ADD8E6", 
                              135 if st.session_state.reaction_state == 'pouring' else 0), 
                   unsafe_allow_html=True)

    with col2:
        st.markdown(draw_cylinder(st.session_state.foam_height), unsafe_allow_html=True)

    # Center the button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Experiment"):
            st.session_state.reaction_state = 'pouring'
            
            # Simulate pouring and reaction
            time.sleep(1)  # Pour animation
            st.session_state.foam_height = 200  # Foam rises
            st.experimental_rerun()

    # Display chemical equation
    if st.session_state.reaction_state == 'pouring':
        st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #f0f0f0; border-radius: 10px;'>
            <h3>Chemical Equation:</h3>
            <p style='font-size: 24px;'>2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        **Note:** For a more dramatic effect in real experiments:
        - Add a few drops of food coloring to create colorful foam
        - Mix in liquid soap to create more voluminous foam
        - Always perform under proper supervision and safety conditions
        """)

        # Reset button state for next experiment
        time.sleep(2)
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 50

if __name__ == "__main__":
    main()
