import streamlit as st
import time

def run_experiment():
    # Custom CSS for styling and animations
    st.markdown("""
    <style>
        /* Title styling */
        .title {
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Container styling */
        .experiment-container {
            position: relative;
            height: 500px;
            margin: 20px auto;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        /* Beaker styling */
        .beaker {
            position: absolute;
            top: 50px;
            right: 55%;
            width: 100px;
            height: 120px;
            border: 4px solid #444;
            border-radius: 5px 5px 10px 10px;
            background: transparent;
            transform-origin: bottom right;
            transition: transform 1.5s ease;
        }
        
        /* Cylinder styling */
        .cylinder {
            position: absolute;
            bottom: 50px;
            left: 55%;
            width: 140px;
            height: 200px;
            border: 4px solid #444;
            border-radius: 10px 10px 20px 20px;
            background: transparent;
            overflow: hidden;
        }
        
        /* Solution styling */
        .h2o2-solution {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 50%;
            background: rgba(173, 216, 230, 0.7);
            transition: all 1s ease;
        }
        
        .ki-solution {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 50%;
            background: rgba(200, 200, 200, 0.7);
            transition: all 1s ease;
        }
        
        /* Label styling */
        .label {
            position: absolute;
            text-align: center;
            width: 100%;
            font-weight: bold;
            color: #444;
        }
        
        /* Foam animation */
        @keyframes foam-eruption {
            0% { height: 50%; }
            50% { height: 300%; }
            100% { height: 250%; }
        }
        
        .foam {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 0;
            background: linear-gradient(to bottom, 
                #ff6b6b,
                #ff8e8e,
                #ffb3b3,
                #ffd8d8
            );
            transition: height 0.5s ease;
            display: none;
        }
        
        /* Pour animation */
        .beaker.pour {
            transform: rotate(135deg);
        }
        
        /* Equation styling */
        .equation {
            text-align: center;
            font-size: 1.2em;
            margin: 20px;
            opacity: 0;
            transition: opacity 1s ease;
        }
        
        .note {
            text-align: center;
            font-style: italic;
            color: #666;
            margin: 10px;
            opacity: 0;
            transition: opacity 1s ease;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display title
    st.markdown("<h1 class='title'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)

    # Create experiment container
    st.markdown("""
    <div class='experiment-container'>
        <div class='beaker' id='beaker'>
            <div class='h2o2-solution'></div>
            <span class='label'>H₂O₂</span>
        </div>
        <div class='cylinder'>
            <div class='ki-solution'></div>
            <div class='foam' id='foam'></div>
            <span class='label'>KI</span>
        </div>
    </div>
    <div class='equation' id='equation'>
        2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)
    </div>
    <div class='note' id='note'>
        Note: Food coloring and liquid soap can be added to create a more dramatic colorful foam effect.
    </div>
    """, unsafe_allow_html=True)

    # Animation control
    if st.button("Start Experiment"):
        st.markdown("""
        <script>
            function runAnimation() {
                const beaker = document.getElementById('beaker');
                const foam = document.getElementById('foam');
                const equation = document.getElementById('equation');
                const note = document.getElementById('note');
                
                // Pour animation
                beaker.classList.add('pour');
                
                // Start foam animation after pour
                setTimeout(() => {
                    foam.style.display = 'block';
                    foam.style.animation = 'foam-eruption 2s ease-out forwards';
                }, 1500);
                
                // Show equation and note
                setTimeout(() => {
                    equation.style.opacity = '1';
                    note.style.opacity = '1';
                }, 3500);
                
                // Reset animation
                setTimeout(() => {
                    beaker.classList.remove('pour');
                    foam.style.display = 'none';
                    foam.style.animation = 'none';
                }, 5000);
            }
            
            runAnimation();
        </script>
        """, unsafe_allow_html=True)
        
        # Simulate animation timing in Streamlit
        time.sleep(5)

# Run the application
if __name__ == "__main__":
    st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="wide")
    run_experiment()
