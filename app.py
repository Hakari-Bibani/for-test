import streamlit as st
import time

# Title of the app
st.title("Elephant Toothpaste Reaction")

# Display the initial setup of the experiment
col1, col2 = st.columns(2)

# Create the beaker and cylinder
with col1:
    st.write("### Beaker (H₂O₂)")
    st.markdown("""
    <div style="height: 200px; width: 100px; background-color: #b0c4de; border: 2px solid #000; position: relative; text-align: center;">
        <div style="position: absolute; top: 70%; width: 100%; font-size: 1.5em;">H₂O₂</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.write("### Cylinder (KI)")
    st.markdown("""
    <div style="height: 300px; width: 80px; background-color: #d3d3d3; border: 2px solid #000; position: relative; text-align: center;">
        <div style="position: absolute; top: 75%; width: 100%; font-size: 1.5em;">KI</div>
    </div>
    """, unsafe_allow_html=True)

# Add a button to start the experiment
if st.button("Start Experiment"):
    # Simulate the reaction start with a brief delay
    time.sleep(1)
    
    # Use JavaScript and CSS for a beaker pouring effect
    st.markdown("""
    <style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .beaker {
        height: 200px;
        width: 100px;
        background-color: #b0c4de;
        border: 2px solid #000;
        position: relative;
        transform: rotate(-45deg);
        transition: transform 1s;
    }
    .beaker-label {
        position: absolute;
        top: 70%;
        width: 100%;
        font-size: 1.5em;
    }
    .cylinder {
        height: 300px;
        width: 80px;
        background-color: #d3d3d3;
        border: 2px solid #000;
        position: relative;
    }
    .reaction {
        height: 0;
        width: 80px;
        background-color: #ff69b4;
        border: 2px solid #000;
        position: relative;
        transition: height 2s ease-in-out;
        overflow: hidden;
    }
    .reaction.animate {
        height: 500px;
    }
    </style>

    <div class="container">
        <div class="beaker">
            <div class="beaker-label">H₂O₂</div>
        </div>
        <div class="cylinder">
            <div class="reaction"></div>
            <div class="beaker-label">KI</div>
        </div>
    </div>

    <script>
    setTimeout(() => {
        // Start the beaker pour animation
        document.querySelector('.beaker').style.transform = 'rotate(0deg)';
        
        // After a slight delay, animate the foam explosion
        setTimeout(() => {
            document.querySelector('.reaction').classList.add('animate');
        }, 1000);
    }, 500);
    </script>
    """, unsafe_allow_html=True)

    # Display chemical equation and additional notes after animation
    time.sleep(2)
    st.subheader("Chemical Equation")
    st.write("2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")

    # Display optional note
    st.write("**Note:** To enhance the visual effect, you can optionally add food coloring and liquid soap.")

# Allow the experiment to be repeated
st.button("Repeat Experiment")
