import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

fig, ax1 = plt.subplots()

# Maak een tweede en derde as
ax2 = ax1.twinx()
ax3 = ax1.twinx()  # Tweede twinx voor de derde as

# Handmatig verplaats de derde as naar rechts
ax3.set_position(("axes", 1.2))  # Offset naar rechts
ax3.yaxis.set_label_position("right")
ax3.yaxis.tick_right()

# Animatiefunctie
def animate(i):
    data = pd.read_csv('live.csv')
    x = data['0']
    y1 = data['1']
    y2 = data['2']
    y3 = data['3']  # Gegevens voor derde as

    # Wis alleen de lijnen in plaats van de volledige assen
    ax1.lines.clear()
    ax2.lines.clear()
    ax3.lines.clear()

    # Plot de gegevens
    ax1.plot(x, y1, label='Channel 1', color='red')
    ax1.set_ylabel("Data 1", color='red')
    ax1.tick_params(axis='y', labelcolor='red')

    ax2.plot(x, y2, label='Channel 2', color='blue')
    ax2.set_ylabel("Data 2", color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    ax3.plot(x, y3, label='Channel 3', color='green')
    ax3.set_ylabel("Data 3", color='green')
    ax3.tick_params(axis='y', labelcolor='green')

    # Positioneer de labels handmatig
    ax2.yaxis.set_label_coords(1.05, 0.5)  # Verplaats naar de rechterkant
    ax3.yaxis.set_label_coords(1.25, 0.5)  # Verplaats verder naar rechts

    # Optionele legenda
    ax1.legend(loc='upper left')
    plt.tight_layout()

# Start animatie
ani = FuncAnimation(fig, animate, interval=100, cache_frame_data=False)
plt.show()
