import streamlit as st
import time
import streamlit.components.v1 as components

def app():
    # Set page config
    st.set_page_config(page_title="Chemical Reaction Simulation")

    # Custom CSS for animations and styling
    st.markdown("""
        <style>
        @keyframes titleMove {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        @keyframes bubbleEffect {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-200px); opacity: 0; }
        }
        
        @keyframes pourAnimation {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(135deg); }
        }

        .moving-title {
            animation: titleMove 5s linear infinite;
            white-space: nowrap;
            font-size: 2em;
            color: #1f77b4;
        }

        .container {
            position: relative;
            height: 400px;
            width: 100%;
        }

        .beaker {
            position: absolute;
            right: 50%;
            top: 50%;
            width: 150px;
            height: 200px;
            background: linear-gradient(
                to bottom,
                transparent 50%,
                rgba(255, 200, 200, 0.7) 50%
            );
            border: 5px solid #666;
            border-radius: 10px;
        }

        .spoon {
            position: absolute;
            right: 60%;
            top: 30%;
            width: 100px;
            height: 30px;
            background: #ddd;
            border: 2px solid #666;
            transform-origin: right center;
        }

        .powder {
            position: absolute;
            right: 65%;
            top: 25%;
            font-size: 1.2em;
            color: #666;
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: bubbleEffect 1s ease-out;
        }

        .equation {
            text-align: center;
            font-size: 1.5em;
            margin-top: 20px;
            opacity: 0;
            transition: opacity 1s;
        }
        </style>
    """, unsafe_allow_html=True)

    # Moving title
    st.markdown('<div class="moving-title">Baking Soda and Vinegar Reaction</div>', unsafe_allow_html=True)

    # Create container for experiment
    st.markdown('<div class="container" id="experiment-container">', unsafe_allow_html=True)
    
    # Add beaker and spoon
    st.markdown('''
        <div class="beaker"></div>
        <div class="spoon" id="spoon"></div>
        <div class="powder">NaHCO₃</div>
    ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Add equation (initially hidden)
    st.markdown('<div class="equation" id="equation">NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO</div>', unsafe_allow_html=True)

    # JavaScript for animations
    js_code = """
    <script>
    function startExperiment() {
        const spoon = document.getElementById('spoon');
        const equation = document.getElementById('equation');
        const container = document.getElementById('experiment-container');
        
        // Pour animation
        spoon.style.animation = 'pourAnimation 1s forwards';
        
        // Create bubbles after slight delay
        setTimeout(() => {
            for (let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const bubble = document.createElement('div');
                    bubble.className = 'bubble';
                    bubble.style.width = Math.random() * 20 + 10 + 'px';
                    bubble.style.height = bubble.style.width;
                    bubble.style.right = '50%';
                    bubble.style.top = '50%';
                    container.appendChild(bubble);
                    
                    // Remove bubble after animation
                    setTimeout(() => bubble.remove(), 1000);
                }, i * 100);
            }
        }, 1000);

        // Show equation after reaction
        setTimeout(() => {
            equation.style.opacity = '1';
        }, 2500);

        // Reset spoon animation after completion
        setTimeout(() => {
            spoon.style.animation = 'none';
            spoon.offsetHeight; // Trigger reflow
        }, 3000);
    }
    </script>
    """
    
    components.html(js_code, height=0)

    # Start experiment button
    if st.button('Start Experiment', on_click=None):
        components.html("""
            <script>
            startExperiment();
            </script>
        """, height=0)

if __name__ == "__main__":
    app()
