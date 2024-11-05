import streamlit as st
import time

def run_experiment():
    # Custom CSS styling and animations
    st.markdown("""
    <style>
        .title {
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .beaker-container {
            display: flex;
            justify-content: space-around;
            padding: 20px;
            position: relative;
        }
        .beaker, .cylinder {
            width: 80px;
            height: 150px;
            border: 3px solid #ddd;
            border-radius: 5px;
            position: relative;
            overflow: hidden;
            margin: 20px;
            text-align: center;
        }
        .solution {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 50%;
            border-radius: 0 0 10px 10px;
            transition: all 1.5s ease;
        }
        .reaction-foam {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            background: radial-gradient(circle, #ffb3b3, #ff7373, #ff3333);
            border-radius: 50%;
            animation: eruption 1s ease-out;
        }
        @keyframes eruption {
            from { width: 0; height: 0; }
            to { width: 200px; height: 200px; bottom: 150px; }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display Title
    st.markdown("<h1 class='title'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)

    # Set up containers for beaker and cylinder
    container = st.container()
    with container:
        st.markdown("""
            <div class='beaker-container'>
                <div class='beaker'>
                    <div class='solution' style='background: lightblue;'></div>
                    <p>H₂O₂</p>
                </div>
                <div class='cylinder'>
                    <div class='solution' style='background: lightgrey;'></div>
                    <p>KI</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def animate_experiment():
        # Simulate beaker tilting and pouring solution
        time.sleep(1)
        st.markdown("""
            <style>
                .beaker .solution { height: 0%; }
                .cylinder .solution { height: 0%; }
            </style>
            <div class='reaction-foam'></div>
        """, unsafe_allow_html=True)
        time.sleep(2)

        # Display reaction equation and notes
        st.markdown("### Reaction Equation: 2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")
        st.markdown("**Note:** Adding food coloring and liquid soap can create a colorful and bubbly reaction.")

    if st.button("Start Experiment"):
        animate_experiment()

# Run the experiment in Streamlit
run_experiment()
