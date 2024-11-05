import streamlit as st
import time
import numpy as np

# Set page config
st.set_page_config(page_title="pH Test Simulation")

# Custom CSS for styling
st.markdown("""
<style>
    .paper {
        width: 30px;
        height: 100px;
        background-color: #fff7e6;
        margin: 10px;
        display: inline-block;
        transition: all 0.5s ease;
        position: relative;
    }
    .beaker {
        width: 100px;
        height: 120px;
        border: 4px solid #e6e6e6;
        border-top: none;
        display: inline-block;
        margin: 20px;
        position: relative;
        overflow: hidden;
    }
    .solution {
        width: 100%;
        height: 80%;
        position: absolute;
        bottom: 0;
        animation: wave 2s infinite ease-in-out;
    }
    @keyframes wave {
        0%, 100% { transform: translateY(2px); }
        50% { transform: translateY(-2px); }
    }
    .title {
        text-align: center;
        font-size: 24px;
        margin-bottom: 30px;
    }
    .container {
        text-align: center;
        margin: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Test the pH of different solutions using litmus paper!</h1>", unsafe_allow_html=True)

# Create container for experiment
col1, col2 = st.columns([3, 1])

with col1:
    # Container for litmus papers
    st.markdown("<div class='container' id='papers'>", unsafe_allow_html=True)
    for _ in range(3):
        st.markdown("<div class='paper'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Container for beakers
    st.markdown("<div class='container' id='beakers'>", unsafe_allow_html=True)
    
    # HCl beaker
    st.markdown("""
        <div class='beaker'>
            <div class='solution' style='background-color: rgba(211,211,211,0.7);'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # NaOH beaker
    st.markdown("""
        <div class='beaker'>
            <div class='solution' style='background-color: rgba(211,211,211,0.7);'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # H2O beaker
    st.markdown("""
        <div class='beaker'>
            <div class='solution' style='background-color: rgba(176,224,230,0.7);'></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    start_button = st.button("Start Experiment")

# Animation script
if start_button:
    animation_script = """
    <script>
        function animate() {
            const papers = document.querySelectorAll('.paper');
            const beakers = document.querySelectorAll('.beaker');
            
            // Initial positions
            papers.forEach((paper, index) => {
                paper.style.transform = 'translateY(0)';
                paper.style.backgroundColor = '#fff7e6';
            });
            
            // Dipping animation
            setTimeout(() => {
                papers.forEach((paper, index) => {
                    paper.style.transform = 'translateY(100px)';
                });
            }, 500);
            
            // Color change animation
            setTimeout(() => {
                papers.forEach((paper, index) => {
                    paper.style.transform = 'translateY(0)';
                    if (index === 0) paper.style.backgroundColor = '#ff6666';  // Red for acid
                    if (index === 1) paper.style.backgroundColor = '#6666ff';  // Blue for base
                    if (index === 2) paper.style.backgroundColor = '#90EE90';  // Light green for neutral
                });
            }, 2000);
        }
        
        if (document.readyState === 'complete') {
            animate();
        } else {
            window.addEventListener('load', animate);
        }
    </script>
    """
    
    st.markdown(animation_script, unsafe_allow_html=True)
    time.sleep(6)  # Wait for animation to complete
    st.experimental_rerun()
