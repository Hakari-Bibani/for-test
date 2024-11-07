import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import plotly.graph_objects as go
import time

# Set page configuration
st.set_page_config(page_title="Acid Base Titration", layout="wide")

# Title
st.title("Acid Base Titration Simulation")

# HTML code for the animation
html_code = """
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      width: 100%;
      height: 500px;
      background: #f5f5f5;
      position: relative;
    }
    
    #solution {
      animation: colorChange 1s ease-in-out;
      animation-play-state: paused;
    }
    
    #drop {
      opacity: 0;
      animation: dropFall 1s infinite;
      animation-play-state: paused;
    }
    
    @keyframes dropFall {
      0% {
        transform: translateY(0);
        opacity: 1;
      }
      100% {
        transform: translateY(150px);
        opacity: 0;
      }
    }
    
    @keyframes colorChange {
      0% { fill: #e6f3ff; }
      100% { fill: #ffcce6; }
    }
    
    #burette-solution {
      animation: decreaseLevel 5s linear;
      animation-play-state: paused;
    }
    
    @keyframes decreaseLevel {
      from { height: 200px; }
      to { height: 180px; }
    }
  </style>
</head>
<body>
  <div class="container">
    <svg width="100%" height="100%" viewBox="0 0 800 500">
      <!-- Background -->
      <rect width="800" height="500" fill="#f5f5f5"/>
      
      <!-- Burette -->
      <g id="burette">
        <!-- Burette body -->
        <rect x="350" y="50" width="40" height="250" fill="none" stroke="#333" stroke-width="2"/>
        <!-- Burette top -->
        <rect x="340" y="30" width="60" height="20" fill="#333"/>
        <!-- Burette tip -->
        <path d="M370 300 L380 320 L360 320 Z" fill="#333"/>
        <!-- Scale marks -->
        <g stroke="#333" stroke-width="1">
          <line x1="340" y1="70" x2="345" y2="70"/>
          <line x1="340" y1="120" x2="345" y2="120"/>
          <line x1="340" y1="170" x2="345" y2="170"/>
          <line x1="340" y1="220" x2="345" y2="220"/>
          <line x1="340" y1="270" x2="345" y2="270"/>
        </g>
        <!-- Solution in burette -->
        <rect id="burette-solution" x="351" y="51" width="38" height="200" fill="#e6f3ff"/>
      </g>
      
      <!-- Dropping solution -->
      <circle id="drop" cx="370" cy="325" r="3" fill="#e6f3ff"/>
      
      <!-- Flask -->
      <g id="flask">
        <!-- Flask body -->
        <path d="M300 450 Q270 450 250 420 L250 380 Q250 350 300 350 L440 350 Q490 350 490 380 L490 420 Q470 450 440 450 Z" 
              fill="none" stroke="#333" stroke-width="2"/>
        <!-- Solution in flask -->
        <path id="solution" 
              d="M252 420 L252 382 Q252 352 300 352 L440 352 Q488 352 488 382 L488 420 Q468 448 440 448 L300 448 Q272 448 252 420 Z" 
              fill="#e6f3ff"/>
      </g>
      
      <!-- Stand -->
      <g id="stand">
        <!-- Base -->
        <rect x="150" y="470" width="200" height="20" fill="#666"/>
        <!-- Pole -->
        <rect x="200" y="20" width="20" height="450" fill="#666"/>
        <!-- Clamp -->
        <path d="M220 150 L330 150 L330 180 L220 180 Z" fill="#666"/>
      </g>
    </svg>
  </div>

  <script>
    let isExperimentRunning = false;
    let dropAnimation;
    let colorChangeTimeout;
    
    function startExperiment() {
      if (isExperimentRunning) return;
      isExperimentRunning = true;
      
      const drop = document.getElementById('drop');
      const solution = document.getElementById('solution');
      const buretteSolution = document.getElementById('burette-solution');
      
      // Start burette solution animation (decrease by 20 mL)
      buretteSolution.style.animationPlayState = 'running';
      
      // Start dropping animation (5 drops)
      drop.style.animationPlayState = 'running';
      
      // Change color after 5 seconds
      colorChangeTimeout = setTimeout(() => {
        solution.style.animationPlayState = 'running';
      }, 5000);
    }
    
    // Add this function to your Streamlit component
    window.addEventListener('message', function(event) {
      if (event.data.type === 'start_experiment') {
        startExperiment();
      }
    });
  </script>
</div>
</body>
</html>
"""

# Display the HTML component
html_container = components.html(html_code, height=600)

# Start experiment button
if st.button("Start Experiment"):
    # Send message to start animation
    st.write("Starting titration...")
    html_container.element.contentWindow.postMessage({'type': 'start_experiment'}, '*')
    
    # Progress indication
    progress_bar = st.progress(0)
    status = st.empty()
    
    # Simulate titration progress
    for i in range(101):
        progress_bar.progress(i)
        if i < 50:
            status.text(f"Adding NaOH... ({i}%)")
        elif i < 80:
            status.text("Color changing to pink!")
        else:
            status.text("Titration complete!")
        time.sleep(0.2)

    # Generate and display pH curve
    volume = np.linspace(0, 50, 100)
    initial_ph = 1
    equivalence_point = 25
    
    def calculate_ph(v):
        if v < equivalence_point:
            return -np.log10(abs(0.1 - (0.1 * v/equivalence_point)))
        elif abs(v - equivalence_point) < 0.1:
            return 7
        else:
            return 14 + np.log10(abs((0.1 * (v-equivalence_point))/v))
    
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
3. As a few drops of NaOH are added:
   - It neutralizes the HCl
   - The pH gradually increases
   - The phenolphthalein indicator changes color to pink
4. At the endpoint:
   - The solution turns pink
   - The pH curve shows a sharp increase
   - All acid has been neutralized
""")
