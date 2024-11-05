import streamlit as st
import time
import random

def main():
    st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="wide")

    # Enhanced CSS for animations
    st.markdown("""
        <style>
        @keyframes rise {
            0% { height: 10%; opacity: 0.7; }
            50% { height: 300%; opacity: 0.9; }
            100% { height: 400%; opacity: 1; }
        }
        @keyframes bubble {
            0% { transform: scale(1) translateY(0); }
            50% { transform: scale(1.2) translateY(-20px); }
            100% { transform: scale(1) translateY(0); }
        }
        @keyframes pour {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(25deg); }
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
            margin-bottom: 30px;
        }
        .foam-bubble {
            position: absolute;
            border-radius: 50%;
            animation: bubble 2s ease-in-out infinite;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="title">Elephant Toothpaste Reaction</p>', unsafe_allow_html=True)

    # Initialize session state
    if 'reaction_state' not in st.session_state:
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 10

    def generate_foam_colors():
        base_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA500', '#FF69B4']
        return [random.choice(base_colors) for _ in range(5)]

    def draw_beaker(label, color, pouring=False):
        rotation = "rotate(25deg)" if pouring else "none"
        return f"""
        <div style="position: relative; width: 100px; height: 150px; margin: auto;">
            <div style="
                position: absolute;
                width: 80px;
                height: 120px;
                border: 3px solid #333;
                border-top: none;
                background: transparent;
                transform: {rotation};
                transition: transform 1s;">
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {50 if not pouring else 20}%;
                    background-color: {color};
                    transition: height 1s;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
                {label}
            </div>
        </div>
        """

    def draw_cylinder(foam_height, foam_colors):
        bubbles = ""
        if foam_height > 50:
            for i in range(5):
                left = random.randint(0, 120)
                delay = random.random()
                size = random.randint(15, 40)
                bubbles += f"""
                <div class="foam-bubble" style="
                    left: {left}px;
                    bottom: {random.randint(0, 200)}px;
                    width: {size}px;
                    height: {size}px;
                    background-color: {random.choice(foam_colors)};
                    animation-delay: {delay}s;">
                </div>"""

        return f"""
        <div style="position: relative; width: 150px; height: 250px; margin: auto;">
            <div style="
                position: absolute;
                width: 120px;
                height: 200px;
                border: 3px solid #333;
                border-top: none;
                background: transparent;">
                {bubbles}
                <div style="
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    height: {foam_height}%;
                    background: linear-gradient(45deg, {', '.join(foam_colors)});
                    animation: rise 3s ease-out;
                    transition: height 2s;">
                </div>
            </div>
            <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
                30% KI solution
            </div>
        </div>
        """

    # Display beaker and cylinder
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(draw_beaker("H₂O₂", "#ADD8E6", pouring=(st.session_state.reaction_state == 'pouring')), 
                    unsafe_allow_html=True)
    with col2:
        foam_colors = generate_foam_colors()
        st.markdown(draw_cylinder(st.session_state.foam_height, foam_colors), 
                    unsafe_allow_html=True)

    # Central button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Experiment") and st.session_state.reaction_state == 'ready':
            st.session_state.reaction_state = 'pouring'
            st.session_state.foam_height = 400  # Simulate foam rising
            st.experimental_rerun()

    # Display reaction information after reaction
    if st.session_state.reaction_state == 'pouring':
        st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #f0f0f0; border-radius: 10px;'>
            <h3 style='color: #2C3E50;'>Chemical Equation:</h3>
            <p style='font-size: 24px; color: #34495E;'>
                2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
        **Experiment Enhancement Tips:**
        - Add food coloring for vibrant foam
        - Use liquid soap for more foam
        - Use 30% hydrogen peroxide for best results
        """)

        # Reset state for repeat experiment
        time.sleep(2)
        st.session_state.reaction_state = 'ready'
        st.session_state.foam_height = 10

if __name__ == "__main__":
    main()
