import streamlit as st
import time

def elephant_toothpaste_experiment():
    # Inject custom CSS and JavaScript for advanced animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');
        
        /* Title styling with floating effect */
        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        
        /* Container for experiment setup */
        .experiment-container {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin: 30px 0;
            position: relative;
        }
        
        /* Beaker and cylinder base styling */
        .beaker, .cylinder {
            width: 80px;
            height: 120px;
            background: rgba(255,255,255,0.1);
            border: 3px solid #ddd;
            border-radius: 10px;
            overflow: hidden;
            text-align: center;
            position: relative;
        }

        /* Solution colors */
        .solution-blue { background: rgba(176,224,230,0.7); }
        .solution-grey { background: rgba(169,169,169,0.7); }
        
        /* Pouring and foam eruption animations */
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

    # JavaScript to control the timing and sequence of animations
    st.markdown("""
    <script>
        function triggerPourAnimation() {
            const beaker = document.querySelector('.beaker');
            if (beaker) {
                beaker.classList.add('pour-animation');
            }
            setTimeout(() => {
                document.querySelector('.reaction-foam').style.height = '200px';
            }, 1500);
        }
    </script>
    """, unsafe_allow_html=True)

    # Display title
    st.markdown("<h1 class='title'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)
    
    # Container for the experiment setup
    experiment_container = st.empty()

    def render_initial_state():
        experiment_container.markdown("""
            <div class='experiment-container'>
                <div class='beaker'>
                    <div class='solution solution-blue' style='height: 50%;'></div>
                    <div>H₂O₂</div>
                </div>
                <div class='cylinder'>
                    <div class='solution solution-grey' style='height: 50%;'></div>
                    <div>KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_reaction():
        experiment_container.markdown("""
            <div class='experiment-container'>
                <div class='beaker pour-animation'>
                    <div class='solution solution-blue' style='height: 50%;'></div>
                    <div>H₂O₂</div>
                </div>
                <div class='cylinder'>
                    <div class='reaction-foam'></div>
                    <div>KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.write("<script>triggerPourAnimation()</script>", unsafe_allow_html=True)
        time.sleep(2)

    render_initial_state()

    # Start Experiment button
    if st.button("Start Experiment"):
        animate_reaction()
        st.markdown("""
            <h3>Chemical Reaction:</h3>
            <p>2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</p>
            <p><em>Tip:</em> Adding food coloring or liquid soap enhances the visual effect!</p>
        """, unsafe_allow_html=True)

# Run the experiment
elephant_toothpaste_experiment()
