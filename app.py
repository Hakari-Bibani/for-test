import streamlit as st
import time

st.title("Test the pH of different solutions using litmus paper!")

# Placeholders for litmus paper and beakers display
litmus_placeholder = st.empty()
beakers_placeholder = st.empty()

# Function to render the initial setup with pale yellow litmus strips and realistic beakers
def render_initial_state():
    with litmus_placeholder.container():
        st.write("### Litmus Papers")
        st.markdown(
            """
            <div style='display:flex; justify-content:space-around;'>
                <div style='background-color: #FFFACD; width:30px; height:80px;'></div>
                <div style='background-color: #FFFACD; width:30px; height:80px;'></div>
                <div style='background-color: #FFFACD; width:30px; height:80px;'></div>
            </div>
            """, unsafe_allow_html=True
        )

    with beakers_placeholder.container():
        st.write("### Beakers with Solutions")
        st.markdown(
            """
            <div style='display:flex; justify-content:space-around; margin-top:20px;'>
                <div style='background-color: #D3D3D3; width:80px; height:150px; border-radius:50% 50% 20% 20%; text-align:center; padding-top:10px;'>HCl</div>
                <div style='background-color: #ADD8E6; width:80px; height:150px; border-radius:50% 50% 20% 20%; text-align:center; padding-top:10px;'>H₂O</div>
                <div style='background-color: #D3D3D3; width:80px; height:150px; border-radius:50% 50% 20% 20%; text-align:center; padding-top:10px;'>NaOH</div>
            </div>
            """, unsafe_allow_html=True
        )

# Function to animate litmus paper diving into beakers, changing colors, and returning
def start_experiment():
    # Step 1: Move litmus papers to the beakers
    with litmus_placeholder.container():
        st.markdown(
            """
            <div style='display:flex; justify-content:space-around; margin-top:100px;'>
                <div style='background-color: #FFFACD; width:30px; height:80px;'></div>
                <div style='background-color: #FFFACD; width:30px; height:80px;'></div>
                <div style='background-color: #FFFACD; width:30px; height:80px;'></div>
            </div>
            """, unsafe_allow_html=True
        )
    time.sleep(1)

    # Step 2: Display litmus papers inside the solutions with initial color change
    with litmus_placeholder.container():
        st.markdown(
            """
            <div style='display:flex; justify-content:space-around; margin-top:0px;'>
                <div style='background-color: #FF6347; width:30px; height:80px;'></div>  <!-- Acid turns red -->
                <div style='background-color: #90EE90; width:30px; height:80px;'></div>  <!-- Neutral turns light green -->
                <div style='background-color: #4682B4; width:30px; height:80px;'></div>  <!-- Base turns blue -->
            </div>
            """, unsafe_allow_html=True
        )
    time.sleep(3)  # Pause to show color change

    # Step 3: Lift the litmus papers back to their original positions with new colors
    with litmus_placeholder.container():
        st.markdown(
            """
            <div style='display:flex; justify-content:space-around;'>
                <div style='background-color: #FF6347; width:30px; height:80px;'></div>  <!-- Acid stays red -->
                <div style='background-color: #90EE90; width:30px; height:80px;'></div>  <!-- Neutral stays light green -->
                <div style='background-color: #4682B4; width:30px; height:80px;'></div>  <!-- Base stays blue -->
            </div>
            """, unsafe_allow_html=True
        )
    time.sleep(3)  # Show final state before resetting

    # Reset to the initial state
    render_initial_state()

# Display the initial setup
render_initial_state()

# Button to start the experiment
if st.button("Start Experiment"):
    start_experiment()
