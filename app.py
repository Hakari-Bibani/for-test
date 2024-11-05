import streamlit as st
import time

def elephant_toothpaste_experiment():
    # CSS for animations and styling
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
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        
        .experiment-container {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            gap: 50px;
            margin: 30px 0;
            padding: 20px;
            min-height: 400px;
            background: linear-gradient(to bottom, #f8f9fa, #e9ecef);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .beaker, .cylinder {
            width: 100px;
            height: 150px;
            position: relative;
            background: rgba(255,255,255,0.4);
            border: 4px solid #ddd;
            border-radius: 10px 10px 15px 15px;
            overflow: hidden;
            text-align: center;
            box-shadow: inset 0 0 20px rgba(255,255,255,0.5);
        }
        
        .beaker::before, .cylinder::before {
            content: '';
            position: absolute;
            top: 0;
            right: 15%;
            width: 3px;
            height: 100%;
            background: rgba(255,255,255,0.4);
        }
        
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            transition: all 1s ease;
        }
        
        .solution-blue { 
            background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));
            animation: liquidWave 4s infinite ease-in-out;
        }
        
        .solution-grey { 
            background: linear-gradient(to bottom, rgba(169,169,169,0.7), rgba(128,128,128,0.9));
            animation: liquidWave 3s infinite ease-in-out;
        }
        
        @keyframes liquidWave {
            0%, 100% { transform: scaleY(1.02); }
            50% { transform: scaleY(0.98); }
        }
        
        .pour-animation {
            transform: rotate(-45deg) translate(20px, -20px);
            transition: transform 1.5s ease-in-out;
        }
        
        .reaction-foam {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 120%;
            height: 0;
            background: linear-gradient(to top, 
                rgba(255,99,71,0.8), 
                rgba(255,160,122,0.8), 
                rgba(245,245,220,0.8));
            animation: foamExpand 3s ease-out forwards;
            border-radius: 10px 10px 0 0;
            box-shadow: 0 0 10px rgba(255,99,71,0.3);
        }
        
        @keyframes foamExpand {
            0% { 
                height: 0;
                opacity: 0;
            }
            20% {
                opacity: 0.8;
            }
            100% { 
                height: 300px;
                opacity: 1;
            }
        }
        
        .chemical-formula {
            background: rgba(255,255,255,0.9);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .start-button {
            background: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 20px 0;
        }
        
        .start-button:hover {
            background: #45a049;
            transform: translateY(-2px);
        }
        
        .label {
            position: absolute;
            bottom: -25px;
            width: 100%;
            text-align: center;
            font-weight: bold;
            color: #2c3e50;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Title with animation
    st.markdown("<h1 class='title'>🧪 Elephant Toothpaste Experiment</h1>", unsafe_allow_html=True)
    
    # Description
    st.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            Watch the decomposition of hydrogen peroxide catalyzed by potassium iodide,
            creating a dramatic foam reaction!
        </div>
    """, unsafe_allow_html=True)
    
    # Experiment container
    experiment_container = st.empty()

    def render_initial_state():
        experiment_container.markdown("""
            <div class='experiment-container'>
                <div class='beaker'>
                    <div class='solution solution-blue'></div>
                    <div class='label'>H₂O₂</div>
                </div>
                <div class='cylinder'>
                    <div class='solution solution-grey'></div>
                    <div class='label'>KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_reaction():
        experiment_container.markdown("""
            <div class='experiment-container'>
                <div class='beaker pour-animation'>
                    <div class='solution solution-blue'></div>
                    <div class='label'>H₂O₂</div>
                </div>
                <div class='cylinder'>
                    <div class='solution solution-grey'></div>
                    <div class='reaction-foam'></div>
                    <div class='label'>KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    render_initial_state()
    
    # Control panel
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Start Experiment", key="start_experiment"):
            animate_reaction()
            time.sleep(0.5)
            st.markdown("""
                <div class='chemical-formula'>
                    <h3>Chemical Reaction:</h3>
                    <p>2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</p>
                    <p><small>The KI acts as a catalyst, speeding up the decomposition of H₂O₂</small></p>
                </div>
            """, unsafe_allow_html=True)
            
            # Additional information appears after reaction
            st.markdown("""
                <div style='margin-top: 20px; text-align: left;'>
                    <h4>Key Observations:</h4>
                    <ul>
                        <li>Rapid production of oxygen gas</li>
                        <li>Exothermic reaction (releases heat)</li>
                        <li>Formation of soap-like foam</li>
                        <li>Catalyst (KI) remains unchanged</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Elephant Toothpaste Experiment", layout="centered")
    elephant_toothpaste_experiment()
