import streamlit as st
import time

# Set up page configuration
st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="centered")

# Custom CSS for animations and styling
st.markdown("""
<style>
    /* Title styling */
    .title {
        font-size: 2.8em;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
    }

    /* Container styling */
    .experiment-container {
        position: relative;
        height: 300px;
        margin: 20px auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Beaker styling */
    .beaker {
        width: 100px;
        height: 120px;
        border: 4px solid #444;
        border-radius: 5px 5px 10px 10px;
        background: rgba(173, 216, 230, 0.7); /* H2O2 solution color */
        transition: transform 1.5s ease;
        transform-origin: bottom right;
    }
    
    .cylinder {
        width: 140px;
        height: 200px;
        border: 4px solid #444;
        border-radius: 10px 10px 20px 20px;
        background: rgba(200, 200, 200, 0.7); /* KI solution color */
        overflow: hidden;
        position: relative;
    }

    /* Foam eruption */
    @keyframes foam-eruption {
        from { height: 0; }
        to { height: 300px; }
    }

    .foam {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 0;
        background: linear-gradient(to top, #ff6b6b, #ff8e8e, #ffb3b3, #ffd8d8);
        animation: foam-eruption 2s forwards;
    }

    /* Hidden note and equation styling */
    .equation, .note {
        text-align: center;
        font-size: 1.2em;
        opacity: 0;
        transition: opacity 2s ease;
    }
</style>
""", unsafe_allow_html=True)

# Title display
st.markdown("<h1 class='title'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)

# Experiment container
beaker_placeholder = st.empty()
cylinder_placeholder = st.empty()
foam_placeholder = st.empty()

# Button for starting the experiment
if st.button("Start Experiment"):
    # Step 1: Display beaker tilting
    with beaker_placeholder.container():
        st.markdown("""
        <div class="experiment-container">
            <div class="beaker" style="transform: rotate(135deg);"></div>
            <div class="cylinder"></div>
        </div>
        """, unsafe_allow_html=True)
    time.sleep(1.5)  # Pause for pour animation

    # Step 2: Show foam eruption
    foam_placeholder.markdown("""
    <div class="experiment-container">
        <div class="foam"></div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2)  # Allow time for foam to animate

    # Step 3: Display equation and optional note
    st.markdown("""
    <div class="equation" style="opacity: 1;">
        2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
    </div>
    <div class="note" style="opacity: 1;">
        Note: Adding food coloring and liquid soap creates a colorful foam effect!
    </div>
    """, unsafe_allow_html=True)
    
# Reset placeholders to allow rerun
time.sleep(2)
beaker_placeholder.empty()
cylinder_placeholder.empty()
foam_placeholder.empty()
