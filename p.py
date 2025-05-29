import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Stel de spines eenmalig in
ax2.spines['right'].set_position(('outward', 50))

def animate(i):
    data = pd.read_csv('live.csv')
    x = data['0']
    y1 = data['1']
    y2 = data['2']

    ax1.cla()
    ax2.cla()

    # Stel de spines opnieuw in
    ax2.spines['right'].set_position(('outward', 50))

    # Plot de lijnen
    ax1.plot(x, y1, label='Channel 1', color='red')
    ax1.set_ylabel("data1", color='red')
    ax1.tick_params(axis='y', labelcolor='red')

    ax2.plot(x, y2, label='Channel 2', color='blue')
    ax2.set_ylabel("data2", color='blue', rotation=-90)
    ax2.tick_params(axis='y', labelcolor='blue')

    # Handmatige positionering van het label
    ax2.yaxis.set_label_coords(1.15, 0.5)  # Verplaatst label rechts van de grafiek

    ax1.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(fig, animate, interval=100, cache_frame_data=False)
plt.show()
