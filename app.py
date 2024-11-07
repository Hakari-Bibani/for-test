import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import log10

# Define the titration parameters
c_hcl = 0.1  # Concentration of HCl
c_naoh = 0.1  # Concentration of NaOH
v_hcl = 50    # Volume of HCl
v_naoh = 0    # Volume of NaOH

# Define the function to calculate pH
def calculate_ph(v_naoh):
    ph = 7 - log10(c_hcl * v_hcl / (v_hcl + v_naoh))
    return ph

# Create the Streamlit app
st.set_page_config(page_title="Acid-Base Titration")
st.title("Acid-Base Titration")

# Add a wave animation for the title
st.markdown(
    """
    <style>
    .title-wave {
        font-size: 36px;
        font-weight: bold;
        background-image: linear-gradient(to right, #4CAF50, #2196F3, #E91E63);
        background-size: 200% auto;
        color: #fff;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: wave 5s ease infinite;
    }
    @keyframes wave {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    <div class="title-wave">Acid-Base Titration</div>
    """,
    unsafe_allow_html=True
)

# Add a button to start the experiment
if st.button("Start Experiment"):
    # Create the burette and conical flask
    st.image("https://via.placeholder.com/300x400?text=Burette+and+Conical+Flask", width=300)

    # Animate the addition of NaOH to HCl
    for i in range(50):
        v_naoh += 0.5
        ph = calculate_ph(v_naoh)
        st.write(f"Adding NaOH: Volume of NaOH = {v_naoh:.1f} mL, pH = {ph:.2f}")
        st.balloons()
        plt.figure(figsize=(8, 6))
        plt.plot([0, v_naoh], [calculate_ph(0), ph])
        plt.xlabel("Volume of NaOH (mL)")
        plt.ylabel("pH")
        plt.title("Acid-Base Titration")
        st.pyplot(plt)
        plt.close()
        st.write("Waiting for color change...")
        st.write("Color changed!")
        st.stop()
