import streamlit as st
import time

# Set page config
st.set_page_config(page_title="pH Test Simulation")

# Custom CSS with keyframe animations
st.markdown("""
<style>
    .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }
    
    .title {
        font-size: 24px;
        margin-bottom: 40px;
        text-align: center;
    }
    
    .experiment-area {
        position: relative;
        height: 800px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }
    
    .paper {
        width: 30px;
        height: 100px;
        background-color: #FFE135;
        position: relative;
        transition: background-color 0.5s ease;
    }
    
    .beaker {
        width: 120px;
        height: 140px;
        border: 4px solid #e6e6e6;
        border-top: none;
        position: relative;
        margin: 20px 0;
    }
    
    .solution {
        width: 100%;
        height: 80%;
        position: absolute;
        bottom: 0;
    }
    
    .acid-solution {
        background-color: rgba(211,211,211,0.7);
    }
    
    .base-solution {
        background-color: rgba(211,211,211,0.7);
    }
    
    .neutral-solution {
        background-color: rgba(176,224,230,0.7);
    }
    
    @keyframes dipPaper {
        0% { transform: translateY(0); }
        40% { transform: translateY(120px); }
        60% { transform: translateY(120px); }
        100% { transform: translateY(0); }
    }
    
    .animate-dip {
        animation: dipPaper 3s forwards;
    }
    
    .red { background-color: #ff6666 !important; }
    .blue { background-color: #6666ff !important; }
    .green { background-color: #90EE90 !important; }
    
    .button-container {
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'animation_counter' not in st.session_state:
    st.session_state.animation_counter = 0

# Layout
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Test the pH of different solutions using litmus paper!</h1>", unsafe_allow_html=True)

# Experiment area
st.markdown("""
    <div class='experiment-area'>
        <div id='paper1' class='paper'></div>
        <div class='beaker'>
            <div class='solution acid-solution'></div>
        </div>
        
        <div id='paper2' class='paper'></div>
        <div class='beaker'>
            <div class='solution base-solution'></div>
        </div>
        
        <div id='paper3' class='paper'></div>
        <div class='beaker'>
            <div class='solution neutral-solution'></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Button
if st.button("Start Experiment", key="start_button"):
    st.session_state.animation_counter += 1
    
    # Animation script
    st.markdown(f"""
    <script>
        function runAnimation() {{
            const papers = document.querySelectorAll('.paper');
            
            // Reset papers to initial state
            papers.forEach(paper => {{
                paper.style.backgroundColor = '#FFE135';
                paper.classList.remove('animate-dip', 'red', 'blue', 'green');
            }});
            
            // Start animation sequence
            setTimeout(() => {{
                papers.forEach(paper => paper.classList.add('animate-dip'));
                
                // Change colors after dipping
                setTimeout(() => {{
                    papers[0].classList.add('red');
                    papers[1].classList.add('blue');
                    papers[2].classList.add('green');
                }}, 1200);
            }}, 100);
        }}
        
        // Run animation when document is ready
        document.addEventListener('DOMContentLoaded', runAnimation);
        // Also run immediately in case document is already loaded
        runAnimation();
    </script>
    """, unsafe_allow_html=True)
    
    # Force rerun after animation
    time.sleep(3)
    st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
