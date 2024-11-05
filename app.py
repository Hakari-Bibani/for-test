import streamlit as st
import time

# Custom CSS with enhanced styling and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');

    .title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5em;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        animation: titleWave 3s ease-in-out infinite;
        background: linear-gradient(45deg, #2c3e50, #3498db);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    @keyframes titleWave {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }

    .litmus-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
        padding: 20px;
        height: 120px;
    }
    
    .beaker-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
        padding: 20px;
        position: relative;
    }
    
    .litmus {
        width: 30px;
        height: 100px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 1s ease;
        position: relative;
    }
    
    .beaker {
        width: 120px;
        height: 150px;
        position: relative;
        background: rgba(255,255,255,0.1);
        border: 3px solid #ddd;
        border-top: 15px solid #ddd;
        border-radius: 10px 10px 20px 20px;
        text-align: center;
        padding-top: 10px;
        margin-bottom: 40px;
    }
    
    .solution {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 80%;
        border-radius: 0 0 17px 17px;
        animation: wave 2s infinite ease-in-out;
    }

    .beaker-label {
        font-family: 'Poppins', sans-serif;
        font-size: 12px;
        text-align: center;
        margin-top: 10px;
        color: #2c3e50;
        max-width: 120px;
        word-wrap: break-word;
        font-weight: 500;
    }

    @keyframes wave {
        0%, 100% { transform: translateY(2px); }
        50% { transform: translateY(-2px); }
    }
</style>
""", unsafe_allow_html=True)

# Title with animation
st.markdown("<h1 class='title'>Test the pH of different solutions using litmus paper!</h1>", unsafe_allow_html=True)

# Create placeholders for dynamic content
litmus_placeholder = st.empty()
beakers_placeholder = st.empty()

def render_initial_state():
    # Render litmus papers
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FFFACD; transform: translate(0, 0);'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translate(0, 0);'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translate(0, 0);'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render beakers with moving solutions and detailed labels
    beakers_placeholder.markdown("""
        <div class='beaker-container'>
            <div>
                <div class='beaker'>
                    <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                </div>
                <div class='beaker-label'>Hydrochloric acid<br>(HCl)</div>
            </div>
            <div>
                <div class='beaker'>
                    <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                </div>
                <div class='beaker-label'>Neutral water<br>(H₂O)</div>
            </div>
            <div>
                <div class='beaker'>
                    <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                </div>
                <div class='beaker-label'>Sodium hydroxide<br>(NaOH)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def animate_experiment():
    # Step 1: Move papers to center of beakers
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FFFACD; transform: translate(-15px, 60px); transition: all 1s;'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translate(0px, 60px); transition: all 1s;'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translate(15px, 60px); transition: all 1s;'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1)
    
    # Step 2: Color change while in solutions
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FF6347; transform: translate(-15px, 60px); transition: all 1s;'></div>
            <div class='litmus' style='background-color: #90EE90; transform: translate(0px, 60px); transition: all 1s;'></div>
            <div class='litmus' style='background-color: #4682B4; transform: translate(15px, 60px); transition: all 1s;'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    
    # Step 3: Return to original positions with new colors
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FF6347; transform: translate(0, 0); transition: all 1s;'></div>
            <div class='litmus' style='background-color: #90EE90; transform: translate(0, 0); transition: all 1s;'></div>
            <div class='litmus' style='background-color: #4682B4; transform: translate(0, 0); transition: all 1s;'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    
    # Reset to initial state
    render_initial_state()

# Initial render
render_initial_state()

# Add start button with custom styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #3498db;
            color: white;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
            border: none;
            padding: 10px 25px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
        }
    </style>
""", unsafe_allow_html=True)

if st.button("Start Experiment"):
    animate_experiment()
