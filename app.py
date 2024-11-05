import streamlit as st
import time
import random

def main():
  st.set_page_config(page_title="Elephant Toothpaste Reaction", layout="wide")

  # CSS for styling and animations
  st.markdown("""
    <style>
      @keyframes rise {
        0% { height: 50%; }
        100% { height: 200%; }
      }
      @keyframes pour {
        0% { transform: rotate(0deg) translateX(-50px); }  /* Move beaker to the right */
        100% { transform: rotate(135deg); }
      }
      .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        font-size: 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      .title {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        animation: gradient 3s ease infinite;
      }
      @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
      }
    </style>
  """, unsafe_allow_html=True)

  # Animated title
  st.markdown('<p class="title">Elephant Toothpaste Reaction</p>', unsafe_allow_html=True)

  # Initialize session state for reaction
  if 'reaction_state' not in st.session_state:
    st.session_state.reaction_state = 'ready'
    st.session_state.foam_height = 50

  # Functions for beaker and cylinder visuals
  def draw_beaker(label, color, pouring=False):
    rotation = "135deg" if pouring else "0deg"
    translation = "translateX(-50px)" if pouring else ""  # Move beaker to the right during pour
    return f"""
      <div style="position: relative; width: 100px; height: 150px; {translation}">
        <div style="
          position: absolute;
          width: 80px;
          height: 120px;
          border: 3px solid #333;
          border-top: none;
          background: transparent;
          transform: rotate({rotation});
          transform-origin: bottom right;
          transition: transform 1s;">
          <div style="
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            background-color: {color};
            transition: height 2s;">
          </div>
        </div>
        <div style="position: absolute; bottom: -25px; width: 100%; text-align: center;">
          {label}
        </div>
      </div>
    """

  def draw_cylinder(foam_height):
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    foam_color = random.choice(colors)
    return f"""
      <div style="position: relative; width: 150px; height: 200px; margin: auto;">
        <div style="
          position: absolute;
          width: 120px;
          height: 180px;
          border: 3px solid #333;
          border-top: none;
          background: transparent;">
          <div style="
            position: absolute;
            bottom: 0;
            width: 100%;
            height: {foam_height}%;
            background: linear-gradient(45deg, {foam_color}, white);
            transition: height 2s;">
          </div>
        </div>
