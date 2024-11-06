import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Title
st.title("Acid Base Titration Simulation")

# Load the HTML content
with open("animation.html", "r") as file:
    html_content = file.read()

# Display the HTML content
html_container = components.html(html_content, height=600)

# Add JavaScript to start the experiment when the button is pressed
if st.button("Start Experiment"):
    # Use Streamlit's custom HTML and JavaScript injection to send a signal
    st.write("Starting experiment with three drops...")

    # Inject JavaScript to trigger the animation
    st.components.v1.html(
        """
        <script>
            // Trigger the experiment start function in the HTML
            window.addEventListener('DOMContentLoaded', (event) => {
                setTimeout(() => {
                    window.postMessage({type: 'start_experiment'}, '*');
                }, 100); // Small delay to ensure the content loads
            });
        </script>
        """,
        height=0
    )
