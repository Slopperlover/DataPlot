
from itertools import count
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv 

x_vals = []
y_vals = []

index = iter(range(100))

# with open('C:\school\python\eindopdracht\plot.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     row = next(csv_reader)
#     print(row)

#     for row in csv_reader:
#         x_vals += [float(row['0.035035'])]
#         y_vals += [float(row['0.021'])]

def animate(i):
    # data = pd.read_csv('plot.csv')
    # x = data['ï»¿a']
    # y = data['b']

    x_vals.append(next(index))
    y_vals.append(random.randint(0,10))


    plt.cla()
    plt.plot(x_vals, y_vals, label='Channel 1', marker='.')

    plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.xlabel('Ages')
plt.ylabel('Hapines')
plt.title('My life')
plt.grid(True)

plt.show()
