import streamlit as st
import time

st.title("Test the pH of different solutions using litmus paper!")

# Custom CSS with simpler animations
st.markdown("""
<style>
.stButton>button {
    width: 200px;
    margin: 0 auto;
    display: block;
}

.experiment-container {
    display: flex;
    justify-content: space-around;
    margin: 20px auto;
    padding: 20px;
}

.beaker {
    text-align: center;
    position: relative;
    width: 150px;
}

.beaker-img {
    width: 100px;
    height: 120px;
    border: 3px solid #333;
    border-radius: 0 0 15px 15px;
    margin: 0 auto;
    position: relative;
    background-color: rgba(200, 200, 200, 0.2);
}

.litmus-paper {
    width: 20px;
    height: 80px;
    margin: 0 auto;
    background-color: #f9f9c5;
    position: relative;
    transition: all 1s ease;
}

.solution {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 75%;
    border-radius: 0 0 12px 12px;
}

.acid .solution {
    background-color: #f0f0f0;
}

.base .solution {
    background-color: #f0f0f0;
}

.neutral .solution {
    background-color: #e6f3ff;
}

.dipped {
    transform: translateY(80px);
}

.acid-result {
    background-color: #ff6666 !important;
}

.base-result {
    background-color: #6666ff !important;
}

.neutral-result {
    background-color: #90EE90 !important;
}
</style>
""", unsafe_allow_html=True)

# HTML Structure
experiment_html = """
<div class="experiment-container">
    <div class="beaker acid">
        <div class="litmus-paper" id="acid-paper"></div>
        <div class="beaker-img">
            <div class="solution"></div>
        </div>
        <p>HCl</p>
    </div>
    
    <div class="beaker base">
        <div class="litmus-paper" id="base-paper"></div>
        <div class="beaker-img">
            <div class="solution"></div>
        </div>
        <p>NaOH</p>
    </div>
    
    <div class="beaker neutral">
        <div class="litmus-paper" id="neutral-paper"></div>
        <div class="beaker-img">
            <div class="solution"></div>
        </div>
        <p>H₂O</p>
    </div>
</div>
"""

# JavaScript for animation
js_code = """
<script>
function animateLitmusTest() {
    const papers = ['acid-paper', 'base-paper', 'neutral-paper'];
    const results = ['acid-result', 'base-result', 'neutral-result'];
    
    // Reset papers
    papers.forEach((paper, index) => {
        const element = document.getElementById(paper);
        element.className = 'litmus-paper';
    });
    
    // Dip papers
    setTimeout(() => {
        papers.forEach(paper => {
            document.getElementById(paper).classList.add('dipped');
        });
    }, 100);
    
    // Change colors
    setTimeout(() => {
        papers.forEach((paper, index) => {
            document.getElementById(paper).classList.add(results[index]);
        });
    }, 2000);
    
    // Return to original position
    setTimeout(() => {
        papers.forEach(paper => {
            document.getElementById(paper).classList.remove('dipped');
        });
    }, 4000);
}
</script>
"""

# Combine HTML and JavaScript
st.components.v1.html(f"{experiment_html}{js_code}", height=400)

# Button to trigger animation
if st.button('Start Test'):
    st.components.v1.html(
        "<script>animateLitmusTest()</script>",
        height=0
    )
