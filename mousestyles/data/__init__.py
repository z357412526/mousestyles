import os as _os

import numpy as np

from mousestyles import data_dir

def all_feature_data():

    feat_arr = ['ASProbability', 'ASNumbers', 'ASDurations', 'Food', 'Water', 'Distance', 'ASFoodIntensity', 'ASWaterIntensity', 'MoveASIntensity']
    feat_arr_units = ['Active state probability', 'Number AS onsets', 'Total time [sec]', 'Food consumed [g]', 'Water consumed [mg]', 'Distance travelled [m]', 'ASFoodIntensity', 'ASWaterIntensity', 'MoveASIntensity [cm/ASsec]']
    
    data_orig_master = np.load(_os.path.join(data_dir, 'all_features_mousedays_11bins.npy'))  # 9 x 1921 x (3 labels + 11 feature time bins)
    features = data_orig_master[:, :, 3:]
    labels = data_orig_master[0, :, 0:3]  # 1st col = strain, 2nd = mouse number, 3rd = day
    return data_orig_master
