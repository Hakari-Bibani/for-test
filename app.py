import streamlit as st
import time

def main():
    # Title with animation
    st.title("🐘🪥 Elephant Toothpaste Reaction 🧪")

    # Display containers for beaker and cylinder
    h2o2_container, ki_container = st.columns(2)
    
    with h2o2_container:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Hydrogen_peroxide_concentration.png/1280px-Hydrogen_peroxide_concentration.png",
                 caption="H₂O₂ Solution", width=200)
    
    with ki_container:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Large_graduated_cylinder.jpg/800px-Large_graduated_cylinder.jpg",
                 caption="30% KI Solution", width=200)

    # Button to start the experiment
    if st.button("Start Experiment"):
        st.write("🔄 Mixing H₂O₂ and KI...")

        # Simulate pouring and reaction steps
        with st.spinner("Pouring H₂O₂ into KI solution..."):
            time.sleep(2)

        # Reaction animation simulation (Text update for dramatic effect)
        st.write("💥 The reaction begins! Foam starts to rise...")

        # Simulated eruption (replace with more frames for better animation)
        for i in range(1, 6):
            st.write("🌊" * i + " Foam Erupting!" + " 🌊" * i)
            time.sleep(0.5)

        # Chemical equation
        st.markdown("""
        ### Chemical Reaction:
        **2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)**

        - This is an exothermic decomposition reaction.
        - The potassium iodide acts as a catalyst, breaking down the hydrogen peroxide rapidly.

        **Optional Enhancements:**
        - Add a few drops of food coloring for color.
        - Add liquid soap to trap oxygen bubbles, creating foam.
        """)

        # Option to restart the experiment
        st.button("Restart Experiment", on_click=lambda: st.experimental_rerun())

# Run the app
if __name__ == "__main__":
    main()
