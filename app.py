import streamlit as st
import time

def run_experiment():
  """
  Simulates the Baking Soda and Vinegar reaction animation.
  """

  # Animation steps with time delays
  for step in range(1, 4):
    if step == 1:
      # Bend the spoon animation
      st.markdown("""
      <style>
        .beaker-container {
          display: flex;
          justify-content: space-around;
          margin: 20px 0;
          padding: 20px;
          position: relative;
        }

        .beaker {
          width: 120px;
          height: 150px;
          position: relative;
          background: rgba(255,255,255,0.1);
          border: 3px solid #ddd;
          border-top: 15px solid #ddd;
          border-radius: 10px 10px 20px 20px;
          text-align: center;
          padding-top: 10px;
          margin-bottom: 40px;
          overflow: hidden;
          transform: rotateX(-30deg);  # Initial tilt for spoon
        }

        .spoon {
          position: absolute;
          top: -30px;
          left: 50%;
          transform: translateX(-50%);
          width: 80px;
          height: 10px;
          border-radius: 5px;
          background-color: lightgray;
          transform: rotateX(45deg);  # Initial spoon angle
        }

        .powder {
          position: absolute;
          top: -40px;
          left: 50%;
          transform: translateX(-50%);
          width: 20px;
          height: 20px;
          border-radius: 50%;
          background-color: lightgray;
        }

        .beaker-label {
          font-family: 'Rajdhani', sans-serif;
          font-size: 14px;
          text-align: center;
          margin-top: 15px;
          color: #2c3e50;
          max-width: 120px;
          word-wrap: break-word;
          font-weight: 600;
          text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
      </style>

      <div class="beaker-container">
        <div class="beaker">
          <div class="spoon"></div>
          <div class="powder"></div>
        </div>
        <div class="beaker-label">Vinegar (CH₃COOH)</div>
      </div>
      """, unsafe_allow_html=True)
    elif step == 2:
      # Pouring animation (increase spoon angle)
      st.markdown("""
      <style>
        .spoon {
          transform: rotateX(90deg);  # Spoon pouring angle
        }
      </style>
      """, unsafe_allow_html=True)
    elif step == 3:
      # Powder falls, remove spoon
      st.markdown("""
      <style>
        .spoon {
          display: none;
        }
        .powder {
          top: 50px;
        }
      </style>
      """, unsafe_allow_html=True)
    time.sleep(1.5)  # Delay between animation steps

  # Reaction animation (replace with your desired bubbles effect)
  st.markdown("""
  <style>
    .beaker {
      background: rgba(255,255,255,0.3);  # Simulate lighter color for bubbles
    }

    .bubbles {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 80%;
      border-radius: 0 0 17px 17px;
      animation: bubbleRise 2s ease-in-out infinite;
    }

    .bubbles::before,
    .bubbles::after
