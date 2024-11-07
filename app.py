import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

def create_burette_flask_ascii(drops, pink_level=0):
    # Create ASCII art for burette and flask
    burette = [
        "  ┌─────────┐  ",
        "  │         │  ",
        "  │  NaOH   │  ",
        "  │         │  ",
        "  └────┬────┘  ",
        "       │       ",
        "       │       "
    ]
    
    # Add drops
    if drops > 0:
        burette.append("       💧      ")
    else:
        burette.append("             ")
        
    flask = [
        "       │       ",
        "    ┌──┴──┐    ",
        "   /  HCl  \\   ",
        "  /         \\  ",
        " /           \\ ",
        "└─────────────┘"
    ]
    
    # Combine burette and flask
    return "\n".join(burette + flask)

def main():
    st.set_page_config(page_title="Acid-Base Titration", layout="wide")
    
    # Title with custom styling
    st.markdown("""
        <h1 style='text-align: center; color: #2E86C1;'>
            🧪 Acid-Base Titration Simulation 🧪
        </h1>
    """, unsafe_allow_html=True)
    
    # Experiment setup
    st.markdown("### Initial Setup")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📋 Reagents:")
        st.write("• Burette: 0.1M NaOH")
        st.write("• Flask: 25mL of 0.1M HCl")
    
    with col2:
        st.info("🔍 Indicator:")
        st.write("• Phenolphthalein")
        st.write("• Color change: Colorless → Pink")
    
    # Create containers for animation and plot
    animation_container = st.empty()
    progress_container = st.empty()
    result_container = st.empty()
    plot_container = st.empty()
    
    # Add start button
    if st.button("Start Titration"):
        drops = 0
        total_drops = 10
        
        # Initialize progress bar
        progress = progress_container.progress(0)
        
        for i in range(total_drops + 1):
            # Update progress
            progress.progress(i/total_drops)
            
            # Show burette and flask ASCII art
            animation_container.code(create_burette_flask_ascii(1 if i < total_drops else 0))
            
            # Update drop count
            drops = i
            
            # Show current status
            if i < total_drops:
                result_container.info(f"Adding drop {i+1} of {total_drops}...")
            time.sleep(0.5)
        
        # Show completion message
        result_container.success("🎉 Endpoint reached! Solution turned pink!")
        
        # Create and display titration curve
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Generate data for the curve
        volume = np.linspace(0, 50, 200)
        ph = np.zeros_like(volume)
        
        # Calculate pH values
        for i, v in enumerate(volume):
            if v < 25:
                # Before endpoint
                ph[i] = -np.log10((0.1 * (25 - v)) / (25 + v))
            elif v == 25:
                # At endpoint
                ph[i] = 7
            else:
                # After endpoint
                ph[i] = 14 + np.log10((0.1 * (v - 25)) / (25 + v))
        
        # Plot the curve
        ax.plot(volume, ph, 'b-', label='Titration Curve')
        ax.axvline(x=25, color='r', linestyle='--', label='Endpoint')
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Volume of NaOH added (mL)')
        ax.set_ylabel('pH')
        ax.set_title('Titration Curve: HCl vs NaOH')
        ax.legend()
        
        # Display the plot
        plot_container.pyplot(fig)
        
        # Add explanation
        st.markdown("""
        ### 📊 Explanation:
        
        1. **Initial Stage** (pH < 7):
           - Solution is acidic due to HCl
        
        2. **Endpoint** (pH = 7):
           - Reached when moles of acid = moles of base
           - Solution turns pink
        
        3. **After Endpoint** (pH > 7):
           - Solution becomes increasingly basic
        """)

if __name__ == "__main__":
    main()
