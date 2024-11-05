import streamlit as st
import time
import streamlit.components.v1 as components

# Set up the app title
st.title("Test the pH of different solutions using litmus paper!")

# Display beakers with solutions and litmus paper image
st.image("/mnt/data/Screenshot 2024-11-05 012547.png", use_column_width=True)

# Show the start button
start = st.button("Start Test")

# If start button is pressed, begin the animation
if start:
    # Description of the beaker and paper colors
    st.write("Testing the solutions...")

    # Displaying the animation for 6 seconds
    with st.empty():
        for i in range(6):
            # Set the colors for each solution and paper (acid - red, base - blue, neutral - green)
            color_changes = [
                ("Hydrochloric Acid", "red"),
                ("Sodium Hydroxide", "blue"),
                ("Neutral Water", "lightgreen")
            ]

            # Display each step in the animation
            for solution, color in color_changes:
                st.write(f"The litmus paper in {solution} changes to {color}.")

            # Sleep for 1 second for the effect
            time.sleep(1)

        # Clear the animation after 6 seconds
        st.write("The test is complete. Press 'Start Test' to repeat.")
