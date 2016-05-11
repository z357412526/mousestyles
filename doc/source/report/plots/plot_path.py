import numpy as np
import matplotlib.pyplot as plt

from mousestyles.data import load_movement
from mousestyles.path_diversity import path_index

movement = load_movement(0, 0, 0)
paths = path_index(movement, 1, 1)

xlim = [-16.25, 3.75]
ylim = [1.0, 43.0]

for sep in paths:
    path = movement[sep[0]:sep[1] + 1]
    plt.plot(path['x'], path['y'], 'b',
             linewidth=1, alpha=.1)
    plt.xlabel('x-coordinate')
    plt.xlim(xlim[0], xlim[1])
    plt.ylabel('y-coordinate')
    plt.ylim(ylim[0], ylim[1])
    plt.title("Example of path plot")

plt.show()
