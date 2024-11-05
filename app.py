import streamlit as st
import time

def elephant_toothpaste_experiment():
    # CSS for animations and beaker design
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
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        
        .experiment-container {
            display: flex;
            justify-content: center;
            margin: 30px 0;
            position: relative;
        }
        
        .beaker, .cylinder {
            width: 80px;
            height: 100px;
            position: relative;
            background: rgba(255,255,255,0.1);
            border: 3px solid #ddd;
            border-radius: 10px;
            overflow: hidden;
            text-align: center;
        }
        
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            animation: liquidWave 4s infinite ease-in-out;
        }
        
        .solution-blue { background: rgba(176,224,230,0.7); }
        .solution-grey { background: rgba(169,169,169,0.7); }
        
        @keyframes liquidWave {
            0%, 100% { transform: scaleY(1.02); }
            50% { transform: scaleY(0.98); }
        }
        
        .pour-animation {
            transform: rotate(-45deg) translate(20px, 20px);
            transition: transform 1.5s;
        }
        
        .reaction-foam {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 10px;
            background: linear-gradient(to top, #ff6347, #ffa07a, #f5f5dc);
            animation: foamExpand 2s ease-out forwards;
        }
        
        @keyframes foamExpand {
            0% { height: 10px; }
            100% { height: 200px; }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Title with animation
    st.markdown("<h1 class='title'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)
    
    # Beaker and Cylinder setup
    experiment_container = st.empty()

    def render_initial_state():
        experiment_container.markdown("""
            <div class='experiment-container'>
                <div class='beaker'>
                    <div class='solution solution-blue'></div>
                    <div>H₂O₂</div>
                </div>
                <div class='cylinder'>
                    <div class='solution solution-grey'></div>
                    <div>KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_reaction():
        # Pouring animation and reaction foam
        experiment_container.markdown("""
            <div class='experiment-container'>
                <div class='beaker pour-animation'>
                    <div class='solution solution-blue'></div>
                    <div>H₂O₂</div>
                </div>
                <div class='cylinder'>
                    <div class='reaction-foam'></div>
                    <div>KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(2)
    
    render_initial_state()
    
    if st.button("Start Experiment"):
        animate_reaction()
        st.markdown("""
            <h3>Chemical Reaction:</h3>
            <p>2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</p>
            <p>Note: Add food coloring or liquid soap for enhanced visual effects.</p>
        """, unsafe_allow_html=True)
    
# Run the experiment
elephant_toothpaste_experiment()
