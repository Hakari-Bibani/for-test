import streamlit as st

st.title("Elephant Toothpaste Reaction 🧪🐘")

st.write("**Let's simulate the experiment!**")

# Beaker and cylinder setup
st.write("Imagine a beaker filled with hydrogen peroxide (H₂O₂) and a cylinder filled with potassium iodide (KI) solution.")

# Start button
if st.button("Start Experiment"):

    # Pouring H₂O₂
    st.write("Pouring H₂O₂ into the cylinder...")
    st.write("**H₂O₂ 🧪 → Cylinder**")

    # Reaction
    st.write("A dramatic reaction occurs! 💥")
    st.write("Foamy bubbles rise rapidly, resembling a toothpaste eruption.")
    st.write("**Foam 🫧 ⬆️**")

    # Reaction equation
    st.write("Chemical Reaction:")
    st.write("2H₂O₂ (aq) + 2I⁻ (aq) → 2H₂O (l) + I₂ (aq) + O₂ (g)")

# Additional notes
st.write("**Note:**")
st.write("- For a more visual experience, consider watching a real-life demonstration on YouTube or other online platforms.")
st.write("- Always perform experiments under adult supervision and follow safety guidelines.")
