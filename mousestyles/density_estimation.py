# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from mousestyles.data import load_movement
import numpy as np
import pandas as pd


def extract_distances(strain, mouse, day, step=1e2):
    """
    Return a numpy array object of project movement data
    for the specified combination of strain, mouse and day.

    The array contains the distance between two different times
    taken with the same time interval

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
    >>> extract_distances(0,0,0, step=1e2)[0]
    0
    >>> np.int(np.sum(extract_distances(1,2,3, step=1e2)))
    60789
    """
    movement = load_movement(strain, mouse, day)
    # Compute distance between samples
    dist = np.empty((movement.shape[0]-1, 2))
    x = np.array(movement["x"])
    y = np.array(movement["y"])
    # dist[:, 0] contains the distances between two
    # consecutive points 
    dist[:, 0] = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2)
    # dist[:, 1] contains the recorded times for which
    # the distances have been computed
    dist[:, 1] = np.array(movement['t'])[1:]
    dist[:, 1] = dist[:, 1] - dist[0, 1]
    tf = dist[dist.shape[0] - 1, 1]
    # Aggregate distances according to step
    aggregate = np.zeros(int(tf/step))
    j = 0
    for i in range(len(aggregate)):
        while dist[j, 1] < i*step:
            aggregate[i] = aggregate[i] + dist[j, 0]
            j = j+1
    return(aggregate)


def extract_distances_bymouse(strain, mouse, step=1e2, verbose=False):
    """
    Aggregates extract_distances for all days.

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
    >>> extract_distances_bymouse(0, 0)[0]
    0
    >>> np.int(sum(extract_distances_bymouse(0, 0)))
    493313
    """
    day = 0
    res = []
    while True:
        try:
            res.append(list(extract_distances(strain, mouse, day, step=step)))
            day = day + 1
            if verbose:
                print('day %s done.' % day)
        except IOError:
            break
    res = pd.DataFrame(res)
    return(np.array(res.sum(axis=0)))


def extract_distances_bystrain(strain, step=1e2, verbose=False):
    """
    Aggregates extract_distances_bymouse for all mice in a strain.

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
    >>> extract_distances_bystrain(0)[0]
    0
    >>> np.int(np.sum(extract_distances_bystrain(0)))
    2088230
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
    return(np.array(res.sum(axis=0)))
