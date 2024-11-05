import streamlit as st
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def app():
    st.set_page_config(page_title="Elephant Toothpaste Reaction")
    st.title("Elephant Toothpaste Reaction")

    # Create the initial scene
    beaker_x, beaker_y = 300, 200
    beaker_width, beaker_height = 100, 200
    cylinder_x, cylinder_y = 500, 200 
    cylinder_width, cylinder_height = 80, 160

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <div style="position: relative;">
                <div style="position: absolute; top: {beaker_y}px; left: {beaker_x}px; width: {beaker_width}px; height: {beaker_height}px; background-color: #ADD8E6; border: 2px solid black;"></div>
                <div style="position: absolute; top: {cylinder_y}px; left: {cylinder_x}px; width: {cylinder_width}px; height: {cylinder_height}px; background-color: #D3D3D3; border: 2px solid black;"></div>
                <div style="position: absolute; top: {beaker_y + beaker_height//2}px; left: {beaker_x + beaker_width//2}px; font-weight: bold;">H2O2</div>
                <div style="position: absolute; top: {cylinder_y + cylinder_height//2}px; left: {cylinder_x + cylinder_width//2}px; font-weight: bold;">KI</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Start Experiment"):
        # Animation of pouring solution
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_xlim(0, 800)
        ax.set_ylim(0, 400)
        ax.set_axis_off()

        beaker_liquid_height = beaker_height // 2
        cylinder_liquid_height = cylinder_height // 2

        def animate(frame):
            ax.clear()

            # Draw beaker
            ax.add_patch(plt.Rectangle((beaker_x, beaker_y), beaker_width, beaker_height, fill=False, color='black'))

            # Draw beaker liquid
            ax.add_patch(plt.Rectangle((beaker_x, beaker_y + beaker_height - beaker_liquid_height), beaker_width, beaker_liquid_height, color='#ADD8E6'))

            # Draw cylinder
            ax.add_patch(plt.Rectangle((cylinder_x, cylinder_y), cylinder_width, cylinder_height, fill=False, color='black'))

            # Draw cylinder liquid
            ax.add_patch(plt.Rectangle((cylinder_x, cylinder_y + cylinder_height - cylinder_liquid_height), cylinder_width, cylinder_liquid_height, color='#D3D3D3'))

            # Animate the pouring
            if frame < 50:
                beaker_liquid_height -= 4
                cylinder_liquid_height += 4
            else:
                # Dramatic reaction
                cylinder_liquid_height = 0
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 80, color='#FFA500'))
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 70, color='#FF4500'))
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 60, color='#8B4513'))
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 50, color='#FFD700'))
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 40, color='#00FF00'))
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 30, color='#00BFFF'))
                ax.add_patch(plt.Circle((cylinder_x + cylinder_width // 2, cylinder_y + cylinder_height // 2), 20, color='#9370DB'))

            return ax.get_images() + ax.patches

        ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
        st.pyplot(fig)

        # Show chemical equation
        st.markdown(
            """
            Chemical Equation:
            2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)

            *Note: Food coloring and liquid soap can be added for a more dramatic effect, but should not be added before the animation.*
            """
        )
