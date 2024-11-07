import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import time
from PIL import Image
import base64
import io

def create_titration_curve(volume_naoh):
    # Calculate pH values for titration curve
    volumes = np.linspace(0, 50, 100)
    pHs = []
    
    for v in volumes:
        if v < 25:  # Before equivalence point
            h_conc = (0.1 * 25 - 0.1 * v) / (25 + v)
            pH = -np.log10(h_conc)
        elif v == 25:  # At equivalence point
            pH = 7
        else:  # After equivalence point
            oh_conc = (0.1 * (v - 25)) / (25 + v)
            pH = 14 + np.log10(oh_conc)
        pHs.append(pH)
    
    return volumes, pHs

def main():
    # Page config
    st.set_page_config(page_title="Acid-Base Titration Simulation", layout="wide")
    
    # Custom CSS for animations
    st.markdown("""
        <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .bouncing-text {
            animation: bounce 2s infinite;
            display: inline-block;
        }
        .stButton>button {
            width: 200px;
            height: 50px;
            font-size: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Animated title
    st.markdown('<h1 class="bouncing-text">Acid-Base Titration</h1>', unsafe_allow_html=True)
    
    # Initial setup description
    st.markdown("### Experiment Setup")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📝 Initial Conditions:")
        st.write("• Burette: 0.1M NaOH")
        st.write("• Conical Flask: 25mL of 0.1M HCl")
    
    # Create a placeholder for the animation
    animation_placeholder = st.empty()
    result_placeholder = st.empty()
    graph_placeholder = st.empty()
    
    # Start experiment button
    if st.button("Start Experiment"):
        # Show initial setup
        animation_placeholder.info("🔬 Setting up the experiment...")
        time.sleep(1)
        
        # Simulate drops and color change
        for i in range(1, 6):
            animation_placeholder.warning(f"""
            ⚗️ Adding NaOH... Drop {i}
            
            Burette: {'▼' * i}
            Flask: {'🌸' * i}
            """)
            time.sleep(1)
        
        # Show completion message
        result_placeholder.success("🎉 Endpoint reached! The solution has turned pink!")
        
        # Generate and display titration curve
        volumes, pHs = create_titration_curve(25)
        
        fig = go.Figure()
        
        # Add titration curve
        fig.add_trace(go.Scatter(
            x=volumes,
            y=pHs,
            mode='lines',
            name='pH Curve',
            line=dict(color='blue', width=2)
        ))
        
        # Add endpoint marker
        fig.add_trace(go.Scatter(
            x=[25],
            y=[7],
            mode='markers',
            name='Endpoint',
            marker=dict(color='red', size=12)
        ))
        
        # Update layout
        fig.update_layout(
            title='Titration Curve: HCl vs NaOH',
            xaxis_title='Volume of NaOH added (mL)',
            yaxis_title='pH',
            hovermode='x',
            showlegend=True,
            width=800,
            height=500
        )
        
        # Add vertical line at endpoint
        fig.add_vline(x=25, line_dash="dash", line_color="gray")
        
        # Show the plot
        graph_placeholder.plotly_chart(fig)
        
        # Add explanation
        st.markdown("""
        ### Explanation of the Titration Curve:
        
        1. **Initial pH**: The solution starts acidic (pH < 7) due to HCl
        2. **Equivalence Point**: Occurs at 25mL when moles of acid = moles of base
        3. **Buffer Region**: The curve is steepest near the equivalence point
        4. **Final pH**: The solution becomes basic (pH > 7) after the equivalence point
        """)

if __name__ == "__main__":
    main()
