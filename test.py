import matplotlib.pyplot as plt

def on_key(event):
    if event.key == 'q':  # Close the window when 'q' is pressed
        plt.close(event.canvas.figure)

# Create a plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Connect the key press event to the on_key function
fig.canvas.mpl_connect('key_press_event', on_key)

# Display the plot
plt.show()