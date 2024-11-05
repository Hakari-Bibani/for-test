import streamlit as st
import time
from PIL import Image, ImageDraw

st.title("🧪 Elephant Toothpaste Reaction 🧪")

# Draw initial setup with a larger cylinder containing KI solution
def draw_initial_cylinder():
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw the larger cylinder with KI solution
    draw.rectangle([(125, 100), (275, 350)], outline="black", width=3)
    draw.rectangle([(125, 250), (275, 350)], fill="lightgrey")
    draw.text((130, 360), "30% KI Solution", fill="black")
    
    return img

# Show initial setup
st.image(draw_initial_cylinder(), caption="Cylinder with KI Solution (30%)")

# Button to start the experiment
start_experiment = st.button("Start Experiment")

# Function to create frames for pouring and reaction sequence
def create_reaction_frames():
    frames = []
    
    # Pouring H2O2 into the cylinder
    for i in range(10):
        img = Image.new('RGB', (400, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Cylinder with KI solution
        draw.rectangle([(125, 100), (275, 350)], outline="black", width=3)
        draw.rectangle([(125, 250), (275, 350)], fill="lightgrey")
        draw.text((130, 360), "30% KI Solution", fill="black")
        
        # Pouring H2O2
        draw.ellipse([(150 - i * 5, 100 - i * 10), (175 - i * 5, 125 - i * 10)], fill="lightblue")
        frames.append(img)
    
    # Foaming reaction frames
    for i in range(15):
        img = Image.new('RGB', (400, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Cylinder with KI solution
        draw.rectangle([(125, 100), (275, 350)], outline="black", width=3)
        draw.rectangle([(125, 250), (275, 350)], fill="lightgrey")
        draw.text((130, 360), "30% KI Solution", fill="black")
        
        # Foam rising out of the cylinder
        draw.rectangle([(125, 250 - i * 10), (275, 250)], fill="orange")
        for j in range(i):
            draw.ellipse([(125, 240 - j * 10), (275, 250 - j * 10)], fill="yellow")
        
        frames.append(img)
    
    return frames

# Display frames in sequence to simulate animation
if start_experiment:
    st.write("Pouring H₂O₂ into KI solution...")

    # Generate frames
    frames = create_reaction_frames()

    # Display each frame with a slight delay to simulate animation
    for frame in frames:
        st.image(frame, use_column_width=True)
        time.sleep(0.2)  # Delay to create an animation effect

    # Display reaction formula and notes
    st.markdown("### Reaction Formula")
    st.write("2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")
    st.write("Note: The food coloring and liquid soap enhance the reaction for dramatic effect.")
