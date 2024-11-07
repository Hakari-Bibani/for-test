import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Title
st.title("Acid Base Titration Simulation")

# HTML container for the simulation
html_container = components.html("""
<div class="container">
  <svg width="100%" height="500" viewBox="0 0 800 500">
    <!-- Background -->
    <rect width="800" height="500" fill="#f5f5f5" />

    <!-- Burette -->
    <g id="burette">
      <rect x="350" y="50" width="40" height="200" fill="none" stroke="#333" stroke-width="2" />
      <rect x="340" y="30" width="60" height="20" fill="#333" />
      <path d="M370 250 L380 270 L360 270 Z" fill="#333" />
    </g>

    <!-- Flask -->
    <g id="flask">
      <path d="M300 450 Q270 450 250 420 L250 380 Q250 350 300 350 L440 350 Q490 350 490 380 L490 420 Q470 450 440 450 Z" fill="none" stroke="#333" stroke-width="2" />
      <rect id="flask-solution" x="252" y="352" width="236" height="68" fill="#e6f3ff" />
      <rect id="indicator" x="252" y="352" width="236" height="68" fill="transparent" />
    </g>

    <!-- Stand -->
    <g id="stand">
      <rect x="150" y="470" width="200" height="20" fill="#666" />
      <rect x="200" y="20" width="20" height="450" fill="#666" />
      <path d="M220 150 L330 150 L330 180 L220 180 Z" fill="#666" />
    </g>
  </svg>
</div>

<script>
  // Add the JavaScript code here
  // (same as the previous 'advanced-titration-final' artifact)
</script>
""", height=600)

# Start experiment button
if st.button("Start Experiment"):
    # Trigger the JavaScript function to start the experiment
    st.scriptify("""
        startExperiment();
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
