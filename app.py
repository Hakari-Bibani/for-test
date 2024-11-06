import streamlit as st
import streamlit.components.v1 as components
import time

def app():
    st.markdown("""
        <style>
            @keyframes titleColor {
                0% { color: #ff4b4b; }
                50% { color: #4b4bff; }
                100% { color: #ff4b4b; }
            }
            
            .animated-title {
                font-size: 2.5rem;
                text-align: center;
                margin: 2rem 0;
                animation: titleColor 4s infinite;
            }
            
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin: 2rem auto;
                position: relative;
                height: 500px;
                width: 100%;
            }
            
            .tube {
                width: 40px;
                height: 120px;
                background: #f0f0f0;
                border: 2px solid #333;
                position: absolute;
                top: 50px;
                transform-origin: bottom center;
                transition: transform 2s;
            }
            
            .tube.pour {
                transform: rotate(135deg);
            }
            
            .powder {
                width: 30px;
                height: 100px;
                background: #ddd;
                position: absolute;
                bottom: 5px;
                left: 5px;
            }
            
            .beaker {
                width: 200px;
                height: 250px;
                background: transparent;
                border: 3px solid #333;
                position: absolute;
                bottom: 50px;
                border-radius: 5px;
                overflow: hidden;
            }
            
            .liquid {
                width: 100%;
                height: 50%;
                background: rgba(255, 200, 200, 0.8);
                position: absolute;
                bottom: 0;
                transition: height 2s;
            }
            
            @keyframes bubble {
                0% { transform: scale(0); opacity: 0; }
                50% { transform: scale(1); opacity: 1; }
                100% { transform: scale(1.5); opacity: 0; }
            }
            
            .bubbles {
                position: absolute;
                width: 100%;
                height: 100%;
                display: none;
            }
            
            .bubbles.active {
                display: block;
            }
            
            .bubble {
                position: absolute;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 50%;
                animation: bubble 1s infinite;
            }
            
            .equation {
                text-align: center;
                margin-top: 2rem;
                font-size: 1.2rem;
                opacity: 0;
                transition: opacity 1s;
            }
            
            .equation.show {
                opacity: 1;
            }
            
            .label {
                position: absolute;
                font-size: 0.9rem;
                color: #333;
            }
        </style>
        
        <div class="animated-title">Baking Soda and Vinegar Reaction</div>
        
        <div class="container">
            <div class="tube">
                <div class="powder"></div>
                <div class="label" style="top: -25px; left: 45px;">NaHCO₃</div>
            </div>
            
            <div class="beaker">
                <div class="liquid"></div>
                <div class="bubbles"></div>
                <div class="label" style="bottom: -25px; left: 45px;">CH₃COOH</div>
            </div>
        </div>
        
        <div class="equation">
            NaHCO₃ (s) + CH₃COOH (aq) → CO₂ (g) + H₂O (l) + NaCH₃COO (aq)
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Experiment"):
        js = """
        <script>
            function createBubbles() {
                const bubbles = document.querySelector('.bubbles');
                bubbles.classList.add('active');
                
                for (let i = 0; i < 50; i++) {
                    const bubble = document.createElement('div');
                    bubble.className = 'bubble';
                    bubble.style.left = Math.random() * 100 + '%';
                    bubble.style.bottom = Math.random() * 100 + '%';
                    bubble.style.width = Math.random() * 20 + 10 + 'px';
                    bubble.style.height = bubble.style.width;
                    bubble.style.animationDelay = Math.random() * 2 + 's';
                    bubbles.appendChild(bubble);
                }
            }
            
            function startReaction() {
                const tube = document.querySelector('.tube');
                const equation = document.querySelector('.equation');
                
                tube.classList.add('pour');
                
                setTimeout(() => {
                    createBubbles();
                    equation.classList.add('show');
                }, 2000);
            }
            
            startReaction();
        </script>
        """
        components.html(js, height=0)
        time.sleep(2)  # Give animation time to complete

if __name__ == "__main__":
    st.set_page_config(page_title="Chemical Reaction Simulation")
    app()
