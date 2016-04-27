# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pytest

from mousestyles.density_estimation import extract_distances, extract_distances_bymouse, extract_distances_bystrain
import numpy as np


def test_sum_day():
    assert np.int(np.sum(extract_distances(1,2,3))) == 60789

def test_sum_bymouse():
    assert np.int(np.sum(extract_distances_bymouse(0,0))) == 493313

def test_sum_bystrain():
    assert np.int(np.sum(extract_distances_bystrain(0))) == 2088230

def test_first_day():
    assert extract_distances(1,2,3)[0] == 0

def test_first_bymouse():
    assert extract_distances_bymouse(0,0)[0] == 0

def test_first_bystrain():
    assert extract_distances_bystrain(0)[0] == 0

def test_shape_day():
    assert np.size(extract_distances(1,2,3)) == 822

def test_shape_bymouse():
    assert np.size(extract_distances_bymouse(0,0)) == 846

def test_shape_bystrain():
    assert np.size(extract_distances_bystrain(0)) == 864