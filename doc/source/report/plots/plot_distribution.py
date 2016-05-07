import matplotlib.pyplot as plt
from mousestyles. import data
from mousestypes.est_power_param import fit()

Estimation=fit()

# Plot the histogram of the parameters of powerlaw 
plot_powerlaw(Estimation)

# Plot the histogram of the parameters of exponential
plot_expoential(Estimation)

# Plot the histogram and fitted curve for strain 0, mouse 2, day 5
plot_fitted(0, 2, 5)