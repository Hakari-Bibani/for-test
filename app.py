import streamlit as st

# Page config and modern styling
st.set_page_config(page_title="pH Test Simulation", layout="wide")

# Enhanced CSS with modern styling and animations
st.markdown("""
<style>
    /* Modern page styling */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Animated title */
    .title {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
        margin: 30px 0;
        padding: 20px;
    }
    
    /* Main container */
    .experiment-wrapper {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 1000px;
    }
    
    .litmus-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
        padding: 20px;
        height: 150px;
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
        width: 140px;
        height: 170px;
        position: relative;
        background: rgba(255,255,255,0.2);
        border: 4px solid #ddd;
        border-top: 18px solid #ddd;
        border-radius: 12px 12px 25px 25px;
        text-align: center;
        margin-bottom: 50px;
        box-shadow: 
            inset -5px 0 15px rgba(255,255,255,0.4),
            inset 5px 0 15px rgba(255,255,255,0.4),
            0 5px 15px rgba(0,0,0,0.1);
    }
    
    .solution {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 80%;
        border-radius: 0 0 20px 20px;
        animation: wave 2s infinite ease-in-out;
        background: linear-gradient(to bottom, 
            rgba(176,224,230,0.7), 
            rgba(135,206,235,0.9)
        );
    }

    .beaker-label {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 14px;
        font-weight: 500;
        text-align: center;
        margin-top: 15px;
        color: #2c3e50;
        line-height: 1.4;
    }

    @keyframes wave {
        0%, 100% { transform: translateY(3px); }
        50% { transform: translateY(-3px); }
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #12c2e9, #c471ed);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 10px 30px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Animated title
st.markdown("<h1 class='title'>Test the pH of different solutions using litmus paper!</h1>", unsafe_allow_html=True)

# Create placeholders
main_container = st.container()
with main_container:
    st.markdown("<div class='experiment-wrapper'>", unsafe_allow_html=True)
    litmus_placeholder = st.empty()
    beakers_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

def render_initial_state():
    # Render litmus papers
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FFFACD; transform: translateY(0px);'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translateY(0px);'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translateY(0px);'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render beakers
    beakers_placeholder.markdown("""
        <div class='beaker-container'>
            <div>
                <div class='beaker'>
                    <div class='solution'></div>
                </div>
                <div class='beaker-label'>Hydrochloric acid<br>(HCl)</div>
            </div>
            <div>
                <div class='beaker'>
                    <div class='solution'></div>
                </div>
                <div class='beaker-label'>Neutral water<br>(H₂O)</div>
            </div>
            <div>
                <div class='beaker'>
                    <div class='solution'></div>
                </div>
                <div class='beaker-label'>Sodium hydroxide<br>(NaOH)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def animate_experiment():
    # Step 1: Move down halfway
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FFFACD; transform: translateY(90px);'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translateY(90px);'></div>
            <div class='litmus' style='background-color: #FFFACD; transform: translateY(90px);'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1)
    
    # Step 2: Show color change while dipped
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FF6347; transform: translateY(90px);'></div>
            <div class='litmus' style='background-color: #90EE90; transform: translateY(90px);'></div>
            <div class='litmus' style='background-color: #4682B4; transform: translateY(90px);'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    
    # Step 3: Return to original position with new colors
    litmus_placeholder.markdown("""
        <div class='litmus-container'>
            <div class='litmus' style='background-color: #FF6347; transform: translateY(0px);'></div>
            <div class='litmus' style='background-color: #90EE90; transform: translateY(0px);'></div>
            <div class='litmus' style='background-color: #4682B4; transform: translateY(0px);'></div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    
    # Reset to initial state
    render_initial_state()

# Initial render
render_initial_state()

# Centered button with modern styling
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("Start Experiment"):
        animate_experiment()
