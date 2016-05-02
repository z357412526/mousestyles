from __future__ import print_function,  absolute_import,  division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import statistics as stat
import pandas as pd
from mousestyles import data

def plot_powerlaw(estimation):
    """
    Return the histogram of all estimators of power law to check the distribution.

    Parameters
    ----------
    estimation: dataframe
        dataframe of strain, mouse, day and the estimator

    Returns
    -------
    plot : histogram
        The histogram of all estimators of power law.
    """
    plt.hist(list(estimation.ix[estimation["strain"]==0, 3]))
    plt.hist(list(estimation.ix[estimation["strain"]==1, 3]))
    plt.hist(list(estimation.ix[estimation["strain"]==2, 3]))
    plt.title("Histogram: Power Law parameters distribution by strain")


def plot_expoential(estimation):
    """
    Return the histogram of all estimators of exponential to check the distribution.

    Parameters
    ----------
    estimation: dataframe
        dataframe of strain, mouse, day and the estimator    

    Returns
    -------
    plot : histogram
        The histogram of all estimators of exponential.
    """
    plt.hist(list(estimation.ix[estimation["strain"]==0, 4]))
    plt.hist(list(estimation.ix[estimation["strain"]==1, 4]))
    plt.hist(list(estimation.ix[estimation["strain"]==2, 4]))
    plt.title("Histogram: Exponential parameters distribution by strain")


def powerlaw_pdf(x, a):
    """
    The probability density function of truncated power law.

    Parameters
    ----------
    x : int 
        x in formula p(x)=(alpha-1)*x^(-alpha).
    a : int>1
        alpha in formula p(x)=(alpha-1)*x^(-alpha).

    Returns
    -------
    probability density : a float number
        The probability density of power law at x.

    Examples
    --------
    >>> powerlaw_pdf (2, 2)
    0.25
    """
    return((a-1)*x**(-a))


def exp_pdf(x, l):
    """
    The probability density function of truncated exponential.

    Parameters
    ----------
    x : int 
        x in formula p(x)=lambda*exp(-lambda*x).
    l : int
        lambda in formula p(x)=lambda*exp(-lambda*x).

    Returns
    -------
    probability density : a float number
        The probability density of power law at x.

    Examples
    --------
    >>> exp_pdf(1, 1)
    0.36787944117144233
    """
    return(l*np.exp(-l*(x-1)))


def plot_fitted(strain,  mouse,  day):
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
    day	:  int
        the day number

    Returns
    -------
    plot : 1 histogram + 2 fitted curve
	"""
    import matplotlib.pyplot as plt
    fig,  ax = plt.subplots(1,  1)
    x = np.arange(1, 2.7, 0.01)
    alpha = fit_powerLaw(strain,  mouse,  day)
    lamb = fit_exponential(strain,  mouse,  day)
    Cut_dist = getdistance(strain,  mouse,  day)
    ax.plot(x,  powerlaw_pdf(x, alpha), 'r-',  lw=2,  alpha=2,  label='powerlaw pdf')
    ax.plot(x,  exp_pdf(x, lamb), 'y-',  lw=2,  alpha=2,  label='expon pdf')
    weights = np.ones_like(Cut_dist)/len(Cut_dist)*(alpha-1)
    ax.hist(Cut_dist, weights=weights)