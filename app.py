import streamlit as st
import time

def run_experiment():
    st.set_page_config(page_title="Elephant Toothpaste Reaction")
    st.title("Elephant Toothpaste Reaction")

    # Display beaker and cylinder
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="height: 200px; width: 150px; background-color: #ADD8E6; border-radius: 10px; display: flex; justify-content: center; align-items: center; font-weight: bold;">
        H2O2
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="height: 200px; width: 150px; background-color: #D3D3D3; border-radius: 10px; display: flex; justify-content: center; align-items: center; font-weight: bold;">
        KI
        </div>
        """, unsafe_allow_html=True)

    if st.button("Start Experiment"):
        # Simulate pouring solution from beaker to cylinder
        st.write("Pouring solution...")
        time.sleep(2)

        # Simulate reaction
        st.write("**Dramatic reaction occurs!**")
        st.markdown("""
        <div style="height: 400px; width: 800px; background-color: #E6E6FA; border-radius: 10px; display: flex; justify-content: center; align-items: center; font-weight: bold; font-size: 24px;">
        🌋 FOAM EXPLOSION 🌋
        </div>
        """, unsafe_allow_html=True)

        # Display chemical equation
        st.markdown("**Chemical Equation:**")
        st.latex(r'2H_2O_2 (aq) \rightarrow 2H_2O (l) + O_2 (g)')

        # Provide note about optional additions
        st.write("*Note: Food coloring and liquid soap can be optionally added to the experiment.*")

run_experiment()
