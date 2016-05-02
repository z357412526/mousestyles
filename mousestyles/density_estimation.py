# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np

from mousestyles.data import load_movement


def distances(strain, mouse, day, step=50):
    """
    Return a numpy array object of project movement data
    for the specified combination of strain, mouse and day.

    At regular timesteps, defined by the step parameter,
    compute the euclidian distance between the positions
    of the mouse at two consecutive times.

    More specifically:

    - let delta_t be the step parameter.
    - let t_n be the sequance of non negative numbers such
    that t_0 = 0 and t_(n+1) = t_n + delta_t. The sequence
    is defined for all n such that n>=0 and t_n <= time
    of the experiment
    - let d_n be the sequence of non negative numbers such
    that d_0 = 0 and d_n equals the position of the mouse
    at a particular day at time t_n. d_n is then defined
    on the same set of integers as the sequence t_n.
    - The function returns the sequence d_n.

    Parameters
    ----------
    strain: int
        nonnegative integer indicating the strain number
    mouse: int
        nonnegative integer indicating the mouse number
    day: int
        nonnegative integer indicating the day number
    step: float
        positive float defining the time between two observations
        default corresponds to 1 second

    Returns
    -------
    movement : numpy array

    Examples
    --------
    >>> dist = distances(0, 0, 0, step=1e2)
    """
    movement = load_movement(strain, mouse, day)
    # Compute distance between samples
    dist = np.sqrt(movement["x"].diff()[1:]**2 + movement["y"].diff()[1:]**2)
    time = movement['t'][1:] - movement['t'][0]
    t_final = time[len(time)-1]
    # Aggregate distances according to step
    aggregate = np.zeros(int(t_final/step))
    j = 1
    for i in range(len(aggregate)):
        while time[j] < i*step:
            aggregate[i] = aggregate[i] + dist[j]
            j = j+1
    return(aggregate)


def distances_bymouse(strain, mouse, step=50, verbose=False):
    """
    Aggregates 'distances' for all days of recorded data for
    one particular mouse.

    More specifically:

    - let d^1,...,d^D be the sequence of distances for one particular
    mouse for days 1 to D.
    - The function returns the concatenation of the d^i.

    Parameters
    ----------
    strain: int
        nonnegative integer indicating the strain number
    mouse: int
        nonnegative integer indicating the mouse number
    step: float
        positive float defining the time between two observations
        default corresponds to 1 second

    Returns
    -------
    movement : numpy array

    Examples
    --------
    >>> dist = distances_bymouse(0, 0, step=1e2)
    """
    day = 0
    res = np.array([])
    while True:
        try:
            res = np.append(res, distances(strain, mouse, day,
                                           step=step))
            day += 1
            if verbose:
                print('day %s done.' % day)
        except ValueError:
            break
    return(res)


def distances_bystrain(strain, step=50, verbose=False):
    """
    Aggregates distances_bymouse for all mice in one given
    strain.

    More specifically:

    - let d^1,...,d^M be the sequence of distances for one particular
    strain for mouses 1 to M.
    - The function returns the sequence concatenation of the d^i.

    Parameters
    ----------
    strain: int
        nonnegative integer indicating the strain number
    step: float
        positive float defining the time between two observations
        default corresponds to 1 second

    Returns
    -------
    movement : numpy array

    Examples
    --------
    >>> dist = distances_bystrain(0, step=1e2)
    """
    mouse = 0
    res = np.array([])
    dist = np.array([0])
    while dist.size > 0:
        dist = distances_bymouse(strain, mouse,
                                 step=step)
        res = np.append(res, dist)
        mouse += 1
        if verbose:
            print('mouse %s done.' % mouse)
    return(res)
