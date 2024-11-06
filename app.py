import streamlit as st
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import time

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Custom CSS for animation
st.markdown("""
    <style>
    @keyframes moveText {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    .moving-text {
        animation: moveText 10s linear infinite;
        white-space: nowrap;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# Animated title
st.markdown('<h1 class="moving-text">Acid Base Titration</h1>', unsafe_allow_html=True)

# Create two columns for the setup
col1, col2 = st.columns(2)

# Initial setup visualization
with col1:
    st.markdown("""
    ```
       NaOH
    ┌─────────┐
    │         │
    │         │ Burette
    │         │
    └────┬────┘
         │
         V
    
    """)

with col2:
    st.markdown("""
    ```
         HCl
    ┌─────────┐
    │         │
    │         │ Flask
    │         │
    └─────────┘
    """)

# Start experiment button
start_experiment = st.button("Start Experiment")

if start_experiment:
    # Animation of titration
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        progress_bar.progress(i)
        if i < 80:
            status_text.text(f"Adding NaOH... ({i}%)")
        else:
            status_text.text("Color changing to pink!")
        time.sleep(0.1)
    
    # Generate titration curve data
    volume = np.linspace(0, 50, 100)
    initial_ph = 1  # Initial pH of strong acid
    equivalence_point = 25  # Volume at equivalence point
    
    def calculate_ph(v):
        if v < equivalence_point:
            return -np.log10(abs(0.1 - (0.1 * v/equivalence_point)))
        elif abs(v - equivalence_point) < 0.1:
            return 7
        else:
            return 14 + np.log10(abs((0.1 * (v-equivalence_point))/v))
    
    ph = [calculate_ph(v) for v in volume]
    
    # Create titration curve
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=volume,
        y=ph,
        mode='lines',
        name='pH curve'
    ))
    
    # Add equivalence point marker
    fig.add_trace(go.Scatter(
        x=[equivalence_point],
        y=[calculate_ph(equivalence_point)],
        mode='markers',
        marker=dict(size=10, color='red'),
        name='Equivalence Point'
    ))
    
    # Update layout
    fig.update_layout(
        title='Titration Curve: HCl vs NaOH',
        xaxis_title='Volume of NaOH added (mL)',
        yaxis_title='pH',
        showlegend=True
    )
    
    # Display the plot
    st.plotly_chart(fig, use_container_width=True)
    
    # Show equivalence point details
    st.success(f"""
        Titration Complete!
        - Equivalence Point reached at {equivalence_point} mL
        - pH at equivalence point: 7.0
        """)

# Add explanation
st.markdown("""
### How it works:
1. The burette contains NaOH (strong base)
2. The conical flask contains HCl (strong acid)
3. As NaOH is added, the pH gradually increases
4. At the equivalence point, the solution turns pink due to phenolphthalein indicator
5. The curve shows the pH change throughout the titration
""")
