import streamlit as st
import time

st.title("Test the pH of different solutions using litmus paper!")

# Display placeholders for the litmus paper and beakers
litmus_placeholder = st.empty()
beakers_placeholder = st.empty()

# Render litmus papers and beakers with initial colors and positions
def render_initial_state():
    with litmus_placeholder.container():
        st.write("### Litmus Papers")
        st.markdown(
            "<div style='display:flex; justify-content:space-around; margin-top:20px;'>"
            "<div style='background-color:paleyellow; width:50px; height:200px;'></div>"
            "<div style='background-color:paleyellow; width:50px; height:200px;'></div>"
            "<div style='background-color:paleyellow; width:50px; height:200px;'></div>"
            "</div>", unsafe_allow_html=True
        )
    with beakers_placeholder.container():
        st.write("### Beakers with Solutions")
        st.markdown(
            "<div style='display:flex; justify-content:space-around; margin-top:20px;'>"
            "<div style='background-color:lightgray; width:100px; height:200px;'><center>HCl</center></div>"
            "<div style='background-color:paleblue; width:100px; height:200px;'><center>H₂O</center></div>"
            "<div style='background-color:lightgray; width:100px; height:200px;'><center>NaOH</center></div>"
            "</div>", unsafe_allow_html=True
        )

# Define function to animate litmus paper dipping and color change
def start_experiment():
    with litmus_placeholder.container():
        st.markdown("<div style='display:flex; justify-content:space-around; margin-top:20px;'>"
                    "<div style='background-color:red; width:50px; height:200px;'></div>"
                    "<div style='background-color:lightgreen; width:50px; height:200px;'></div>"
                    "<div style='background-color:blue; width:50px; height:200px;'></div>"
                    "</div>", unsafe_allow_html=True)
    time.sleep(6)
    render_initial_state()

# Display initial setup
render_initial_state()

# Button to start the experiment
if st.button("Start"):
    start_experiment()
