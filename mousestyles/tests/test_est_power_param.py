from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pandas
from mousestyles.est_power_param import (fit_powerlaw, fit_exponential,
	fit_dist_all)


def test_fit_powerlaw():
    assert (fit_powerlaw(0, 0, 0) == 9.4748705008269827)


def test_fit_exponential():
    assert (fit_exponential(0, 0, 0) == 7.385844980814098)


def test_fit_dist_all():
    assert type(fit_dist_all()) is pandas.core.frame.DataFrame
