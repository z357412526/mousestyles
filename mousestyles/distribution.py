from __future__ import print_function,  absolute_import,  division
import numpy as np


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
    return((a - 1) * x ** (-a))


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
    return(l * np.exp(-l * (x - 1)))
