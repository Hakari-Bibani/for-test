import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
st.write("""
<style>
  .burette, .beaker {
    width: 100px;
    height: 300px;
    position: relative;
    display: inline-block;
    margin: 20px;
  }

  .burette-liquid, .beaker-liquid {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #ccc;
    transition: height 1s;
  }

  .burette-liquid {
    height: 0%;
  }

  .beaker-liquid {
    height: 0%;
    background-color: #fff;
  }
</style>

<div class="burette">
  <div class="burette-liquid"></div>
</div>
<div class="beaker">
  <div class="beaker-liquid"></div>
</div>
""", unsafe_allow_html=True)

# Add start experiment button
if st.button("Start Experiment"):
    # Animate burette and beaker
    beaker_liquid = st.markdown("""
    <script>
      const beakerLiquid = document.querySelector('.beaker-liquid');
      beakerLiquid.style.height = '50%';
      beakerLiquid.style.backgroundColor = '#ff0000';

      const buretteLiquid = document.querySelector('.burette-liquid');
      buretteLiquid.style.height = '20%';
    </script>
    """, unsafe_allow_html=True)

    # Plot pH curve
    x = np.linspace(0, 14, 100)
    y = 7 - np.log10(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y)
    ax.set_xlabel('Volume of NaOH (mL)')
    ax.set_ylabel('pH')
    ax.set_title('pH Curve')
    ax.axvline(x=7.1, color='r', linestyle='--', label='Equivalence Point')
    ax.legend()

    st.pyplot(fig)
