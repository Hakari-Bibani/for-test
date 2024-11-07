import streamlit as st
import plotly.graph_objs as go
import numpy as np

# Streamlit UI
st.title("Interactive Titration Animation: Adding NaOH to HCl Solution")

# Example data for titration
volume_naoh = np.linspace(0, 50, 100)  # Volume of NaOH added in mL
pH_values = 1 + (13 * volume_naoh / (50 + volume_naoh))  # Simplified pH change curve

# Create a Plotly figure
fig = go.Figure()

# Initial trace (empty)
fig.add_trace(go.Scatter(x=[], y=[], mode="lines+markers", name="pH Curve"))

# Frames for the animation
frames = [
    go.Frame(
        data=[go.Scatter(x=volume_naoh[:i], y=pH_values[:i], mode="lines+markers")],
        name=str(i),
    )
    for i in range(1, len(volume_naoh))
]

# Add frames to the figure
fig.frames = frames

# Layout for the animation
fig.update_layout(
    title="Titration of HCl with NaOH",
    xaxis=dict(title="Volume of NaOH (mL)", range=[0, 50]),
    yaxis=dict(title="pH", range=[0, 14]),
    updatemenus=[
        dict(
            type="buttons",
            showactive=False,
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}],
                ),
            ],
        )
    ],
)

# Add animation to Streamlit
st.plotly_chart(fig)
