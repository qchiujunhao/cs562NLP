from  hw2_utils import constants 
import numpy as np

# deliverable 4.1
def get_token_type_ratio(counts):
    """
    Compute the ratio of tokens to types
    
    :param counts: bag of words feature for a song
    :returns: ratio of tokens to types
    :rtype float
    """
    
    if len(counts) == 0:
        return 0.0

    num = 0
    for v in counts.values():
        if v>0:
            num += 1
    return sum(counts.values()) / num


# deliverable 4.2
def concat_ttr_binned_features(data):
    """
    Add binned token-type ratio features to the observation represented by data
    
    :param data: Bag of words
    :returns: Bag of words, plus binned ttr features
    :rtype: dict
    """

    ttr = int(get_token_type_ratio(data))
    if ttr > 6:
        ttr = 6

    data[constants.TTR_ZERO] = 0
    data[constants.TTR_ONE] = 0
    data[constants.TTR_TWO] = 0
    data[constants.TTR_THREE] = 0
    data[constants.TTR_FOUR] = 0 
    data[constants.TTR_FIVE] = 0
    data[constants.TTR_SIX] = 0

    if ttr == 0:
        data[constants.TTR_ZERO] = 1
    elif ttr == 1:
        data[constants.TTR_ONE] = 1
    elif ttr == 2:
        data[constants.TTR_TWO] = 1
    elif ttr == 3:
        data[constants.TTR_THREE] = 1
    elif ttr == 4:
        data[constants.TTR_FOUR] = 1
    elif ttr == 5:
        data[constants.TTR_FIVE] = 1
    elif ttr == 6:
        data[constants.TTR_SIX] = 1

    return data



                                                                    

