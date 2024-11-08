import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Set page configuration
st.set_page_config(page_title="Acid-Base Titration")

# Add title with animation
st.write("""
<style>
  .title {
    font-size: 36px;
    font-weight: bold;
    animation: move-title 2s infinite alternate;
  }

  @keyframes move-title {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
  }
</style>

<div class="title">Acid-Base Titration</div>
""", unsafe_allow_html=True)

# Experiment setup
st.write("""
## Experiment Setup
This experiment demonstrates the titration of Hydrochloric Acid (HCl) with Sodium Hydroxide (NaOH). A burette containing NaOH solution is used to titrate a beaker of HCl solution.
""")

# Add burette and beaker
burette_height = 300
beaker_height = 200
burette_liquid_height = 0
beaker_liquid_height = 0

burette = st.empty()
beaker = st.empty()

# Add start experiment button
if st.button("Start Experiment"):
    # Animate burette and beaker
    for i in range(1, 21):
        burette_liquid_height = i * (burette_height / 20)
        beaker_liquid_height = i * (beaker_height / 20)
        burette.markdown(f"""
        <div class="burette" style="height:{burette_height}px;width:100px;">
          <div class="burette-liquid" style="height:{burette_liquid_height}px;background-color:#ccc;"></div>
        </div>
        """, unsafe_allow_html=True)
        beaker.markdown(f"""
        <div class="beaker" style="height:{beaker_height}px;width:100px;">
          <div class="beaker-liquid" style="height:{beaker_liquid_height}px;background-color:#ff0000;"></div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

    # Plot pH curve
    x = np.linspace(0, 14, 100)
    y = 7 - np.log10(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y)
    ax.set_xlabel('Volume of NaOH (mL)')
    ax.set_ylabel('pH')
    ax.set_title('pH Curve')
    ax.axvline(x=7.1, color='r', linestyle='--', label='Equivalence Point')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 14)
    ax.legend()

    st.pyplot(fig)
