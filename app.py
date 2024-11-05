import streamlit as st
import streamlit.components.v1 as components

# Define title
st.title("Elephant Toothpaste Reaction")

# Display initial setup with beaker and cylinder
st.write("**Reaction Setup:**")
st.image("beaker_h2o2.png", caption="Beaker with H₂O₂", width=200)  # Placeholder for beaker image
st.image("cylinder_ki.png", caption="Cylinder with KI", width=200)   # Placeholder for cylinder image

# Add the start button for the experiment
start_experiment = st.button("Start Experiment")

# JavaScript for the animation (simple placeholder animation using HTML/JS)
animation_script = """
<script>
function startAnimation() {
    let beaker = document.getElementById("beaker");
    let cylinder = document.getElementById("cylinder");
    let foam = document.getElementById("foam");
    
    // Pouring animation
    beaker.style.transform = "rotate(45deg)";
    setTimeout(() => {
        beaker.style.opacity = "0"; // Hide beaker after pouring
        
        // Foam eruption animation
        foam.style.height = "200px";
        foam.style.transition = "height 1s";
        
        // Reveal chemical equation and note
        document.getElementById("equation").style.display = "block";
        document.getElementById("note").style.display = "block";
    }, 1000);
}

// Run the animation on button click
if (window.startExperiment) {
    startAnimation();
}
</script>
"""

# Add CSS for foam and beaker positioning
css_style = """
<style>
#beaker, #cylinder {
    display: inline-block;
    margin-right: 20px;
}
#foam {
    width: 80px;
    height: 0px;
    background-color: lightblue;
    border-radius: 10px;
    margin-top: -40px;
    transition: height 0.5s ease;
}
#equation, #note {
    display: none;
}
</style>
"""

# Display the experiment setup as HTML with inline CSS for styling
html_content = f"""
<div id="beaker" style="display: inline-block;">
    <img src="https://via.placeholder.com/80x120.png?text=H2O2" alt="Beaker with H2O2">
</div>
<div id="cylinder" style="display: inline-block;">
    <img src="https://via.placeholder.com/80x120.png?text=KI" alt="Cylinder with KI">
</div>
<div id="foam"></div>
<div id="equation"><strong>Chemical Equation:</strong> 2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</div>
<div id="note"><em>Note:</em> You can add food coloring and liquid soap to make the reaction even more dramatic!</div>
"""

# Run the animation script if the button is clicked
if start_experiment:
    components.html(css_style + html_content + animation_script, height=400, width=500)
