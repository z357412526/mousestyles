import os as _os
import numpy as np
import pandas as pd
from mousestyles import data_dir

def load_all_features():
    """
    Returns a (21131, 13) size pandas.DataFrame object corresponding to
    9 features over each mouse's 2-hour time bin. The first four columns
    index each mouses's 2-hour bin:

    Column 0: the strain of the mouse (0-15)
    Column 1: the mouse number (number depends on strain)
    Column 2: the day number (5-16)
    Column 3: 

    The remaining 9 columns are the computed features.

    Returns
    -------
    features_data_frame : pandas.DataFrame
        A dataframe of computed features.
    """
    features = ['ASProbability', 'ASNumbers', 'ASDurations', 'Food', 'Water', 'Distance', 'ASFoodIntensity', 'ASWaterIntensity', 'MoveASIntensity']

    all_features = np.load(_os.path.join(data_dir, 'all_features_mousedays_11bins.npy'))  # 9 x 1921 x (3 labels + 11 feature time bins)
   
    # Here we begin reshaping the 3-d numpy array into a pandas 2-d dataframe
    columns = ['strain', 'mouse', 'day']
    for i in range(11):
        columns.append(i * 2) #Append 2-hour time bin values
    
    # For each feature, unpivot its dataframe so that the 2-hour
    # time bins become a value column, rather than a dimension
    data_frames = []
    for (i, feature) in enumerate(features):
        df = pd.DataFrame(data=all_features[i,:,:], columns=columns)
        melted_df = pd.melt(df, id_vars=columns[:3], value_vars=columns[3:],
                var_name='hour', value_name=feature)
        data_frames.append(melted_df)

    # Connect each of the feature dataframes to make one dataframe
    all_features_df = data_frames.pop(0)
    other_features = [x.iloc[:,-1] for x in data_frames]
    other_features.insert(0, all_features_df)
    return pd.concat(other_features, axis=1)
