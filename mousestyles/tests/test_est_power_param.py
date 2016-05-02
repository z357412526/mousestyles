from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import numpy as np
import pandas as pd
from mousestyles.est_power_param import (fit_powerLaw, fit_exponential, fit)


def test_fit_powerLaw():
    assert (fit_powerLaw(0, 0, 0) == 9.4748705008269827)


def test_fit_exponential():
    assert (fit_exponential(0, 0, 0) == 7.385844980814098)


def test_fit():
    assert type(fit()) is pandas.core.frame.DataFrame
