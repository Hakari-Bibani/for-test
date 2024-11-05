import streamlit as st
import time
from PIL import Image, ImageDraw

# Set the title
st.title("Test the pH of different solutions using litmus paper!")

# Display initial image of three yellow litmus strips and three beakers
initial_image = Image.open("/mnt/data/Screenshot 2024-11-05 012547.png")
st.image(initial_image, caption="Initial setup with yellow litmus paper strips above each beaker")

# Start button for the test
start = st.button("Start Test")

# Define a function to change the color of the litmus paper based on solution
def color_litmus(paper_color, solution_color):
    image = initial_image.copy()
    draw = ImageDraw.Draw(image)

    # Coordinates for the litmus strips in the beakers (center of each beaker)
    litmus_positions = [(130, 100), (400, 100), (670, 100)]
    
    for pos, color in zip(litmus_positions, paper_color):
        draw.rectangle([pos[0], pos[1], pos[0] + 20, pos[1] + 80], fill=color)

    # Draw beaker color
    solution_positions = [(130, 160), (400, 160), (670, 160)]
    for pos, color in zip(solution_positions, solution_color):
        draw.rectangle([pos[0], pos[1], pos[0] + 100, pos[1] + 200], fill=color)

    return image

# If Start button is pressed, show the litmus paper changing colors
if start:
    st.write("Testing...")

    # Initial setup with beakers containing different solutions
    solution_colors = ["lightgray", "lightgray", "pale blue"]  # Colors for acid, base, and neutral
    paper_colors = ["yellow", "yellow", "yellow"]  # Initial color of the litmus papers (all yellow)

    # First step: papers dive into beakers
    for i in range(3):
        st.image(color_litmus(paper_colors, solution_colors), caption="Dipping litmus paper into solutions")
        time.sleep(1)

    # Second step: change litmus paper colors after reaction
    paper_colors = ["red", "blue", "lightgreen"]  # Colors after reaction (red for acid, blue for base, green for neutral)
    st.image(color_litmus(paper_colors, solution_colors), caption="Litmus paper changes color based on pH")
    
    time.sleep(6)  # Show the result for 6 seconds before resetting
    st.write("Test complete! Press 'Start Test' to repeat.")
