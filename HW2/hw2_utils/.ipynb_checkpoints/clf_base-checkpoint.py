from hw2_utils.constants import OFFSET
import numpy as np

# HELPER FUNCTION
def argmax(score_dict):
    """
    Find the 
    :param score_dict: A dict whose keys are labels and values are scores
    :returns: Top-scoring label
    :rtype: string
    """
    items = list(score_dict.items())
    items.sort()
    return items[np.argmax([i[1] for i in items])][0]


# deliverable 2.1
def make_feature_vector(base_features, label):
    """
    Take a dict of bag-of-words features and a label; return a dict of features, corresponding to f(x,y)
    
    :param base_features: Counter of base features
    :param label: label string
    :returns dict of features, f(x,y)
    :rtype: dict
    """

    return_features = {}
    for k,v in base_features.items():
        return_features[(label, k)] = v

    return_features[(label, OFFSET)] = 1

    return return_features
    
# deliverable 2.2
def predict(base_features, weights, labels):
    """
    Simple linear prediction function y_hat = argmax_y \theta^T f(x,y)
    
    :param base_features: a dictionary of base features and counts (base features, NOT a full feature vector)
    :param weights: a defaultdict of features and weights. Features are tuples (label, base_feature)
    :param labels: a list of candidate labels
    :returns: top-scoring label, plus the scores of all labels
    :rtype: string, dict
    """
    
    scores = dict()

    for l in labels:
        scores[l] = 0
        features_made = make_feature_vector(base_features, l)

        for _, word in features_made:
            if (l, word) in weights:
                scores[l] += weights[(l, word)] * features_made[(l, word)]

    return argmax(scores), scores


    
def predict_all(x, weights, labels):
    """
    Predict the label for all instances in a dataset. For bulk prediction.
    
    :param x: iterable of base instances
    :param weights: defaultdict of weights
    :param labels: a list of candidate labels
    :returns: predictions for each instance
    :rtype: numpy array
    """
    y_hat = np.array([predict(x_i, weights, labels)[0] for x_i in x])
    return y_hat
    