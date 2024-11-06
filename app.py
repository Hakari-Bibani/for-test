import streamlit as st
import time
from PIL import Image, ImageDraw

# Set page configuration
st.set_page_config(page_title="Titration Animation", layout="centered")

# Function to draw the titration setup
def draw_titration_setup(volume_added):
    img = Image.new("RGBA", (600, 400), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Draw the burette
    draw.rectangle([250, 50, 270, 350], outline="black", width=2)
    draw.rectangle([250, 50, 270, 50 + int(volume_added * 3)], fill=(135, 206, 250))  # Burette liquid

    # Draw the beaker
    draw.rectangle([150, 350, 450, 370], outline="black", width=2)
    draw.rectangle([150, 360, 450, 370], fill=(100, 149, 237))  # Initial pale blue color in beaker

    # Change beaker color gradually based on volume added
    if volume_added > 5:
        color_change_intensity = min(255, int((volume_added - 5) * 10))
        draw.rectangle([150, 360, 450, 370], fill=(255 - color_change_intensity, 149, 237))

    return img

# Display the title
st.title("Titration Animation")

# Description
st.markdown(
    "This simulation demonstrates a simple titration experiment. As the titrant is added from the burette, the color in the beaker changes gradually."
)

# Button to start titration
if st.button("Start Titration"):
    st.write("Titration in Progress...")

    # Simulate titration process
    for volume in range(0, 11):
        img = draw_titration_setup(volume)
        st.image(img, use_column_width=True)
        time.sleep(0.5)

    # Final message
    st.write("Titration Complete!")
