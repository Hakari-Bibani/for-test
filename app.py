import streamlit as st
import time
from PIL import Image

def run_experiment():
    st.title("Elephant Toothpaste Reaction")

    # Display beaker and cylinder
    col1, col2 = st.columns(2)
    with col1:
        beaker = Image.open("beaker.png")
        st.image(beaker, caption="H2O2")
    with col2:
        cylinder = Image.open("cylinder.png")
        st.image(cylinder, caption="KI")

    if st.button("Start Experiment"):
        # Simulate pouring solution from beaker to cylinder
        st.write("Pouring solution...")
        time.sleep(2)

        # Simulate reaction
        st.write("**Dramatic reaction occurs!**")
        reaction = Image.open("reaction.png")
        st.image(reaction, use_column_width=True)

        # Display chemical equation
        st.markdown("**Chemical Equation:**")
        st.latex(r'2H_2O_2 (aq) \rightarrow 2H_2O (l) + O_2 (g)')

        # Provide note about optional additions
        st.write("*Note: Food coloring and liquid soap can be optionally added to the experiment.*")

run_experiment()
