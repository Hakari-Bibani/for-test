import streamlit as st
import time

def main():
    # Title
    st.markdown("<h1 style='text-align: center;'>Elephant Toothpaste Reaction</h1>", unsafe_allow_html=True)

    # CSS Styling and Animations
    st.markdown("""
    <style>
        /* Title animation */
        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
        }
        
        /* Beaker and Cylinder styling */
        .beaker {
            width: 100px;
            height: 150px;
            background-color: rgba(176,224,230,0.7);
            border: 3px solid #2c3e50;
            border-radius: 5px;
            display: inline-block;
            margin-right: 30px;
            position: relative;
            top: -20px;
            transition: transform 2s;
        }
        .cylinder {
            width: 80px;
            height: 130px;
            background-color: rgba(169,169,169,0.7);
            border: 3px solid #2c3e50;
            border-radius: 10px;
            display: inline-block;
            position: relative;
        }

        /* Pouring animation */
        .beaker.pour {
            transform: rotate(45deg);
        }

        /* Foam explosion animation */
        .foam {
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 30px;
            height: 30px;
            background: linear-gradient(to top, #ff6347, #ffa07a, #f08080);
            animation: foamExplosion 2s ease-in-out forwards;
            opacity: 0;
        }
        @keyframes foamExplosion {
            0% { height: 30px; opacity: 1; }
            50% { height: 200px; opacity: 0.9; }
            100% { height: 350px; opacity: 0.5; }
        }

        /* Button styling */
        .stButton>button {
            background: #d3d3d3;
            color: #2c3e50;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 600;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: #c0c0c0;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(211, 211, 211, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

    # Display beaker and cylinder
    container = st.container()
    with container:
        st.markdown("""
        <div style="display: flex; align-items: flex-start;">
            <div class="beaker" id="beaker">H₂O₂</div>
            <div class="cylinder" id="cylinder">KI</div>
        </div>
        """, unsafe_allow_html=True)

    # Start Experiment Button
    if st.button("Start Experiment"):
        # Animate the beaker tilt and foam explosion
        st.markdown("""
        <script>
            const beaker = document.getElementById('beaker');
            const cylinder = document.getElementById('cylinder');

            // Tilt beaker to simulate pouring
            beaker.classList.add('pour');

            // Delay to simulate foam explosion
            setTimeout(() => {
                const foam = document.createElement('div');
                foam.classList.add('foam');
                cylinder.appendChild(foam);
            }, 2000);
        </script>
        """, unsafe_allow_html=True)

        # Display chemical reaction equation
        time.sleep(3)
        st.markdown("### Reaction Equation")
        st.markdown("2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")

        # Optional note
        st.info("Optional: Add food coloring and liquid soap to enhance the reaction's visual effect.")

    # Repeat Experiment Button
    if st.button("Repeat Experiment"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
