import streamlit as st
import numpy as np
import time
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def run_experiment():
    st.title("Elephant Toothpaste Reaction")

    # Display beaker and cylinder
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/150x200?text=H2O2", caption="H2O2")
    with col2:
        st.image("https://via.placeholder.com/150x200?text=KI", caption="KI")

    if st.button("Start Experiment"):
        # Animate pouring solution from beaker to cylinder
        lottie_url = "https://assets4.lottiefiles.com/packages/lf20_FI4tnv.json"
        lottie_animation = load_lottie_url(lottie_url)
        st_lottie(lottie_animation, height=300, width=600)

        # Simulate reaction
        time.sleep(2)
        st.markdown("**Dramatic reaction occurs!**")
        lottie_url = "https://assets4.lottiefiles.com/packages/lf20_KvMFxO.json"
        lottie_animation = load_lottie_url(lottie_url)
        st_lottie(lottie_animation, height=400, width=800)

        # Display chemical equation
        st.markdown("**Chemical Equation:**")
        st.latex(r'2H_2O_2 (aq) \rightarrow 2H_2O (l) + O_2 (g)')

        # Provide note about optional additions
        st.write("*Note: Food coloring and liquid soap can be optionally added to the experiment.*")

run_experiment()
