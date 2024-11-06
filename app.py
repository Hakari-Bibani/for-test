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
            height: 500px;
            margin-bottom: 20px;
            overflow: visible;
        }
        
        .beaker {
            width: 80px;
            height: 120px;
            border: 3px solid #ddd;
            border-radius: 5px 5px 10px 10px;
            position: absolute;
            left: 35%;  /* Moved more to the left */
            top: 15%;
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
            overflow: visible;
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
        
        .beaker .label {
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        .cylinder .label {
            position: absolute;
            bottom: -30px;  /* Moved label below cylinder */
            left: 50%;
            transform: translateX(-50%);
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        @keyframes pour {
            0% { height: 50%; }
            50% { height: 0%; }
            100% { height: 0%; }
        }
        
        @keyframes reaction {
            0% {
                height: 50%;
                background: linear-gradient(to top, #000000, #ff0000);
            }
            20% {
                height: 140%;
                background: linear-gradient(to top, #000000, #ff0000);
            }
            40% {
                height: 180%;
                background: linear-gradient(to top, #000000, #ff0000);
                transform: scaleX(1.1);
            }
            60% {
                height: 220%;
                background: linear-gradient(to top, #000000, #ff0000);
                transform: scaleX(1);
            }
            80% {
                height: 200%;
                background: linear-gradient(to top, #000000, #ff0000);
                transform: scaleX(1.1);
            }
            100% {
                height: 190%;
                background: linear-gradient(to top, #000000, #ff0000);
                transform: scaleX(1);
            }
        }
        
        .foam {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 0;
            background: linear-gradient(to top, #000000, #ff0000);
            animation: none;
            filter: drop-shadow(0 0 5px rgba(255, 0, 0, 0.3));
        }
        
        .pouring {
            transform: rotate(55deg) translateY(-20px) translateX(40px);  /* Adjusted angle for better pouring */
        }
        
        .pouring .solution {
            animation: pour 1s ease forwards;
        }
        
        .reacting .foam {
            animation: reaction 1.5s ease-out forwards;
        }
        
        /* Foam particles effect */
        .particle {
            position: absolute;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #ff0000;
            opacity: 0;
        }
        
        @keyframes particle {
            0% {
                transform: translate(0, 0);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty));
                opacity: 0;
            }
        }
        
        .reacting .particle {
            animation: particle 0.8s ease-out forwards;
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
                    <div class="solution"></div>
                    <div class="foam"></div>
                    <div class="label">30% KI</div>
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
                    <div class="solution"></div>
                    <div class="foam"></div>
                    <div class="label">30% KI</div>
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
                    <div class="solution"></div>
                    <div class="foam"></div>
                    <div class="label">30% KI</div>
                    <!-- Add foam particles -->
                    <div class="particle" style="--tx: 20px; --ty: -40px;"></div>
                    <div class="particle" style="--tx: -15px; --ty: -35px;"></div>
                    <div class="particle" style="--tx: 10px; --ty: -45px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    render_initial_state()
    
    if st.button("Start Reaction"):
        animate_reaction()
        st.markdown("""
            **Chemical Reaction:**
            2 H₂O₂ (aq) + 30% KI (aq) → 2 H₂O (l) + O₂ (g) + KI (aq)
            
            **Note:** The rapid decomposition of hydrogen peroxide is catalyzed by potassium iodide, 
            producing water and oxygen gas. The dramatic foam effect is created by the rapid release of oxygen gas.
        """)
        
        st.button("Reset Experiment", on_click=run_experiment)

if __name__ == "__main__":
    run_experiment()
