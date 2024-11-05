import streamlit as st
import time
from indicator import run_experiment

def main():
    st.markdown("<h1 style='text-align: center;'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)

    # Container for the beaker and cylinder visuals
    container = st.container()
    
    with container:
        # Display the initial beaker and cylinder setup
        st.markdown("""
        <style>
            .beaker {
                width: 100px;
                height: 150px;
                position: relative;
                background-color: rgba(176,224,230,0.7);
                border: 3px solid #2c3e50;
                border-radius: 5px;
                display: inline-block;
                margin-right: 30px;
                transform: translateY(-20px);
            }
            .cylinder {
                width: 80px;
                height: 130px;
                background-color: rgba(169,169,169,0.7);
                border: 3px solid #2c3e50;
                border-radius: 10px;
                display: inline-block;
            }
        </style>
        <div class="beaker">H₂O₂</div>
        <div class="cylinder">KI</div>
        """, unsafe_allow_html=True)

    # Add "Start Experiment" button
    if st.button("Start Experiment"):
        # Animate beaker tilting and pouring
        st.markdown("""
        <style>
            @keyframes tiltPour {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(45deg); }
            }
            .beaker-tilt {
                animation: tiltPour 2s forwards;
            }
            .foam {
                position: absolute;
                bottom: 0;
                left: 50%;
                width: 30px;
                height: 200px;
                background: linear-gradient(to top, #ff6347, #ffa07a, #f08080);
                animation: foamExplosion 3s ease-in-out forwards;
            }
            @keyframes foamExplosion {
                0% { height: 30px; opacity: 1; }
                50% { height: 200px; opacity: 0.9; }
                100% { height: 350px; opacity: 0.5; }
            }
        </style>
        <div class="beaker beaker-tilt"></div>
        <div class="cylinder">
            <div class="foam"></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Chemical equation after the reaction
        time.sleep(3)
        st.markdown("### Reaction Equation")
        st.markdown("2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")

        # Note about food coloring and liquid soap
        st.info("Optional: Add food coloring and liquid soap to enhance the reaction's visual effect.")

    # Button to repeat the experiment
    if st.button("Repeat Experiment"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
