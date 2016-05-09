from mousestyles.est_power_param import fit
from mousestyles.visualization.distribution_plot import (plot_powerlaw,
                                             plot_exponential,
                                             plot_fitted)

estimation = fit()

# Plot the histogram of the parameters of powerlaw
plot_powerlaw(estimation)

# Plot the histogram of the parameters of exponential
plot_exponential(estimation)

# Plot the histogram and fitted curve for strain 0, mouse 2, day 5
plot_fitted(0, 2, 5)
