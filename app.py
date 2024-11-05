import streamlit as st
import time

# Set page config
st.set_page_config(page_title="pH Test Simulation")

# Custom CSS for styling
st.markdown("""
<style>
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        padding: 20px;
    }
    .title {
        text-align: center;
        font-size: 24px;
        padding: 20px;
    }
    .paper {
        width: 30px;
        height: 100px;
        background-color: #FFE135;
        margin: 10px auto;
        display: block;
        transition: background-color 0.5s ease;
    }
    .beaker {
        width: 120px;
        height: 140px;
        border: 4px solid #e6e6e6;
        border-top: none;
        margin: 20px auto;
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
    @keyframes dip {
        0% { transform: translateY(0); }
        20% { transform: translateY(140px); }
        70% { transform: translateY(140px); }
        100% { transform: translateY(0); }
    }
    .animate-dip-1 { animation: dip 6s forwards; }
    .animate-dip-2 { animation: dip 6s forwards; }
    .animate-dip-3 { animation: dip 6s forwards; }
    
    #start-btn {
        margin: 20px auto;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="main-container">
    <h1 class="title">Test the pH of different solutions using litmus paper!</h1>
    
    <!-- Litmus Papers -->
    <div id="paper1" class="paper"></div>
    <div id="paper2" class="paper"></div>
    <div id="paper3" class="paper"></div>
    
    <!-- Beakers -->
    <div class="beaker">
        <div class="solution" style="background-color: rgba(211,211,211,0.7);"></div>
    </div>
    <div class="beaker">
        <div class="solution" style="background-color: rgba(211,211,211,0.7);"></div>
    </div>
    <div class="beaker">
        <div class="solution" style="background-color: rgba(176,224,230,0.7);"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Start button
start_button = st.button("Start Experiment")

# Animation script
if start_button:
    animation_script = """
    <script>
        function animate() {
            const papers = document.querySelectorAll('.paper');
            
            // Remove any existing animation classes
            papers.forEach(paper => {
                paper.classList.remove('animate-dip-1', 'animate-dip-2', 'animate-dip-3');
                paper.style.backgroundColor = '#FFE135';  // Reset to yellow
            });
            
            // Add animation classes
            papers[0].classList.add('animate-dip-1');
            papers[1].classList.add('animate-dip-2');
            papers[2].classList.add('animate-dip-3');
            
            // Change colors during animation
            setTimeout(() => {
                papers[0].style.backgroundColor = '#ff6666';  // Red for acid
                papers[1].style.backgroundColor = '#6666ff';  // Blue for base
                papers[2].style.backgroundColor = '#90EE90';  // Light green for neutral
            }, 2000);
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
