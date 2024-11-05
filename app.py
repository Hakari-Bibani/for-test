import streamlit as st
import time
import streamlit.components.v1 as components

st.title("Test the pH of different solutions using litmus paper!")

# Custom CSS for the animation
st.markdown("""
<style>
    .container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
        position: relative;
        height: 400px;
    }
    .beaker {
        width: 100px;
        height: 150px;
        border: 3px solid #333;
        border-radius: 0 0 20px 20px;
        position: relative;
        margin-top: 100px;
    }
    .solution {
        width: 100%;
        height: 80%;
        position: absolute;
        bottom: 0;
        border-radius: 0 0 17px 17px;
        animation: bubble 2s infinite;
    }
    .litmus {
        width: 15px;
        height: 80px;
        background-color: #f9f9c5;
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        transition: all 0.5s;
    }
    @keyframes bubble {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    .animate-test {
        animation: dipTest 6s forwards;
    }
    @keyframes dipTest {
        0% { transform: translateX(-50%) translateY(0); }
        20% { transform: translateX(-50%) translateY(150px); }
        80% { transform: translateX(-50%) translateY(150px); }
        100% { transform: translateX(-50%) translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# HTML for the beakers and litmus papers
beakers_html = """
<div class="container">
    <div class="beaker" id="acid">
        <div class="solution" style="background-color: #e0e0e0;"></div>
        <div class="litmus" id="litmus1"></div>
    </div>
    <div class="beaker" id="base">
        <div class="solution" style="background-color: #e0e0e0;"></div>
        <div class="litmus" id="litmus2"></div>
    </div>
    <div class="beaker" id="neutral">
        <div class="solution" style="background-color: #e0f7ff;"></div>
        <div class="litmus" id="litmus3"></div>
    </div>
</div>
"""

# JavaScript for handling the animation
js_code = """
<script>
function startTest() {
    const litmus1 = document.getElementById('litmus1');
    const litmus2 = document.getElementById('litmus2');
    const litmus3 = document.getElementById('litmus3');
    
    // Reset colors
    litmus1.style.backgroundColor = '#f9f9c5';
    litmus2.style.backgroundColor = '#f9f9c5';
    litmus3.style.backgroundColor = '#f9f9c5';
    
    // Add animation class
    litmus1.classList.add('animate-test');
    litmus2.classList.add('animate-test');
    litmus3.classList.add('animate-test');
    
    // Change colors after delay
    setTimeout(() => {
        litmus1.style.backgroundColor = '#ff6b6b';  // Red for acid
        litmus2.style.backgroundColor = '#4dabf7';  // Blue for base
        litmus3.style.backgroundColor = '#8ce99a';  // Light green for neutral
    }, 1500);
    
    // Remove animation class after completion
    setTimeout(() => {
        litmus1.classList.remove('animate-test');
        litmus2.classList.remove('animate-test');
        litmus3.classList.remove('animate-test');
    }, 6000);
}
</script>
"""

# Combine HTML and JavaScript
components.html(f"{beakers_html}{js_code}", height=450)

# Create the start button
if st.button("Start Test", key="start_test"):
    js_code = f"<script>startTest()</script>"
    components.html(js_code, height=0)
