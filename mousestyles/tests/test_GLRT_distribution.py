from mousestyles.GLRT_distribution import random_powerlaw, random_exp, hypo_law_null, hypo_exp_null
import numpy

def test_random_powerlaw():
    assert type(random_powerlaw(4,2)) is numpy.ndarray
    
def test_random_exp():
    assert type(random_exp(4,2)) is numpy.ndarray

def test_hypo_powerLaw_null():
    assert (abs(hypo_law_null(0, 0, 0)-0.007)<=1.96*sqrt(0.007*(1-0.007))
            
def test_hypo_exp_null():
    assert (abs(hypo_exp_null(0, 0, 0)-1.0)<=1.96*sqrt(0.005*(1-0.005))