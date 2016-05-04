# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np

from mousestyles.density_estimation import (distances,
                                            distances_bymouse,
                                            distances_bystrain)


def test_pos_day():
    assert np.all(distances(1, 2, 3) >= 0)


def test_pos_bymouse():
    assert np.all(distances_bymouse(1, 2, 3) >= 0)


def test_pos_bystrain():
    assert np.all(distances_bystrain(1, 2, 3) >= 0)


def test_array_day():
    assert type(distances(1, 2, 3)) is np.ndarray


def test_array_bymouse():
    assert type(distances_bymouse(1, 2)) is np.ndarray


def test_array_bystrain():
    assert type(distances_bystrain(1)) is np.ndarray


def max_speed():
    # Max speed of a mouse should be less than 40 km/h
    assert max(distances(0, 0, 0, step=50) * 3.6 / 100) < 40


def max_speed_bymouse():
    # Max speed of a mouse should be less than 40 km/h
    assert max(distances_bymouse(0, 0, step=50) * 3.6 / 100) < 40


def max_speed_bystrain():
    # Max speed of a mouse should be less than 40 km/h
    assert max(distances_bystrain(0, step=50) * 3.6 / 100) < 40
