"""Standard test data.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from numpy.testing import assert_equal, assert_raises

import mousestyles.data as data


def test_all_features_loader():
    # Checking load_all_features returns a data frame of the correct dimension
    all_features = data.load_all_features()
    assert_equal(all_features.shape, (21131, 13))


def test_intervals_loader():
    # Checking load_intervals returns a data frame of the correct dimension
    AS = data.load_intervals('AS')
    assert_equal(AS.shape, (1343, 5))


def test_movement_loader():
    # Checking load_movement returns a data frame of the correct dimension
    movement = data.load_movement(0, 0, 0)
    assert_equal(movement.shape, (39181, 4))


def test_feature_load_input():
    # checking functions raise the correct errors
    assert_raises(ValueError, load_intervals, "A")
    assert_raises(TypeError, load_movement, 0.0, 0, 0)
    assert_raises(ValueError, load_movement, -1, 0, 0)
