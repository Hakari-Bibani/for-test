import streamlit as st
import time

# Custom CSS for animations
st.markdown(
    """
    <style>
        /* Title Wave Animation */
        @keyframes wave {
            0%, 100% { transform: translateX(0); }
            50% { transform: translateX(10px); }
        }
        .title {
            font-size: 2.5em;
            color: #2e86c1;
            animation: wave 1s infinite alternate;
        }

        /* Container for the beaker and cylinder */
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            margin-top: 50px;
        }

        /* Beaker and Cylinder styling */
        .beaker, .cylinder {
            width: 100px;
            height: 200px;
            position: relative;
            border: 3px solid #888;
            border-radius: 8px;
            overflow: hidden;
        }

        /* H2O2 and KI solutions */
        .h2o2-solution {
            width: 100%;
            height: 50%;
            background-color: #add8e6; /* Light blue color for H2O2 */
            position: absolute;
            bottom: 0;
        }

        .ki-solution {
            width: 100%;
            height: 50%;
            background-color: #d3d3d3; /* Light grey color for KI */
            position: absolute;
            bottom: 0;
        }

        /* Pouring animation */
        .pour {
            position: absolute;
            width: 10px;
            height: 50px;
            background-color: #add8e6;
            animation: pour 2s forwards;
        }

        @keyframes pour {
            0% { transform: translateY(-100px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }

        /* Reaction (Foam rise and fall) animation */
        .reaction {
            position: absolute;
            width: 100%;
            background: linear-gradient(180deg, #ff4d4d, #ffcc99, #ffff66);
            bottom: 0;
            height: 0;
            animation: foam 2s forwards;
            animation-delay: 2s;
        }

        @keyframes foam {
            0% { height: 0; }
            50% { height: 300px; }
            100% { height: 0; }
        }

        /* Notes text */
        .notes {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<h1 class="title">Elephant Toothpaste Reaction</h1>', unsafe_allow_html=True)

# Display beaker and cylinder with solutions
st.markdown(
    """
    <div class="container">
        <div class="beaker">
            <div class="h2o2-solution"></div>
        </div>
        <div class="cylinder">
            <div class="ki-solution"></div>
            <p style="text-align:center; margin-top: 210px; color: #555;">30% KI Solution</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Button to start experiment
if st.button("Start Experiment"):
    st.markdown(
        """
        <div class="container">
            <div class="beaker">
                <div class="h2o2-solution"></div>
                <div class="pour"></div> <!-- Pouring animation -->
            </div>
            <div class="cylinder">
                <div class="reaction"></div> <!-- Reaction animation -->
                <p style="text-align:center; margin-top: 210px; color: #555;">30% KI Solution</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Display notes
    st.markdown(
        """
        <div class="notes">
            <p>2H<sub>2</sub>O<sub>2</sub> (aq) → 2H<sub>2</sub>O (l) + O<sub>2</sub> (g)</p>
            <p>Food coloring and liquid soap can be added</p>
        </div>
        """,
        unsafe_allow_html=True
    )
