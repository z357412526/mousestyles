from __future__ import print_function, absolute_import, division

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import statistics as stat
import pandas as pd
from mousestyles import data

def fit_powerLaw (strain, mouse, day):
	"""
    Return the estimator of truncated power law.

    Parameters
    ----------
    strain : int
        the strain number of the mouse
    mouse  : int
        the mouse number in its strain
    day    :  int
    	the day number

    Returns
    -------
    estimator : a float number
    	The estimator of truncated power law.

    Examples
    --------
    >>> fit_powerLaw (0, 0, 0)
    9.4748705008269827
    """
    df  = data.load_movement(strain, mouse, day)
    xcood = df["x"]
    ycood = df["y"]
    distance_vector = np.sqrt(np.diff(xcood)**2+np.diff(ycood)**2)
    msk = distance_vector > 1
    cut_dist = distance_vector[msk]
    ret_mle = 1+len(cut_dist)*1/(np.sum(np.log(cut_dist/np.min(cut_dist))))
    return ret_mle


#script
esti_df = {"strain":[], "mouse":[],"day":[], "estimator":[]}
for i in range(3):
    for j in range(4):
        for k in range(12):
            try:
                temp = fit_powerLaw(i,j,k)
                esti_df["strain"].append(i)
                esti_df["mouse"].append(j)
                esti_df["day"] .append(k)
                esti_df["estimator"] .append(temp)
            except:
                next
                
estimation = pd.DataFrame(esti_df, columns = ["strain", "mouse", "day", "estimator"])
plt.hist(list(estimation.ix[estimation["strain"]==0,3]))
plt.hist(list(estimation.ix[estimation["strain"]==1,3]))
plt.hist(list(estimation.ix[estimation["strain"]==2,3]))
plt.title("Histogram: power law parameters distribution by strain")


