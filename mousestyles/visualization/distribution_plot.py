import matplotlib.pyplot as plt
import numpy as np

from mousestypes.est_power_param import (fit_powerLaw, fit_exponential,
                                         getdistance, powerlaw_pdf, exp_pdf)


def plot_powerlaw(estimation):
    """
    Return the histogram of all estimators of power law
    to check the distribution.

    Parameters
    ----------
    estimation: dataframe
        dataframe of strain, mouse, day and the estimator

    Returns
    -------
    plot : histogram
        The histogram of all estimators of power law
    """
    plt.hist(list(estimation.ix[estimation["strain"] == 0, 3]))
    plt.hist(list(estimation.ix[estimation["strain"] == 1, 3]))
    plt.hist(list(estimation.ix[estimation["strain"] == 2, 3]))
    plt.title("Histogram: Power Law parameters distribution by strain")


def plot_expoential(estimation):
    """
    Return the histogram of all estimators of exponential
    to check the distribution.

    Parameters
    ----------
    estimation: dataframe
        dataframe of strain, mouse, day and the estimator

    Returns
    -------
    plot : histogram
        The histogram of all estimators of exponential.
    """
    plt.hist(list(estimation.ix[estimation["strain"] == 0, 4]))
    plt.hist(list(estimation.ix[estimation["strain"] == 1, 4]))
    plt.hist(list(estimation.ix[estimation["strain"] == 2, 4]))
    plt.title("Histogram: Exponential parameters distribution by strain")


def plot_fitted(strain, mouse, day):
    """
    Return the plot of one signle mouse day
    -histogram of distance
    -fitted power law
    -fitted exponential

    Parameters
    ----------
    strain : int
        the strain number of the mouse
    mouse  : int
        the mouse number in its strain
    day :  int
        the day number

    Returns
    -------
    plot : 1 histogram + 2 fitted curve
    """
    fig, ax = plt.subplots(1, 1)
    x = np.arange(1, 2.7, 0.01)
    alpha = fit_powerLaw(strain, mouse, day)
    lamb = fit_exponential(strain, mouse, day)
    Cut_dist = getdistance(strain, mouse, day)
    ax.plot(x, powerlaw_pdf(x, alpha), 'r-', lw=2, alpha=2,
            label='powerlaw pdf')
    ax.plot(x, exp_pdf(x, lamb), 'y-', lw=2, alpha=2,
            label='exp pdf')
    weights = np.ones_like(Cut_dist) / len(Cut_dist) * (alpha - 1)
    ax.hist(Cut_dist, weights=weights)
