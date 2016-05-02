# coding: utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

import numpy

from mousestyles.powerlaw import (powerlaw_pdf,exp_pdf)

def test_powerlaw_pdf():
	assert (powerlaw_pdf(2,2) == 0.25)

def test_exp_pdf():
	assert (exp_pdf(2,1) == 0.36787944117144233)