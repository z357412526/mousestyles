from __future__ import print_function, absolute_import, division
import numpy as np 


def get_dist_speed(movement, start, end):
    r"""
    Return a tuple containing distance covered in a path and
    average speed within a path.

    Parameters
    ----------
    movement : pandas.DataFrame
        CT, CX, CY coordinates and homebase status for the unique
        combination of strain, mouse, and day

    start : int
        positive integer indicating the starting index of a path

    end : int
        positive integer indicating the end index of a path

    Returns
    -------
    dist : distance travelled along a path

    speed : average speed along a path

    Examples
    --------
    >>> movement = data.load_movement(1, 2, 1)
    >>> dist, speed = get_dist_speed(movement, 0, 500)
    (554.5573324808769, 0.080910098911799441)
    """

    # Check whether inputs are valid.
    if (start < 0) or (end < 0):
        raise ValueError("Start and end indices must be positive")
    if (type(start) != int) or (type(end) != int):
        raise TypeError("Start and end indices must be integers")
    if start > end:
        raise ValueError("Start index must be smaller than end index")
    if end - start > len(movement) - 1:
        raise ValueError("Number of observations must be less than \
        or equal to total observations")

    if start == end:
        return(0, 0)

    x = movement['x'][start:(end+1)].ravel()
    y = movement['y'][start:(end+1)].ravel()
    t = movement['t']
    time = t[end] - t[start]

    dist = sum(np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2))
    speed = dist / time

    return(dist, speed)
