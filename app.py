import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Title
st.title("Acid Base Titration Simulation")

# Load the HTML component
with open("animation.html", "r") as file:
    html_content = file.read()

# Display the HTML component
html_container = components.html(html_content, height=600)

# Start experiment button
if st.button("Start Experiment"):
    # Send message to start animation
    st.write("Starting experiment with three drops...")
    
    # This uses JavaScript to send a message to the HTML content
    # Use Streamlit's Markdown to inject the script
    st.markdown(
        """
        <script>
            window.addEventListener('load', function() {
                window.postMessage({type: 'start_experiment'}, '*');
            });
        </script>
        """,
        unsafe_allow_html=True
    )
