# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np

from mousestyles.density_estimation import (extract_distances,
                                            extract_distances_bymouse,
                                            extract_distances_bystrain)


def test_pos_day():
    assert np.all(extract_distances(1, 2, 3) >= 0)


def test_pos_bymouse():
    assert np.all(extract_distances_bymouse(1, 2, 3) >= 0)


def test_pos_bystrain():
    assert np.all(extract_distances_bystrain(1, 2, 3) >= 0)


def test_array_day():
    assert type(extract_distances(1, 2, 3)) is np.ndarray


def test_array_bymouse():
    assert type(extract_distances_bymouse(1, 2)) is np.ndarray


def test_array_bystrain():
    assert type(extract_distances_bystrain(1)) is np.ndarray
