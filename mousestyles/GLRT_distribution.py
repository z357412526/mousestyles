from __future__ import print_function, absolute_import, division

import numpy as np
from mousestyles import data


def powerlaw_pdf(x, a):
    """
    The probability density function of truncated power law.

    Parameters
    ----------
    x : int
        x in formula p(x) = (alpha-1)*x^(-alpha).
    a : int>1
        alpha in formula p(x) = (alpha-1)*x^(-alpha).

    Returns
    -------
    probability density : a float number
        The probability density of power law at x.

    Examples
    --------
    >>> powerlaw_pdf (2,2)
    0.25
    """
    return((a - 1) * x**(-a))


def exp_pdf(x, l):
    """
    The probability density function of truncated exponential.

    Parameters
    ----------
    x : int
        x in formula p(x) = lambda*exp(-lambda*x).
    l : int
        lambda in formula p(x) = lambda*exp(-lambda*x).

    Returns
    -------
    probability density : a float number
        The probability density of power law at x.

    Examples
    --------
    >>> exp_pdf(2,2)
    0.2706705664732254
    """
    return(l * np.exp(-l * (x - 1)))


def random_powerlaw(n, a):
    """
    Random generate points of truncated power law.

    Parameters
    ----------
    n : int
        number of points
    a : int>1
        power law parameter alpha

    Returns
    -------
    points : a vector of float number
        n points have the target distribution.

    Examples
    --------
    >>> random_powerlaw(4,2)
    array([  1.18097435,   1.04584078,   1.4650779 ,  36.03967524])
    """
    y = np.random.sample(n)
    return((1 - y)**(-1 / (a - 1)))


def random_exp(n, l):
    """
    Random generate points of truncated exponential.

    Parameters
    ----------
    n : int
        number of points
    l : int
        exponential parameter lambda

    Returns
    -------
    points : a vector of float number
        n points have the target distribution.

    Examples
    --------
    >>> random_exp(4,2)
    array([ 1.07592496,  1.19789646,  1.19759663,  1.03993227])
    """
    y = np.random.exponential(1.0 / l, n)
    return(y + 1)


def hypo_powerLaw_null(strain, mouse, day, law_est=0):
    """
    Return the outcome from GLRT with null hypothesis law distribution.

    Parameters
    ----------
    strain : int
        the strain number of the mouse
    mouse  : int
        the mouse number in its strain
    day       :  int
        the day number
    law_est: double (optional)
        the estimated parameter in law distribution

    Returns
    -------
    p_value:
        the probablity under null reject.

    Examples
    --------
    >>> hypo_law_null (0, 0, 0)
    0.0070000000000000001
    """
    df = data.load_movement(strain, mouse, day)
    xcood = df["x"]
    ycood = df["y"]
    distance_vector = np.sqrt(np.diff(xcood)**2 + np.diff(ycood)**2)
    msk = distance_vector > 1
    cut_dist = distance_vector[msk]
    if law_est == 0:
        law_est = 1 + len(cut_dist) * 1 / \
                          (np.sum(np.log(cut_dist / np.min(cut_dist))))
    n = len(cut_dist)
    log_cut = np.log(cut_dist)
    sum_cut = np.sum(log_cut)
    test_stat = n * (np.log(sum_cut - n) - np.log(sum_cut)) - law_est * sum_cut
    sample_stat = []
    for i in range(1000):
        sample = random_powerlaw(len(cut_dist), law_est)
        sum_sam = np.sum(sample)
        log_sam = np.log(sample)
        sum_log_sam = np.log(np.sum(log_sam))
        tmp = n*(np.log(sum_sam-n)-sum_log_sam) - law_est*np.sum(log_sam)
        sample_stat.append(tmp)
    # critical_value = ss.mstats.mquantiles(sample_stat, prob = 0.05)[0]
    p_value = np.sum(sample_stat > test_stat) / len(sample_stat)
    return (p_value)


def hypo_exp_null(strain, mouse, day, law_est=0, exp_est=0):
    """
    Return the outcome from GLRT with null hypothesis law distribution.

    Parameters
    ----------
    strain : int
        the strain number of the mouse
    mouse  : int
        the mouse number in its strain
    day       :  int
        the day number
    law_est: double (optional)
        the estimated parameter in law distribution
    exp_est: double (optional)
        the estimated parameter in exponential distribution

    Returns
    -------
    p_value:
        the probablity under null reject.

    Examples
    --------
    >>> hypo_exp_null (0, 0, 0)
    1.0
    """
    df = data.load_movement(strain, mouse, day)
    xcood = df["x"]
    ycood = df["y"]
    distance_vector = np.sqrt(np.diff(xcood)**2 + np.diff(ycood)**2)
    msk = distance_vector > 1
    cut_dist = distance_vector[msk]
    if law_est == 0:
        law_est = 1 + len(cut_dist) * 1 / \
                        (np.sum(np.log(cut_dist / np.min(cut_dist))))
    if exp_est == 0:
        exp_est = len(cut_dist) / (np.sum(cut_dist) - len(cut_dist))
    n = len(cut_dist)
    sum_cut = np.sum(cut_dist)
    log_cut = np.log(cut_dist)
    sum_log_cut = np.sum(log_cut)
    test_stat = n * (np.log(sum_cut - n) - np.log(sum_log_cut)) - \
        law_est * sum_log_cut
    sample_stat = []
    for i in range(1000):
        sample = random_exp(len(cut_dist), exp_est)
        sum_sam = np.sum(sample)
        log_sam = np.log(sample)
        sum_log_sam = np.sum(log_sam)
        tmp = n * (np.log(sum_sam - n) - np.log(sum_log_sam)) - \
            law_est * sum_log_sam
        sample_stat.append(tmp)
    # critical_value = ss.mstats.mquantiles(sample_stat, prob = 0.95)[0]
    p_value = np.sum(sample_stat <= test_stat) / len(sample_stat)
    return (p_value)
