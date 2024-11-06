import streamlit as st
import time
from PIL import Image
import numpy as np
import io
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

def create_scene(stage=0):
    """Create the reaction scene at different stages"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    
    # Draw beaker
    beaker = Rectangle((-2, -3), 4, 4, fill=False, color='black')
    ax.add_patch(beaker)
    
    # Draw liquid (vinegar)
    vinegar = Rectangle((-2, -3), 4, 2, color='lightcoral', alpha=0.3)
    ax.add_patch(vinegar)
    
    if stage >= 1:  # Draw spoon position based on stage
        spoon_y = 2 - (stage * 0.5)  # Move spoon down as stage increases
        spoon = Rectangle((-1, spoon_y), 2, 0.3, color='gray', angle=-stage*15)
        ax.add_patch(spoon)
        
        # Draw baking soda on spoon
        if stage < 3:
            baking_soda = Circle((0, spoon_y + 0.2), 0.3, color='lightgray')
            ax.add_patch(baking_soda)
    
    if stage >= 3:  # Show reaction
        # Add bubbles
        for _ in range(20):
            x = np.random.uniform(-1.8, 1.8)
            y = np.random.uniform(-1, 2)
            size = np.random.uniform(0.1, 0.4)
            bubble = Circle((x, y), size, color='white', alpha=0.6)
            ax.add_patch(bubble)
    
    ax.axis('off')
    return fig

# Set page config
st.set_page_config(page_title="Baking Soda and Vinegar Reaction", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #2c3e50;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .chemical-equation {
        text-align: center;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        margin: 20px 0;
        font-size: 1.2rem;
    }
    
    .stButton>button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with animation
st.markdown('<h1 class="title">Baking Soda and Vinegar Reaction</h1>', unsafe_allow_html=True)

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'reaction_complete' not in st.session_state:
    st.session_state.reaction_complete = False

# Chemical formulas
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Vinegar")
    st.latex("CH_3COOH")
with col2:
    st.markdown("### Baking Soda")
    st.latex("NaHCO_3")

# Main reaction display
reaction_container = st.empty()

# Button and animation logic
if st.button("Start Experiment", disabled=st.session_state.stage > 0):
    for i in range(5):
        st.session_state.stage = i
        fig = create_scene(i)
        reaction_container.pyplot(fig)
        plt.close(fig)
        time.sleep(0.5)
    st.session_state.reaction_complete = True

# Default display if no animation is running
if st.session_state.stage == 0:
    fig = create_scene(0)
    reaction_container.pyplot(fig)
    plt.close(fig)

# Show chemical equation after reaction
if st.session_state.reaction_complete:
    st.markdown('<div class="chemical-equation">', unsafe_allow_html=True)
    st.latex(r"NaHCO_3 (s) + CH_3COOH (aq) \rightarrow CO_2 (g) + H_2O (l) + NaCH_3COO (aq)")
    st.markdown('</div>', unsafe_allow_html=True)

# Reset button
if st.session_state.reaction_complete:
    if st.button("Reset Experiment"):
        st.session_state.stage = 0
        st.session_state.reaction_complete = False
        st.experimental_rerun()
