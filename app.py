import streamlit as st
import time
import base64
from io import BytesIO

def get_svg_content(step):
    svg = f'''
    <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
        <!-- Beaker -->
        <path d="M100 150 L100 350 L300 350 L300 150 L280 150 L280 180 L120 180 L120 150 Z" 
              fill="none" stroke="black" stroke-width="2"/>
        
        <!-- Vinegar solution -->
        <path d="M120 180 L120 350 L280 350 L280 180 Z" 
              fill="#ffcdd2" fill-opacity="0.7"/>
        
        <!-- Spoon -->
        <g transform="rotate({45 if step >= 2 else 0} 250 100)">
            <path d="M200 100 L300 100 L310 90 L300 80 L200 80 Z" 
                  fill="#d3d3d3" stroke="black"/>
            <circle cx="200" cy="90" r="15" fill="#d3d3d3" stroke="black"/>
            {'' if step >= 2 else '<circle cx="250" cy="90" r="10" fill="white" stroke="#d3d3d3"/>'}
        </g>
        
        <!-- Labels -->
        <text x="320" y="95" font-family="sans-serif" font-size="14">NaHCO3</text>
        <text x="320" y="250" font-family="sans-serif" font-size="14">CH3COOH</text>
        
        {'''
        <!-- Falling powder -->
        <path d="M250 120 Q250 200 250 280" stroke="white" stroke-width="4" stroke-dasharray="4,4">
            <animate attributeName="stroke-dashoffset" from="0" to="32" dur="1s" repeatCount="indefinite"/>
        </path>
        ''' if step == 2 else ''}
        
        {'''
        <!-- Bubbles -->
        <g>
            <circle cx="220" cy="300" r="8" fill="white" opacity="0.6">
                <animate attributeName="cy" from="350" to="100" dur="1.5s" repeatCount="indefinite"/>
                <animate attributeName="opacity" from="0.6" to="0" dur="1.5s" repeatCount="indefinite"/>
            </circle>
            <circle cx="240" cy="320" r="6" fill="white" opacity="0.6">
                <animate attributeName="cy" from="350" to="100" dur="1.2s" repeatCount="indefinite"/>
                <animate attributeName="opacity" from="0.6" to="0" dur="1.2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="200" cy="310" r="7" fill="white" opacity="0.6">
                <animate attributeName="cy" from="350" to="100" dur="1.8s" repeatCount="indefinite"/>
                <animate attributeName="opacity" from="0.6" to="0" dur="1.8s" repeatCount="indefinite"/>
            </circle>
            <circle cx="180" cy="330" r="5" fill="white" opacity="0.6">
                <animate attributeName="cy" from="350" to="100" dur="1.3s" repeatCount="indefinite"/>
                <animate attributeName="opacity" from="0.6" to="0" dur="1.3s" repeatCount="indefinite"/>
            </circle>
        </g>
        ''' if step >= 3 else ''}
    </svg>
    '''
    return svg

def main():
    st.set_page_config(page_title="Baking Soda and Vinegar Reaction")
    
    # Title
    st.title("Baking Soda and Vinegar Reaction")
    
    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.animation_complete = False
    
    # Create columns for layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Display SVG
        svg = get_svg_content(st.session_state.step)
        st.components.v1.html(svg, height=400)
        
        # Start button
        if not st.session_state.animation_complete:
            if st.button("Start Experiment"):
                st.session_state.step = 1
                
                # Use empty containers for updating content
                progress_placeholder = st.empty()
                
                # Animation sequence
                for i in range(2, 5):
                    time.sleep(1)  # Delay between steps
                    st.session_state.step = i
                    svg = get_svg_content(st.session_state.step)
                    st.components.v1.html(svg, height=400)
                    
                st.session_state.animation_complete = True
                st.experimental_rerun()
        
        # Show equation after animation
        if st.session_state.animation_complete:
            st.markdown("""
            <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 5px;'>
                <code>NaHCO3 (s) + CH3COOH (aq) → CO2 (g) + H2O (l) + NaCH3COO (aq)</code>
            </div>
            """, unsafe_allow_html=True)
            
            # Reset button
            if st.button("Reset Experiment"):
                st.session_state.step = 0
                st.session_state.animation_complete = False
                st.experimental_rerun()

if __name__ == "__main__":
    main()
