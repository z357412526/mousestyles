"""Standard test data.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from numpy.testing import assert_equal

import mousestyles.data as data


def test_all_features_loader():
    all_features = data.load_all_features()
    assert_equal(all_features.shape, (21131, 13))


def test_intervals_loader():
    AS = data.load_intervals('AS')
    assert_equal(AS.shape, (1343, 5))


def test_movement_loader():
    movement = data.load_movement(0, 0, 0)
    assert_equal(movement.shape, (39181, 4))
