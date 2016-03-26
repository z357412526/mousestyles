"""Standard test data.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
from numpy.testing import assert_equal

import mousestyles.data as data


def test_all_features_mousedays_11bins():
    all_features = data.all_feature_data()
    print(all_features.shape)


