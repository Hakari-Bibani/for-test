import streamlit as st
from PIL import Image

# Animation libraries (choose one based on preference and complexity)
# Option 1: Using matplotlib animation (simpler, good for basic animations)
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Option 2: Using libraries like moviepy or ffmpeg (more complex, allows for richer visual effects)
# from moviepy.editor import VideoFileClip  # (or ffmpeg)

# Function for the pouring animation (using matplotlib animation)
def animate_pouring(frames):
    fig, ax = plt.subplots()
    ax.set_ylim(0, 10)  # Adjust y-limits for pouring animation
    line, = ax.plot([], [], lw=2)

    def animate(i):
        y_data = frames[i]
        line.set_data([0, 1], [0, y_data])
        return line,

    anim = FuncAnimation(fig, animate, frames=frames, interval=100, blit=True)
    st.pyplot(anim)

# Function for the reaction animation (using matplotlib animation)
def animate_reaction(frames):
    fig, ax = plt.subplots()
    ax.set_ylim(0, 15)  # Adjust y-limits for reaction animation
    foam, = ax.plot([], [], color='lightcoral', lw=2)

    def animate(i):
        y_data = frames[i]
        foam.set_data([0, 1], [0, y_data])
        return foam,

    anim = FuncAnimation(fig, animate, frames=frames, interval=100, blit=True)
    st.pyplot(anim)

# Load beaker and cylinder images
beaker_image = Image.open("beaker.png")  # Replace with your beaker image file
cylinder_image = Image.open("cylinder.png")  # Replace with your cylinder image file

# Experiment state variables
st.session_state.experiment_started = False
h2o2_level = 0  # Track H2O2 level for animation (0-10)
foam_level = 0  # Track foam level for animation (0-15)
frames_pouring = range(1, 11)  # Frames for pouring animation
frames_reaction = range(1, 16)  # Frames for reaction animation
reaction_notes = "2H₂O₂ (aq) + 2H₂O (l) + KI (aq) → O₂ (g) + I₂ (aq) + H₂O (l)"  # Updated reaction equation

st.title("Elephant Toothpaste Reaction")

# Display beaker and cylinder images (adjust positioning as needed)
st.image(beaker_image, width=200, use_column_width=True)
st.image(cylinder_image, width=300, use_column_width=True)

# Display "30% KI solution" text
st.caption("30% KI solution (light grey)")

# Start experiment button
if st.button("Start Experiment"):
    st.session_state.experiment_started = True

if st.session_state.experiment_started:
    # Animate pouring H2O2
    animate_pouring(frames_pouring)

    # Simulate reaction delay
    st.write("Adding catalyst...")
    st.success("Reaction starting!")

    # Animate foam rising
    animate_reaction(frames_reaction)

    # Display reaction notes
    st.markdown(reaction_notes)

# Additional notes (optional)
st.write("**Safety:**")
st.write("- Adult supervision is recommended for children.")
st.write("- Perform the experiment in a well-ventilated area.")
st.write("- Wear gloves and goggles for protection.")
st.write("- Dispose of waste properly.")

st.write("**Food coloring and liquid soap (optional):**")
st.write("- These can be added to the hydrogen peroxide for a more visually appealing reaction.")

# Choose the animation library you prefer (comment out the other option):
# st.pyplot(animate_pouring(frames_pouring))  # Using matplotlib animation for pouring
# st.pyplot(animate_reaction(frames_reaction))  # Using matplotlib animation for reaction

# Example usage with moviepy or ffmpeg (more complex setup):
# clip = VideoFileClip("pouring.mp
