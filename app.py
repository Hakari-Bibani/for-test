import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import log10

def app():
    st.set_page_config(page_title="Acid Base Titration")

    st.title("Acid Base Titration 🌊")

    # Create a beaker and a burette
    st.markdown(
        """
        <div style="position: relative; width: 400px; height: 500px;">
            <div style="position: absolute; bottom: 0; left: 0; width: 200px; height: 300px; background-color: #4682B4; border-radius: 20px; animation: wave 5s ease-in-out infinite;">
                <div style="position: absolute; bottom: 0; left: 50px; width: 100px; height: 200px; background-color: #FF0000; border-radius: 10px;"></div>
            </div>
            <div style="position: absolute; top: 100px; right: 50px; width: 50px; height: 300px; background-color: #008000; border-radius: 10px;"></div>
        </div>
        <style>
            @keyframes wave {
                0% { transform: translateX(-10px); }
                50% { transform: translateX(10px); }
                100% { transform: translateX(-10px); }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Start Experiment"):
        st.markdown(
            """
            <div style="position: relative; width: 400px; height: 500px;">
                <div style="position: absolute; bottom: 0; left: 0; width: 200px; height: 300px; background-color: #4682B4; border-radius: 20px; animation: wave 5s ease-in-out infinite;">
                    <div style="position: absolute; bottom: 0; left: 50px; width: 100px; height: 200px; background-color: #FF0000; border-radius: 10px; animation: add-naoh 10s linear forwards;">
                        <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 0%; background-color: #008000; border-radius: 10px;"></div>
                    </div>
                </div>
                <div style="position: absolute; top: 100px; right: 50px; width: 50px; height: 300px; background-color: #008000; border-radius: 10px;"></div>
            </div>
            <style>
                @keyframes wave {
                    0% { transform: translateX(-10px); }
                    50% { transform: translateX(10px); }
                    100% { transform: translateX(-10px); }
                }
                @keyframes add-naoh {
                    0% { height: 0%; }
                    100% { height: 100%; }
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Titration calculation
        volume_naoh = np.linspace(0, 50, 101)
        ph = 7 - log10(volume_naoh)

        # Plot the pH curve
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(volume_naoh, ph)
        ax.axvline(x=25, color='r', linestyle='--', label='Equivalence Point')
        ax.set_xlabel('Volume of NaOH (mL)')
        ax.set_ylabel('pH')
        ax.set_title('Acid Base Titration')
        ax.legend()

        st.pyplot(fig)
