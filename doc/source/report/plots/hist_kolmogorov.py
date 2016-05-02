import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from mousestyles.distributions.kolmogorov_test import get_travel_distances
from mousestyles.distributions.kolmogorov_test import perform_kstest


def plot_histogram(strain=0, mouse=0, day=0, distribution=stats.pareto,
                   n_hist_bins=50, loc_legend="best"):
    """ Plot the histogram of distances travelled by a mouse in a day within 20
    milliseconds.
    We then fit a distribution as specified by the argument distribution,
    using Maximum Likelihood, and plot the histgoram of that fitted
    distribution.
    Finally, we fit a distribution by minimizing CDF distance, and plot the
    histogram of that fitted distribution.

    In addition to the histograms (PDF), the CDF are also provided.
    Parameters:
    -----------
    strain: int
        Denote the strain of mouse to plot
    mouse: int
        Denote the the mouse id (what twin) within the strain
    day: int
        Denote the day to plot
    distribution: scipy.stats.rv_continuous object
        {stats.pareto, stats.expon, stats.gamma}
        A distribution to fit the data to. Currently supporting three
        distributions.
    n_hist_bins: int
        Number of bins for plotting histogram
    loc_legend: string, int
        {0, 1, 2, ..., 10} or {"best", "upper right", "upper left", ...}
        Location for plotting legend as in plt.legend function
    """
    dist_name = distribution.__class__.__name__.split("_")[0]
    distances = get_travel_distances(strain, mouse, day)
    mle_params = distribution.fit(distances)
    opt_params = perform_kstest(distances, distribution, verbose=False)
    mle_data = distribution(*mle_params).rvs(len(distances))
    opt_data = distribution(*opt_params).rvs(len(distances))

    bins = np.linspace(min(distances), max(distances), n_hist_bins)
    # Plot The Empirical PDF and CDF
    counts, b, _ = plt.hist(distances, bins=bins, alpha=.4, color="green",
                            histtype="step")
    scale = np.max(counts)
    plt.plot(b, np.concatenate([counts.cumsum() / np.sum(counts) * scale,
             [scale]]), color="green", drawstyle="steps-post", lw=2)
    # Plot the MLE PDF and CDF
    counts, b, _ = plt.hist(mle_data, bins=bins, alpha=.4, color="blue",
                            histtype="step")
    plt.plot(b, np.concatenate([counts.cumsum() / np.sum(counts) * scale,
             [scale]]), color="blue", drawstyle="steps-post", lw=2)
    # Plot the Opt PDF and CDF
    counts, b, _ = plt.hist(opt_data, bins=bins, alpha=.4, color="red",
                            histtype="step")
    plt.plot(b, np.concatenate([counts.cumsum() / np.sum(counts) * scale,
             [scale]]), color="red", drawstyle="steps-post", lw=2)
    plt.legend(["Emp CDF", "MLE CDF", "Opt CDF",
                "Emp PDF", "MLE PDF", "Opt PDF"], loc=loc_legend)
    plt.title("Fitting Distribution {} to Data".format(dist_name))
    plt.xlim(1., 1.6)


plt.figure()
plt.subplot(121)
plot_histogram(strain=0, mouse=0, day=0, distribution=stats.pareto)
plt.subplot(122)
plot_histogram(strain=0, mouse=0, day=0, distribution=stats.gamma)
