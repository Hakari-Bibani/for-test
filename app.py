import streamlit as st
import time

# Title with Wave Animation
st.markdown(
    """
    <style>
    .title-wave {
        font-size: 3em;
        font-weight: bold;
        color: #0066cc;
        animation: wave 2s infinite alternate;
    }

    @keyframes wave {
        0% { transform: translateX(-10px); }
        50% { transform: translateX(10px); }
        100% { transform: translateX(-10px); }
    }
    </style>
    <div class="title-wave">Elephant Toothpaste Reaction</div>
    """, 
    unsafe_allow_html=True
)

# Render Beaker and Cylinder with Initial State
st.write("### Initial Setup")
st.markdown(
    """
    <style>
    .container { display: flex; justify-content: space-around; }
    .beaker, .cylinder {
        width: 100px; height: 200px; 
        border: 2px solid #666; 
        border-radius: 10px; 
        position: relative; 
        overflow: hidden;
    }
    .h2o2 { background-color: lightblue; height: 50%; }
    .ki { background-color: lightgrey; height: 50%; }
    .label { position: absolute; bottom: -20px; left: 0; width: 100%; text-align: center; font-weight: bold; }
    </style>
    <div class="container">
        <div class="beaker">
            <div class="h2o2"></div>
            <div class="label">H₂O₂ Solution</div>
        </div>
        <div class="cylinder">
            <div class="ki"></div>
            <div class="label">30% KI Solution</div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)

# Button to Start Experiment
if st.button("Start Experiment"):
    st.write("### Reaction In Progress")

    # Pouring and Reaction Animation
    st.markdown(
        """
        <style>
        .reaction-container {
            width: 150px;
            height: 250px;
            border: 2px solid #666;
            border-radius: 10px;
            position: relative;
            margin-top: 20px;
            overflow: hidden;
            animation: foam-rise 3s ease-in-out forwards;
        }

        .foam {
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(
                180deg,
                #FFC0CB,
                #FFC0CB 10px,
                #FFFFFF 10px,
                #FFFFFF 20px
            );
            position: absolute;
            bottom: 0;
            transform: translateY(100%);
            animation: foam-animation 3s ease-in-out forwards;
        }

        @keyframes foam-animation {
            0% { transform: translateY(100%); }
            50% { transform: translateY(-50%); }
            100% { transform: translateY(0%); }
        }

        @keyframes foam-rise {
            0% { height: 50px; }
            50% { height: 150px; }
            100% { height: 250px; }
        }
        </style>
        <div class="reaction-container">
            <div class="foam"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display Final Reaction Result
    time.sleep(3)
    st.write("### Reaction Complete!")
    st.markdown(
        """
        **Reaction:** 2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
        
        *Food coloring and liquid soap can be added for extra effect.*
        """,
        unsafe_allow_html=True
    )
