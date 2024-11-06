import streamlit as st
import time

def run_experiment():
    # Custom CSS for styling and animations
    st.markdown("""
    <style>
        /* ... (previous CSS styles) ... */

        .beaker {
            width: 100px;
            height: 150px;
            border: 3px solid #555;
            border-radius: 5px 5px 10px 10px;
            background: rgba(255, 182, 193, 0.6);
            position: relative;
            overflow: hidden;
        }
        .beaker-fill {
            width: 100px;
            height: 0;
            background: rgba(255, 182, 193, 0.6);
            position: absolute;
            bottom: 0;
            animation: fill 2s ease-in-out forwards;
        }
        @keyframes fill {
            0% { height: 0; }
            100% { height: 75px; }
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
            background: #d3d3d3;
            border-radius: 10px;
            position: absolute;
            right: 30px;
            top: 120px;
            transform-origin: right center;
            animation: pour 1s ease-in-out forwards;
        }
        @keyframes pour {
            0% { transform: rotate(0); }
            100% { transform: rotate(-45deg); }
        }
        .spoon-content {
            font-size: 14px;
            color: #555;
            position: absolute;
            right: -30px;
            top: -10px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #d3d3d3;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .reaction {
            width: 100px;
            height: 75px;
            background: linear-gradient(to top, #ff4757, #2ed573, #1e90ff);
            border-radius: 50% 50% 0 0;
            position: absolute;
            bottom: 0;
            animation: bubbles 2s ease forwards;
        }
        @keyframes bubbles {
            0% { height: 0; }
            100% { height: 75px; }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Baking Soda and Vinegar Reaction</h1>", unsafe_allow_html=True)

    # Container for the experiment setup
    container = st.empty()

    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="beaker-fill"></div>
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon">
                    <div class="spoon-content">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def animate_experiment():
        # Step 1: Animate the spoon pouring
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="beaker-fill"></div>
                    <div class="label">CH₃COOH</div>
                </div>
                <div class="spoon">
                    <div class="spoon-content">NaHCO₃</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1)

        # Step 2: Show the reaction with bubbles
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="beaker-fill"></div>
                    <div class="label">CH₃COOH</div>
                    <div class="reaction"></div>
                </div>
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
            NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
        """)

if __name__ == "__main__":
    run_experiment()
