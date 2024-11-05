import streamlit as st
import time

def run_experiment():
    # Custom CSS for enhanced styling and animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');
        
        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(45deg, #2c3e50, #3498db, #2c3e50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 200% auto;
            animation: gradient 3s linear infinite, float 3s ease-in-out infinite;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(-2deg); }
            50% { transform: translateY(-10px) rotate(2deg); }
        }
        
        .beaker-container {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            position: relative;
            height: 250px;
            margin-bottom: 20px;
        }
        
        .beaker, .cylinder {
            width: 120px;
            height: 180px;
            border: 3px solid #ddd;
            border-top: 15px solid #ddd;
            border-radius: 10px 10px 0 0;
            overflow: hidden;
            position: relative;
            margin: 0 20px;
        }
        
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            border-radius: 0 0 17px 17px;
            animation: liquidWave 4s infinite ease-in-out;
        }
        
        .solution::before {
            content: '';
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            height: 20px;
            background: inherit;
            filter: blur(5px);
            opacity: 0.7;
            animation: surfaceWave 2s infinite ease-in-out;
        }
        
        @keyframes liquidWave {
            0%, 100% { transform: translateY(2px) scaleY(1.02); }
            50% { transform: translateY(-2px) scaleY(0.98); }
        }
        
        @keyframes surfaceWave {
            0%, 100% { transform: translateX(-5px); }
            50% { transform: translateX(5px); }
        }
        
        .reaction {
            background: linear-gradient(to top, #ff4b2b, #ff416c, #f7b733);
            width: 100%;
            position: absolute;
            bottom: 0;
            height: 0;
            overflow: hidden;
            animation: foam 1.5s ease forwards;
        }
        
        @keyframes foam {
            from { height: 0; }
            to { height: 300%; }
        }
        
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)
    
    # Display the beaker and cylinder containers
    beaker_placeholder = st.empty()
    cylinder_placeholder = st.empty()
    
    def render_initial_state():
        beaker_placeholder.markdown("""
            <div class="beaker-container">
                <div class="beaker">
                    <div class="solution" style="background: rgba(176,224,230,0.7);" id="beaker-solution"></div>
                </div>
                <div class="cylinder">
                    <div class="solution" style="background: rgba(169,169,169,0.7);" id="cylinder-solution"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_reaction():
        # Step 1: Move beaker and "pour" solution
        beaker_placeholder.markdown("""
            <div class="beaker-container">
                <div class="beaker" style="transform: rotate(-20deg);">
                    <div class="solution" style="background: rgba(176,224,230,0);"></div>
                </div>
                <div class="cylinder">
                    <div class="reaction"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.5)
        
        # Step 2: Reset beaker position and trigger foam animation in cylinder
        beaker_placeholder.markdown("""
            <div class="beaker-container">
                <div class="beaker">
                    <div class="solution" style="background: rgba(176,224,230,0.7);"></div>
                </div>
                <div class="cylinder">
                    <div class="reaction"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    render_initial_state()
    
    if st.button("Start Experiment"):
        animate_reaction()
        st.markdown("""
            **Chemical Equation:**
            2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
            
            **Note:** Optionally, you can add food coloring and liquid soap for more dramatic effect.
        """)
        
        st.button("Repeat Experiment", on_click=run_experiment)

run_experiment()
