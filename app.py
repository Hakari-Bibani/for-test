import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Draw a conical flask and burette outline
burette, = ax.plot([], [], 'k-', lw=2)
flask, = ax.plot([], [], 'b-', lw=2)

# Data for flask and burette
x_flask = [2, 4, 3]  # Example outline of the flask
y_flask = [1, 1, 4]  # Example outline of the flask
x_burette = [7, 7]   # Example outline of the burette
y_burette = [5, 10]  # Example outline of the burette

# Animation function
def animate(i):
    flask.set_data(x_flask, y_flask)
    burette.set_data(x_burette, y_burette)
    
    # Update to show the liquid level change in the burette
    ax.plot([7, 7], [10 - i*0.1, 10], 'c-', lw=4)  # Decrease liquid level

# Create animation
ani = FuncAnimation(fig, animate, frames=50, interval=200)

plt.show()
