import streamlit as st
import time
import random

def main():
    st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="wide")

    # Enhanced CSS for better animations
    st.markdown("""
        <style>
        @keyframes rise {
            0% { height: 10%; opacity: 0.7; }
            50% { height: 180%; opacity: 0.9; }
            100% { height: 250%; opacity: 1; }
        }
        @keyframes bubble {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        @keyframes pour {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(-40px, 40px) rotate(45deg); }
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
            margin-bottom: 30px;
        }
        .foam-bubble {
            position: absolute;
            border-radius: 50%;
            animation: bubble 1s ease-in-out infinite;
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

    # Initialize session state
    if 'reaction_state' not in st.session_state:
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 10
        st.session_state.foam_colors = []

    def generate_foam_colors():
        base_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA500', '#FF69B4']
        return [random.choice(base_colors) for _ in range(5)]

    def draw_beaker(label, color, pouring=False):
        transform = "translate(-40px, 40px) rotate(45deg)" if pouring else "translate(0, 0) rotate(0deg)"
        return f"""
        <div style="position: relative; width: 100px; height: 150px; margin: auto; margin-bottom: 20px;">
            <div style="
                position: absolute;
                width: 80px;
                height: 120px;
                border: 3px solid #333;
                border-top: none;
                background: transparent;
                transform: {transform};
                transition: transform 1s ease-in-out;">
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {50 if not pouring else 20}%;
                    background-color: {color};
                    transition: all 1s ease-in-out;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; left: 50%; transform: translateX(-50%); text-align: center;">
                {label}
            </div>
        </div>
        """

    def draw_cylinder(foam_height, foam_colors):
        bubbles = ""
        if foam_height > 50:
            for i in range(5):
                left = random.randint(0, 80)
                delay = random.random()
                bubbles += f"""
                <div class="foam-bubble" style="
                    left: {left}px;
                    top: {random.randint(20, 150)}px;
                    width: {random.randint(10, 25)}px;
                    height: {random.randint(10, 25)}px;
                    background-color: {random.choice(foam_colors)};
                    animation-delay: {delay}s;">
                </div>"""

        return f"""
        <div style="position: relative; width: 150px; height: 300px; margin: auto;">
            <div style="
                position: absolute;
                width: 120px;
                height: 180px;
                border: 3px solid #333;
                border-top: none;
                background: transparent;
                overflow: visible;">
                {bubbles}
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {foam_height}%;
                    background: linear-gradient(45deg, {', '.join(foam_colors)});
                    animation: rise 2s ease-out;
                    transition: height 2s;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
                30% KI solution
            </div>
        </div>
        """

    # Layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(draw_beaker("H₂O₂", "#ADD8E6", pouring=(st.session_state.reaction_state == 'pouring')), 
                   unsafe_allow_html=True)
    with col2:
        st.markdown(draw_cylinder(st.session_state.foam_height, st.session_state.foam_colors), 
                   unsafe_allow_html=True)

    # Central button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Experiment") and st.session_state.reaction_state == 'ready':
            st.session_state.reaction_state = 'pouring'
            st.session_state.foam_colors = generate_foam_colors()
            time.sleep(0.5)  # Short pause for pour animation
            st.session_state.foam_height = 250  # Dramatic foam rise
            st.experimental_rerun()

    # Display reaction information
    if st.session_state.reaction_state == 'pouring':
        st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #f0f0f0; border-radius: 10px;
             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); animation: fadeIn 1s ease-in;'>
            <h3 style='color: #2C3E50;'>Chemical Equation:</h3>
            <p style='font-size: 24px; color: #34495E; font-family: "Computer Modern", serif;'>
                2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        💡 **Experiment Enhancement Tips:**
        1. Add a few drops of food coloring for vibrant, colorful foam
        2. Mix in liquid soap to create more voluminous, lasting foam
        3. For best results, use 30% hydrogen peroxide
        
        ⚠️ **Safety Note:** Always perform under proper supervision and safety conditions. 
        Wear protective gear and conduct in a well-ventilated area.
        """)

        # Reset state for repeat experiment
        time.sleep(2)
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 10

if __name__ == "__main__":
    main()
