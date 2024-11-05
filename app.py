import streamlit as st
import time

st.set_page_config(page_title="pH Test Simulation")

# Custom CSS for styling
st.markdown("""
<style>
    /* Beaker styles */
    .beaker {
        position: relative;
        width: 100px;
        height: 120px;
        margin: 20px;
        display: inline-block;
        border: 2px solid #ddd;
        border-radius: 5px 5px 15px 15px;
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 
            inset -10px 0 20px rgba(255, 255, 255, 0.2),
            inset 10px 0 20px rgba(255, 255, 255, 0.2),
            0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .beaker::before {
        content: '';
        position: absolute;
        top: -10px;
        left: -5px;
        right: -5px;
        height: 15px;
        background: #ddd;
        border-radius: 5px;
    }
    
    .solution {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 80%;
        border-radius: 0 0 13px 13px;
        animation: wave 2s infinite ease-in-out;
    }
    
    /* Litmus paper styles */
    .litmus-paper {
        width: 20px;
        height: 100px;
        background-color: #FFFACD;
        margin: 0 40px;
        display: inline-block;
        position: relative;
        transition: all 0.5s ease;
        border-radius: 3px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .litmus-paper.dipping {
        transform: translateY(120px);
    }
    
    /* Animation keyframes */
    @keyframes wave {
        0%, 100% { transform: translateY(2px); }
        50% { transform: translateY(-2px); }
    }
    
    /* Container styles */
    .experiment-container {
        text-align: center;
        padding: 20px;
        background: #f8f9fa;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    .beaker-container {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        margin-top: 50px;
    }
    
    .beaker-label {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("Test the pH of different solutions using litmus paper!")

def create_experiment_layout():
    st.markdown("""
    <div class="experiment-container">
        <div id="litmus-papers">
            <div class="litmus-paper"></div>
            <div class="litmus-paper"></div>
            <div class="litmus-paper"></div>
        </div>
        
        <div class="beaker-container">
            <div>
                <div class="beaker">
                    <div class="solution" style="background: linear-gradient(to bottom, rgba(211,211,211,0.7), rgba(169,169,169,0.9));"></div>
                </div>
                <div class="beaker-label">HCl</div>
            </div>
            
            <div>
                <div class="beaker">
                    <div class="solution" style="background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));"></div>
                </div>
                <div class="beaker-label">H₂O</div>
            </div>
            
            <div>
                <div class="beaker">
                    <div class="solution" style="background: linear-gradient(to bottom, rgba(211,211,211,0.7), rgba(169,169,169,0.9));"></div>
                </div>
                <div class="beaker-label">NaOH</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Animation script
def get_animation_script():
    return """
    <script>
        function animateLitmusTest() {
            const papers = document.querySelectorAll('.litmus-paper');
            
            // Step 1: Dip the papers
            papers.forEach(paper => {
                paper.style.transition = 'all 1s ease';
                paper.classList.add('dipping');
            });
            
            // Step 2: Change colors while dipped
            setTimeout(() => {
                papers[0].style.backgroundColor = '#FF6347';  // Red for acid
                papers[1].style.backgroundColor = '#90EE90';  // Light green for neutral
                papers[2].style.backgroundColor = '#4682B4';  // Blue for base
            }, 1000);
            
            // Step 3: Return to original position with new colors
            setTimeout(() => {
                papers.forEach(paper => {
                    paper.classList.remove('dipping');
                });
            }, 3000);
        }
        
        // Run animation when the page loads
        if (document.readyState === 'complete') {
            animateLitmusTest();
        } else {
            window.addEventListener('load', animateLitmusTest);
        }
    </script>
    """

# Create main layout
create_experiment_layout()

# Add start button
if st.button("Start Experiment"):
    st.markdown(get_animation_script(), unsafe_allow_html=True)
    time.sleep(6)  # Wait for animation to complete
    st.experimental_rerun()
