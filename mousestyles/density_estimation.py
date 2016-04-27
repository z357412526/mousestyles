# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
import pandas as pd

from mousestyles.data import load_movement


def extract_distances(strain, mouse, day, step=1e2):
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

    Returns
    -------
    movement : numpy array

    Examples
    --------
    >>> dist = extract_distances(0, 0, 0, step=1e2)
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


def extract_distances_bymouse(strain, mouse, step=1e2, verbose=False):
    """
    Aggregates extract_distances for all days of recorded data for
    one particular mouse. Then returns the mean of the aggregated data.

    More specifically:

    - let d^1,...,d^D be the sequence of distances for one particular
    mouse for days 1 to D.
    - let d^mouse the empty sequence of length the maximal length of
    d^1,...,d^D, defined as follow:
    for each index i in d^mouse, d^mouse[i] is equal to the mean
    over j of the existing d^j[i].
    - The function returns the sequence d^mouse.

    Parameters
    ----------
    strain: int
        nonnegative integer indicating the strain number
    mouse: int
        nonnegative integer indicating the mouse number
    step: float
        positive float defining the time between two observations

    Returns
    -------
    movement : numpy array

    Examples
    --------
    >>> dist = extract_distances_bymouse(0, 0, step=1e2)
    """
    day = 0
    res = []
    while True:
        try:
            res.append(list(extract_distances(strain, mouse, day, step=step)))
            day = day + 1
            if verbose:
                print('day %s done.' % day)
        except ValueError:
            break
    res = pd.DataFrame(res)
    return(np.array(res.mean(axis=0)))


def extract_distances_bystrain(strain, step=1e2, verbose=False):
    """
    Aggregates extract_distances_bymouse for all mice in one given
    strain.

    More specifically:

    - let d^1,...,d^M be the sequence of distances for one particular
    strain for mouses 1 to M.
    - let d^strain the empty sequence of length the maximal length of
    d^1,...,d^M, defined as follow:
    for each index i in d^mouse, d^strain[i] is equal to the mean
    over j of the existing d^j[i].
    - The function returns the sequence d^strain.

    Parameters
    ----------
    strain: int
        nonnegative integer indicating the strain number
    step: float
        positive float defining the time between two observations

    Returns
    -------
    movement : numpy array

    Examples
    --------
    >>> dist = extract_distances_bystrain(0, step=1e2)
    """
    mouse = 0
    res = []
    e = np.array([0])
    while e.size > 0:
        e = extract_distances_bymouse(strain, mouse, step=step)
        res.append(list(e))
        mouse = mouse + 1
        if verbose:
            print('mouse %s done.' % mouse)
    res = pd.DataFrame(res)
    return(np.array(res.mean(axis=0)))
