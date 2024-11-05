import streamlit as st
import time
from PIL import Image, ImageDraw

# Set up the title
st.title("🧪 Elephant Toothpaste Reaction 🧪")

# Instructions
st.markdown("## Instructions:")
st.write("Observe the setup below, and press the 'Start Experiment' button to see the reaction take place!")

# Drawing the initial setup with H2O2 in a beaker and KI in a cylinder
def draw_initial_setup():
    # Create an image with a half-filled beaker and cylinder
    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw beaker with H2O2
    draw.rectangle([(50, 50), (150, 250)], outline="black", width=3)
    draw.rectangle([(50, 150), (150, 250)], fill="lightblue")
    draw.text((60, 260), "H2O2 (Hydrogen Peroxide)", fill="black")
    
    # Draw cylinder with KI
    draw.rectangle([(250, 100), (350, 250)], outline="black", width=3)
    draw.rectangle([(250, 175), (350, 250)], fill="lightgrey")
    draw.text((260, 260), "30% KI Solution", fill="black")
    
    return img

st.image(draw_initial_setup(), caption="Initial Setup: H2O2 & KI")

# Start experiment button
start_experiment = st.button("Start Experiment")

# Function to create the reaction animation
def create_reaction_animation():
    frames = []
    for i in range(15):
        # Create base image
        img = Image.new('RGB', (400, 300), color='white')
        draw = ImageDraw.Draw(img)

        # Beaker with H2O2
        draw.rectangle([(50, 50), (150, 250)], outline="black", width=3)
        if i < 7:  # Pouring animation
            draw.rectangle([(50, 150 - i * 10), (150, 250)], fill="lightblue")
        else:
            draw.rectangle([(50, 150), (150, 250)], fill="lightblue")

        # Cylinder with foaming reaction
        draw.rectangle([(250, 100), (350, 250)], outline="black", width=3)
        if i >= 7:  # Foam rising
            draw.ellipse([(250, 100 - i * 10), (350, 100)], fill="yellow")
            for j in range(i - 6):
                draw.ellipse([(250, 70 - j * 20), (350, 100 - j * 20)], fill="orange")
        
        frames.append(img)

    return frames

if start_experiment:
    st.write("Pouring H2O2 into KI solution...")
    
    # Display pouring animation
    for frame in create_reaction_animation():
        st.image(frame)
        time.sleep(0.2)  # Delay to animate reaction

    # Display reaction notes
    st.markdown("### Reaction Formula")
    st.write("2H2O2 (aq) → 2H2O (l) + O2 (g)")
    st.write("Note: The food coloring and liquid soap enhance the reaction for dramatic effect.")
