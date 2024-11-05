import streamlit as st

st.title("Elephant Toothpaste Reaction 🧪🐘")

st.write("**Let's simulate the experiment!**")

# Beaker and cylinder setup
st.write("Imagine a beaker filled with hydrogen peroxide (H₂O₂) and a cylinder filled with potassium iodide (KI) solution.")

# Start button
if st.button("Start Experiment"):

    # Pouring H₂O₂
    st.write("Pouring H₂O₂ into the cylinder...")
    progress = st.progress(0)
    for i in range(10):
        progress.progress(i + 1)
        st.write(f"H₂O₂ level: {i+1}/10")

    # Reaction
    st.write("A dramatic reaction occurs! 💥")
    st.write("Foamy bubbles rise rapidly, resembling a toothpaste eruption.")
    progress = st.progress(0)
    for i in range(20):
        progress.progress(i + 1)
        st.write(f"Foam level: {i+1}/20")

    # Reaction equation
    st.write("Chemical Reaction:")
    st.write("2H₂O₂ (aq) + 2I⁻ (aq) → 2H₂O (l) + I₂ (aq) + O₂ (g)")

    # Final message
    st.write("The reaction is complete! The foamy eruption has subsided.")
