import streamlit as st
import time

# Streamlit page configuration
st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="centered")

# Dynamic title with animation
st.markdown("<h1 style='text-align: center; color: darkblue;'>🧪 Elephant Toothpaste Reaction 🧪</h1>", unsafe_allow_html=True)
st.write("A fun and colorful chemistry experiment simulation!")

# Display initial setup with text labels for H₂O₂ and KI solution
st.write("### 🧴 Experiment Setup")
st.write("1. Beaker containing **H₂O₂ (Hydrogen Peroxide)** solution.")
st.write("2. Larger cylinder containing **30% KI (Potassium Iodide) solution**.")

# Button to Start Experiment
start_button = st.button("Start Experiment")

if start_button:
    # Step 1: Display Pouring Effect
    st.write("### 🔄 Pouring H₂O₂ into the KI solution...")
    with st.empty():
        for i in range(5):
            st.write(f"Pouring...{'💧' * (i+1)}")
            time.sleep(0.3)
    
    # Step 2: The Reaction
    st.write("### 🎉 Reaction Begins!")
    with st.empty():
        for foam_level in range(1, 6):
            st.write("🧪" + "🌊" * foam_level)  # Simulating rising foam with emojis
            time.sleep(0.5)
    
    # Display the Chemical Equation
    st.write("### Chemical Equation")
    st.latex(r"2\text{H}_2\text{O}_2 \rightarrow 2\text{H}_2\text{O} + \text{O}_2")
    
    # Optional Ingredients Note
    st.write("📝 **Note:** For a more colorful reaction, you can add food coloring to the H₂O₂. "
             "Adding liquid soap will help trap the oxygen, creating even more foam!")

