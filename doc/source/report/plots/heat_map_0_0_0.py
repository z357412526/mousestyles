import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

from mousestyles.data.utils import day_to_mouse_average, mouse_to_strain_average, total_time_rectangle_bins, pull_locom_tseries_subset, split_data_in_half_randomly

# Make position density first mouse first day
from mousestyles.data import load_movement,load_start_time_end_time
from mousestyles.path_index import path_index
# Make position density first mouse first day
# from mousestyles.data import load_movement
M = load_movement(0, 0, 0)
CT = M['t']
CX = M['x']
CY = M['y']

# mask for HB Move Events
CT_NHB = M['isHB']
CT_HB = ~ CT_NHB

start_time, stop_time = load_start_time_end_time(0,0,0)

# Cage boundaries
YLower = 1.0; YUpper = 43.0; XUpper = 3.75; XLower = -16.25
xbins = 12; ybins = 24
M = np.vstack([CT, CX, CY])
pos_subset = pull_locom_tseries_subset(M, start_time, stop_time)
bin_times = total_time_rectangle_bins(pos_subset, xlims=(XLower, XUpper), ylims=(YLower, YUpper), xbins=xbins, ybins=ybins)
position_pdf = bin_times / bin_times.sum()

plt.matshow(position_pdf)
plt.title('Cage PDF: 1st Strain, 1st Mouse, 1st Day (12 x 24)')
plt.xlabel('Cage X discretized coordinate')
plt.ylabel('Cage Y discretized coordinate')
plt.show()