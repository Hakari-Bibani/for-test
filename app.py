import streamlit as st
import time

st.title("Test the pH of different solutions using litmus paper!")

# Custom CSS for better styling
st.markdown("""
<style>
    .litmus-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
        padding: 20px;
    }
    
    .beaker-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
        padding: 20px;
    }
    
    .litmus {
        width: 30px;
        height: 100px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .beaker {
        width: 100px;
        height: 150px;
        position: relative;
        background: rgba(255,255,255,0.1);
        border: 3px solid #ddd;
        border-top: 15px solid #ddd;
        border-radius: 10px 10px 20px 20px;
        text-align: center;
        padding-top: 10px;
    }
    
    .solution {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 80%;
        border-radius: 0 0 17px 17px;
    }
</style>
""", unsafe_allow_html=True)

# Create placeholders for dynamic content
litmus_placeholder = st.empty()
beakers_placeholder = st.empty()

def render_initial_state():
    # Render litmus papers
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FFFACD;'></div>
            <div class='litmus' style='background-color: #FFFACD;'></div>
            <div class='litmus' style='background-color: #FFFACD;'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render beakers
    beakers_placeholder.markdown("""
        <div class='beaker-container'>
            <div>
                <div class='beaker'>
                    <div class='solution' style='background: linear-gradient(to bottom, rgba(211,211,211,0.7), rgba(169,169,169,0.9));'></div>
                    HCl
                </div>
            </div>
            <div>
                <div class='beaker'>
                    <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                    H₂O
                </div>
            </div>
            <div>
                <div class='beaker'>
                    <div class='solution' style='background: linear-gradient(to bottom, rgba(211,211,211,0.7), rgba(169,169,169,0.9));'></div>
                    NaOH
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def animate_experiment():
    # Step 1: Move litmus papers down (diving animation)
    litmus_placeholder.markdown("""
        <div class='litmus-container' style='margin-top: 120px;'>
            <div class='litmus' style='background-color: #FFFACD;'></div>
            <div class='litmus' style='background-color: #FFFACD;'></div>
            <div class='litmus' style='background-color: #FFFACD;'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1)
    
    # Step 2: Show color change
    litmus_placeholder.markdown("""
        <div class='litmus-container' style='margin-top: 120px;'>
            <div class='litmus' style='background-color: #FF6347;'></div>
            <div class='litmus' style='background-color: #90EE90;'></div>
            <div class='litmus' style='background-color: #4682B4;'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    
    # Step 3: Move litmus papers back up with new colors
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FF6347;'></div>
            <div class='litmus' style='background-color: #90EE90;'></div>
            <div class='litmus' style='background-color: #4682B4;'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    
    # Reset to initial state
    render_initial_state()

# Initial render
render_initial_state()

# Add start button
if st.button("Start Experiment"):
    animate_experiment()
