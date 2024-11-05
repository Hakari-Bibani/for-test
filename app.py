import streamlit as st
import time

# Set page config
st.set_page_config(page_title="pH Test Simulation", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .paper {
        width: 30px;
        height: 100px;
        background-color: #FFE135;  /* Bright yellow color */
        margin: 10px;
        display: inline-block;
        transition: all 1s ease;
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
    .experiment-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto;
        max-width: 800px;
    }
    .papers-container, .beakers-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 10px 0;
    }
    .button-container {
        margin: 20px 0;
    }
    @keyframes dip {
        0% { transform: translateY(0); }
        45% { transform: translateY(80px); }
        55% { transform: translateY(80px); }
        100% { transform: translateY(0); }
    }
    .animate-dip {
        animation: dip 6s forwards;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Test the pH of different solutions using litmus paper!</h1>", unsafe_allow_html=True)

# Create container for experiment
st.markdown("<div class='experiment-container'>", unsafe_allow_html=True)

# Container for litmus papers
st.markdown("<div class='papers-container' id='papers'>", unsafe_allow_html=True)
for _ in range(3):
    st.markdown("<div class='paper'></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Container for beakers
st.markdown("<div class='beakers-container' id='beakers'>", unsafe_allow_html=True)

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

# Button container
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
start_button = st.button("Start Experiment")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Animation script
if start_button:
    animation_script = """
    <script>
        function animate() {
            const papers = document.querySelectorAll('.paper');
            
            // Add dipping animation class
            papers.forEach(paper => {
                paper.classList.add('animate-dip');
            });
            
            // Color change timing
            setTimeout(() => {
                papers[0].style.backgroundColor = '#ff6666';  // Red for acid
                papers[1].style.backgroundColor = '#6666ff';  // Blue for base
                papers[2].style.backgroundColor = '#90EE90';  // Light green for neutral
            }, 3000);  // Change colors halfway through the dip
            
            // Reset after animation
            setTimeout(() => {
                papers.forEach(paper => {
                    paper.classList.remove('animate-dip');
                });
            }, 6000);
        }
        
        // Run animation
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
