import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import plotly.graph_objects as go
import time

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Title
st.title("Acid Base Titration Simulation")

# Load the HTML content from the file
with open("animation.html", "r") as file:
    html_content = file.read()

# Embed the HTML content in Streamlit
components.html(html_content, height=600, scrolling=False)

# Button to start the experiment
if st.button("Start Experiment"):
    # Indicate that the experiment is starting
    st.write("Starting titration...")

    # Simulate the progress of the titration with a progress bar
    progress_bar = st.progress(0)
    status = st.empty()

    # Simulate titration progress
    for i in range(101):
        progress_bar.progress(i)
        if i < 80:
            status.text(f"Adding NaOH... ({i}%)")
        elif i < 90:
            status.text("Color changing to pink!")
        else:
            status.text("Titration complete!")
        time.sleep(0.2)

    # Generate and display the pH curve
    volume = np.linspace(0, 50, 100)
    equivalence_point = 25

    def calculate_ph(v):
        if v < equivalence_point:
            return -np.log10(abs(0.1 - (0.1 * v / equivalence_point)))
        elif abs(v - equivalence_point) < 0.1:
            return 7
        else:
            return 14 + np.log10(abs((0.1 * (v - equivalence_point)) / v))

    ph = [calculate_ph(v) for v in volume]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=volume,
        y=ph,
        mode='lines',
        name='pH curve'
    ))
    fig.add_trace(go.Scatter(
        x=[equivalence_point],
        y=[calculate_ph(equivalence_point)],
        mode='markers',
        marker=dict(size=10, color='red'),
        name='Equivalence Point'
    ))
    fig.update_layout(
        title='Titration Curve: HCl vs NaOH',
        xaxis_title='Volume of NaOH added (mL)',
        yaxis_title='pH',
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)

    st.success(f"""
        Titration Complete!
        - Equivalence Point reached at {equivalence_point} mL
        - pH at equivalence point: 7.0
        - Final color: Pink (phenolphthalein indicator)
    """)

# Add explanation
st.markdown("""
### What's happening in this titration?
1. The burette contains NaOH (0.1M strong base)
2. The conical flask contains HCl (0.1M strong acid)
3. As NaOH is added dropwise:
   - It neutralizes the HCl
   - The pH gradually increases
   - The phenolphthalein indicator remains colorless until pH ≈ 8.2
4. At the endpoint:
   - The solution turns pink
   - The pH curve shows a sharp increase
   - All acid has been neutralized
""")
