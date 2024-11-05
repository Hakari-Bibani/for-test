import streamlit as st
import time
from PIL import Image, ImageDraw
import imageio

st.title("🧪 Elephant Toothpaste Reaction 🧪")

# Drawing the initial setup with a larger cylinder containing KI solution
def draw_initial_cylinder():
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw the larger cylinder with KI solution (30% KI solution)
    draw.rectangle([(125, 100), (275, 350)], outline="black", width=3)
    draw.rectangle([(125, 250), (275, 350)], fill="lightgrey")
    draw.text((130, 360), "30% KI Solution", fill="black")
    
    return img

st.image(draw_initial_cylinder(), caption="Cylinder with KI Solution (30%)")

# Button to start the experiment
start_experiment = st.button("Start Experiment")

# Function to create pouring and reaction animation frames
def create_reaction_animation():
    frames = []
    
    # Pouring H2O2 into the cylinder
    for i in range(10):
        img = Image.new('RGB', (400, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw cylinder with KI solution
        draw.rectangle([(125, 100), (275, 350)], outline="black", width=3)
        draw.rectangle([(125, 250), (275, 350)], fill="lightgrey")
        draw.text((130, 360), "30% KI Solution", fill="black")
        
        # Simulate pouring H2O2
        draw.ellipse([(150 - i * 5, 100 - i * 10), (175 - i * 5, 125 - i * 10)], fill="lightblue")
        frames.append(img)
    
    # Foaming reaction animation
    for i in range(15):
        img = Image.new('RGB', (400, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw cylinder
        draw.rectangle([(125, 100), (275, 350)], outline="black", width=3)
        draw.rectangle([(125, 250), (275, 350)], fill="lightgrey")
        draw.text((130, 360), "30% KI Solution", fill="black")
        
        # Draw foam rising
        draw.rectangle([(125, 250 - i * 10), (275, 250)], fill="orange")
        for j in range(i):
            draw.ellipse([(125, 240 - j * 10), (275, 250 - j * 10)], fill="yellow")
        
        frames.append(img)

    # Save as GIF
    gif_path = "/mnt/data/elephant_toothpaste_reaction.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    
    return gif_path

# Display animation when button is pressed
if start_experiment:
    st.write("Pouring H₂O₂ into KI solution...")

    # Create and display GIF animation
    gif_path = create_reaction_animation()
    st.image(gif_path, caption="Elephant Toothpaste Reaction Animation", use_column_width=True)

    # Display reaction formula
    st.markdown("### Reaction Formula")
    st.write("2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)")
    st.write("Note: The food coloring and liquid soap enhance the reaction for dramatic effect.")
