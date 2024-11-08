import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import json

def create_titration_animation():
    # Custom CSS for the animation
    st.markdown("""
        <style>
        @keyframes wave {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        .wave-text {
            animation: wave 3s infinite linear;
            display: inline-block;
        }
        .apparatus {
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .drop {
            position: absolute;
            width: 10px;
            height: 10px;
            background-color: #87CEEB;
            border-radius: 50%;
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with wave animation
    st.markdown('<h1 class="wave-text">Acid Base Titration</h1>', unsafe_allow_html=True)

    # Create SVG for burette and flask
    svg_code = f"""
    <svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
        <!-- Burette -->
        <rect x="180" y="50" width="40" height="250" fill="#ffffff" stroke="#000000" stroke-width="2"/>
        <path d="M180 300 L170 320 L230 320 L220 300 Z" fill="#ffffff" stroke="#000000" stroke-width="2"/>
        
        <!-- Stopcock -->
        <rect x="195" y="320" width="10" height="20" fill="#000000"/>
        
        <!-- Solution in burette -->
        <rect id="burette-solution" x="182" y="52" width="36" height="246" fill="#87CEEB" opacity="0.7"/>
        
        <!-- Conical Flask -->
        <path d="M150 450 L250 450 L220 350 L180 350 Z" fill="#ffffff" stroke="#000000" stroke-width="2"/>
        
        <!-- Solution in flask -->
        <path id="flask-solution" d="M152 448 L248 448 L218 352 L182 352 Z" fill="#ff69b4" opacity="0.7"/>
        
        <!-- Dropping animation -->
        <circle id="drop" cx="200" cy="340" r="3" fill="#87CEEB" opacity="0">
            <animate id="drop-animation" 
                    attributeName="cy" 
                    from="340" 
                    to="370" 
                    dur="1s" 
                    begin="indefinite"
                    fill="freeze"/>
            <animate attributeName="opacity" 
                    from="1" 
                    to="0" 
                    dur="1s" 
                    begin="indefinite"/>
        </circle>
    </svg>
    """

    # Display the SVG
    st.markdown(svg_code, unsafe_allow_html=True)

    # Start button
    if st.button("Start Experiment"):
        # Simulate titration
        progress = st.progress(0)
        
        # Create pH vs Volume plot
        volume_data = np.linspace(0, 50, 100)
        ph_data = []
        
        fig = go.Figure()
        
        # Initial pH calculation (HCl)
        initial_ph = 1
        
        for vol in volume_data:
            if vol < 25:  # Before equivalence point
                ph = -np.log10(10**(-initial_ph) * (25-vol)/25)
            elif vol == 25:  # At equivalence point
                ph = 7
            else:  # After equivalence point
                ph = 14 + np.log10((vol-25)/25)
            ph_data.append(min(14, max(0, ph)))
        
        fig.add_trace(go.Scatter(x=volume_data, y=ph_data, mode='lines', name='pH curve'))
        fig.update_layout(
            title='pH vs Volume of NaOH added',
            xaxis_title='Volume of NaOH (mL)',
            yaxis_title='pH',
            yaxis_range=[0, 14]
        )
        
        # Add vertical line for equivalence point
        fig.add_vline(x=25, line_dash="dash", line_color="red",
                     annotation_text="Equivalence Point")
        
        # Create placeholder for plot
        plot_placeholder = st.empty()
        
        # Simulate the titration
        for i in range(100):
            # Update progress bar
            progress.progress(i + 1)
            
            # Update plot with current data
            current_fig = go.Figure(fig)
            current_fig.add_trace(
                go.Scatter(x=volume_data[:i+1], y=ph_data[:i+1],
                          mode='lines',
                          line=dict(color='blue'),
                          name='Current pH')
            )
            plot_placeholder.plotly_chart(current_fig)
            
            # Change flask solution color near equivalence point
            if 45 <= i <= 55:
                st.markdown("""
                    <style>
                    #flask-solution { fill: purple !important; }
                    </style>
                """, unsafe_allow_html=True)
            
            time.sleep(0.1)

        st.success("Titration Complete!")
        st.markdown("""
        ### Results:
        - Equivalence point reached at 25.0 mL
        - Initial pH: 1.0
        - Final pH: 13.0
        - Color change observed at pH ≈ 7.0
        """)

if __name__ == "__main__":
    st.set_page_config(page_title="Acid-Base Titration Simulation")
    create_titration_animation()
