from mousestyles.est_power_param import fit_dist_all
from mousestyles.visualization.distribution_plot import plot_exponential

estimation = fit_dist_all()
plot_exponential(estimation)
