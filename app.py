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
            color: #1e90ff;
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(45deg, #ff6347, #32cd32, #1e90ff, #ff8c00);
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
            background: rgba(173, 216, 230, 0.7); /* Pale blue water */
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            overflow: hidden;
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
            background: #696969;
            border-radius: 10px;
            position: absolute;
            left: 50%;
            top: 80px;
            transform-origin: center right;
            transform: translateX(-50%);
            transition: transform 1s;
        }
        .spoon-content {
            font-size: 14px;
            color: #fff;
            background-color: #000;
            padding: 5px;
            border-radius: 50%;
            position: absolute;
            right: -30px;
            top: -10px;
        }
        .pouring {
            transform: translateX(-50%) rotate(-45deg);
        }
        .spark {
            width: 50px;
            height: 50px;
            background: radial-gradient(circle, #ff4500, transparent);
            position: absolute;
            left: 50%;
            top: 80px;
            transform: translateX(-50%);
            opacity: 0;
            animation: explosion 0.5s ease-out forwards;
        }
        @keyframes explosion {
            0% { opacity: 1; transform: translateX(-50%) scale(0.5); }
            100% { opacity: 0; transform: translateX(-50%) scale(1.5); }
        }
        .boom-text {
            font-size: 2.5em;
            font-weight: bold;
            color: red;
            text-align: center;
            opacity: 0;
            animation: boom 1s ease-out forwards;
        }
        @keyframes boom {
            0% { opacity: 0; transform: scale(0.5); }
            100% { opacity: 1; transform: scale(1.5); }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Sodium and Water Reaction</h1>", unsafe_allow_html=True)

    # Container for the experiment setup
    container = st.empty()

    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O</div>
                </div>
                <div class="spoon">
                    <div class="spoon-content">Na</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def animate_experiment():
        # Step 1: Animate the spoon bending and pouring Na into the beaker
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O</div>
                </div>
                <div class="spoon pouring">
                    <div class="spoon-content">Na</div>
                </div>
                <div class="spark"></div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1)  # Pause to show the bending and reaction

        # Step 2: Show the dramatic reaction and "BOOM" text
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O</div>
                </div>
                <div class="boom-text">BOOM!</div>
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
            2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)
        """)

if __name__ == "__main__":
    run_experiment()
