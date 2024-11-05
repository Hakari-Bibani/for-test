import streamlit as st
import time
import random

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

    # Pouring Animation
    st.markdown(
        """
        <style>
        @keyframes pour {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(45deg); }
        }
        .beaker {
            animation: pour 1s forwards;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Delay to simulate pouring time
    time.sleep(1)
    
    # Reaction Animation - Simulate foam rising
    reaction_height = 50
    st.write("## Reaction Occurring...")
    st.markdown(
        f"""
        <style>
        .reaction-container {{
            width: 150px; 
            height: 250px; 
            border: 2px solid #666; 
            border-radius: 10px; 
            position: relative; 
            margin-top: 20px;
            background: repeating-linear-gradient(
                180deg,
                #FFC0CB,
                #FFC0CB 10px,
                #FFFFFF 10px,
                #FFFFFF 20px
            );
        }}
        </style>
        <div class="reaction-container"></div>
        """,
        unsafe_allow_html=True
    )
    
    for i in range(0, 15):
        reaction_height += random.randint(10, 30)
        st.markdown(
            f"""
            <div class="reaction-container" style="height: {reaction_height}px;"></div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.2)

    # Display Final Reaction Result
    st.write("### Reaction Complete!")
    st.markdown(
        """
        **Reaction:** 2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
        
        *Food coloring and liquid soap can be added for extra effect.*
        """,
        unsafe_allow_html=True
    )
