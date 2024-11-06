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
            animation: gradient 3s linear infinite;
        }
        
        .experiment-container {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            position: relative;
            height: 400px;
            margin-bottom: 20px;
        }
        
        .beaker {
            width: 80px;
            height: 120px;
            border: 3px solid #ddd;
            border-radius: 5px 5px 10px 10px;
            position: absolute;
            right: 45%;
            top: 20%;
            transform-origin: bottom right;
            transition: transform 1s ease;
            z-index: 2;
        }
        
        .cylinder {
            width: 160px;
            height: 240px;
            border: 4px solid #ddd;
            border-radius: 10px 10px 20px 20px;
            position: relative;
            overflow: hidden;
            margin-top: 120px;
        }
        
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            transition: all 1s ease;
        }
        
        .beaker .solution {
            background: rgba(176, 224, 230, 0.7);
        }
        
        .cylinder .solution {
            background: rgba(169, 169, 169, 0.7);
        }
        
        .label {
            position: absolute;
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        .beaker .label {
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
        }
        
        .cylinder .label {
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
        }
        
        @keyframes pour {
            0% { height: 50%; }
            50% { height: 0%; }
            100% { height: 0%; }
        }
        
        @keyframes reaction {
            0% {
                height: 50%;
                background: linear-gradient(to top, #ff4b2b, #ff416c, #f7b733);
            }
            50% {
                height: 300%;
                background: linear-gradient(to top, #ff4b2b, #ff416c, #f7b733);
            }
            75% {
                height: 350%;
                background: linear-gradient(to top, #ff4b2b, #ff416c, #f7b733);
            }
            100% {
                height: 400%;
                background: linear-gradient(to top, #ff4b2b, #ff416c, #f7b733);
            }
        }
        
        .foam {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 0;
            background: linear-gradient(to top, #ff4b2b, #ff416c, #f7b733);
            animation: none;
        }
        
        .pouring {
            transform: rotate(45deg) translateY(-20px);
        }
        
        .pouring .solution {
            animation: pour 1s ease forwards;
        }
        
        .reacting .foam {
            animation: reaction 2s ease-out forwards;
        }
        
        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 50%;
            animation: float 2s infinite ease-in-out;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-20px) scale(1.1); }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Chemical Reaction Animation</h1>", unsafe_allow_html=True)
    
    # Container for the experiment
    container = st.empty()
    
    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O₂</div>
                    <div class="solution"></div>
                </div>
                <div class="cylinder">
                    <div class="label">KI</div>
                    <div class="solution"></div>
                    <div class="foam"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_reaction():
        # Step 1: Pour the solution
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker pouring">
                    <div class="label">H₂O₂</div>
                    <div class="solution"></div>
                </div>
                <div class="cylinder">
                    <div class="label">KI</div>
                    <div class="solution"></div>
                    <div class="foam"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1)
        
        # Step 2: Return beaker and start reaction
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O₂</div>
                    <div class="solution"></div>
                </div>
                <div class="cylinder reacting">
                    <div class="label">KI</div>
                    <div class="solution"></div>
                    <div class="foam"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    render_initial_state()
    
    if st.button("Start Reaction"):
        animate_reaction()
        st.markdown("""
            **Chemical Reaction:**
            2 H₂O₂ (aq) + KI (aq) → 2 H₂O (l) + O₂ (g) + KI (aq)
            
            **Note:** The rapid decomposition of hydrogen peroxide is catalyzed by potassium iodide, 
            producing water and oxygen gas. The dramatic foam effect is created by the rapid release of oxygen gas.
        """)
        
        st.button("Reset Experiment", on_click=run_experiment)

if __name__ == "__main__":
    run_experiment()
