import streamlit as st
import numpy as np
import time
from PIL import Image
import base64

def app():
    st.set_page_config(page_title="Acid-Base Titration Experiment")
    st.title("Acid-Base Titration Experiment")

    # Load the HTML animation
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Acid-Base Titration Animation</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }
            .experiment-container {
                position: relative;
                width: 200px;
                height: 400px;
            }
            .burette {
                position: absolute;
                top: 0;
                left: 80px;
                width: 10px;
                height: 300px;
                background-color: #ddd;
                border: 2px solid #aaa;
            }
            .drop {
                position: absolute;
                top: 50px;
                left: 80px;
                width: 6px;
                height: 10px;
                background-color: blue;
                border-radius: 50%;
                animation: drop 4s infinite;
            }
            @keyframes drop {
                0% { top: 50px; opacity: 1; }
                90% { top: 250px; opacity: 1; }
                100% { top: 250px; opacity: 0; }
            }
            .beaker {
                position: absolute;
                bottom: 0;
                left: 50px;
                width: 100px;
                height: 120px;
                border: 2px solid #aaa;
                border-top: none;
                background-color: #ff6666;
                transition: background-color 1s ease;
            }
            .beaker.color-change {
                background-color: #ffcc00;
            }
        </style>
    </head>
    <body>
        <div class="experiment-container">
            <div class="burette"></div>
            <div class="drop"></div>
            <div class="beaker" id="beaker"></div>
        </div>
        <script>
            // Change the color of the beaker after a delay
            setTimeout(() => {
                document.getElementById('beaker').classList.add('color-change');
            }, 4000);
        </script>
    </body>
    </html>
    """

    # Display the HTML animation
    st.write(f'<div style="text-align: center;">{html_code}</div>', unsafe_allow_html=True)

    # Add a start button
    if st.button("Start Experiment"):
        st.write("The experiment is in progress...")
        time.sleep(4)
        st.success("The experiment is complete!")

        # Plot the pH curve
        ph_values = np.linspace(0, 14, 100)
        titration_curve = 14 - ph_values
        st.line_chart(titration_curve)

if __name__ == "__main__":
    app()
