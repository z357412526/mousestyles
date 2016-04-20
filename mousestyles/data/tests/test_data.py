"""Standard test data.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pytest

import mousestyles.data as data
import numpy as np


def test_all_features_loader():
    # Checking load_all_features returns a data frame of the correct dimension
    all_features = data.load_all_features()
    assert all_features.shape == (21131, 13)


def test_intervals_loader():
    # Checking load_intervals returns a data frame of the correct dimension
    AS = data.load_intervals('AS')
    assert AS.shape == (1343, 5)


def test_movement_loader():
    # Checking load_movement returns a data frame of the correct dimension
    movement = data.load_movement(0, 0, 0)
    assert movement.shape == (39181, 4)


def test_feature_load_input():
    # checking functions raise the correct errors
    with pytest.raises(ValueError) as excinfo:
        data.load_intervals('A')
    msg = 'Input value must be one of {"AS", "F", "IS", "M_AS", "M_IS", "W"}'
    assert excinfo.value.args[0] == msg

    with pytest.raises(ValueError) as excinfo:
        data.load_movement(-1, 0, 0)
    assert excinfo.value.args[0] == "Input values need to be nonnegative"

    with pytest.raises(TypeError) as excinfo:
        data.load_movement(0.0, 0, 0)
    assert excinfo.value.args[0] == "Input values need to be integer"

    with pytest.raises(ValueError) as excinfo:
        data.load_movement(1000, 1000, 1000)
    expected = "No data exists for strain 1000, mouse 1000, day 1000"
    assert excinfo.value.args[0] == expected


def test_load_movement_and_intervals():
    m1 = data.load_movement(1, 1, 1)
    m2 = data.load_movement_and_intervals(
        1, 1, 1, [])  # don't add any features
    assert np.all(m1 == m2)
    m3 = data.load_movement_and_intervals(1, 1, 1, ['AS'])
    assert m3.shape[1] == m1.shape[1] + 1  # adds one column
    assert m3.shape[0] == m1.shape[0]  # same number of rows
