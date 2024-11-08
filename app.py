import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Load the Lottie animation
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

titration_animation = load_lottie("https://assets4.lottiefiles.com/packages/lf20_zqlcuhax.json")

st.set_page_config(page_title="Acid-Base Titration Experiment")

st.title("Acid-Base Titration Experiment")

# Display the burette and beaker
st.write("""
  <div style="display: flex; justify-content: center;">
    <img src="https://via.placeholder.com/150x300" alt="Burette">
    <img src="https://via.placeholder.com/150x300" alt="Beaker">
  </div>
""", unsafe_allow_html=True)

if st.button("Start Experiment"):
    # Display the titration animation
    st_lottie(titration_animation, height=400, width=400, key="titration")

    # Display the pH plot
    st.subheader("pH Plot")
    st.write("""
      ```mermaid
      graph LR
        A[Start] --> B{pH}
        B --> |Decreasing| C[Endpoint]
        B --> |Increasing| D[Endpoint]
      ```
    """, unsafe_allow_html=True)
