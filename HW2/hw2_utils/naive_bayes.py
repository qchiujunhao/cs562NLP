from hw2_utils.constants import OFFSET
from hw2_utils import clf_base, evaluation

import numpy as np
from collections import defaultdict, Counter
from itertools import chain
import math

# deliverable 3.1
def get_corpus_counts(x,y,label):
    """
    Compute corpus counts of words for all documents with a given label.

    :param x: list of counts, one per instance
    :param y: list of labels, one per instance
    :param label: desired label for corpus counts
    :returns: defaultdict of corpus counts
    :rtype: defaultdict

    """

    return_list = defaultdict(float)

    for i in range(len(y)):
        if y[i] == label:
            for word, freq in x[i].items():
                return_list[word] += freq
                

    return return_list


# deliverable 3.2
def estimate_pxy(x,y,label,smoothing,vocab):
    """
    Compute smoothed log-probability P(word | label) for a given label. (eq. 2.30 in Eisenstein, 4.14 in J&M)

    :param x: list of counts, one per instance
    :param y: list of labels, one per instance
    :param label: desired label
    :param smoothing: additive smoothing amount
    :param vocab: list of words in vocabulary
    :returns: defaultdict of log probabilities per word
    :rtype: defaultdict of log probabilities per word

    """
    
    counts_list = get_corpus_counts(x,y,label)

    return_list = defaultdict(float)

    sum_count = math.log(sum(counts_list.values()) + len(vocab) * smoothing)

    for v in vocab:

        return_list[v] = math.log((counts_list[v] + smoothing)) - sum_count

    return return_list

    

# deliverable 3.3
def estimate_nb(x,y,smoothing):
    """
    Estimate a naive bayes model

    :param x: list of dictionaries of base feature counts
    :param y: list of labels
    :param smoothing: smoothing constant
    :returns: weights, as a default dict where the keys are (label, word) tuples and values are smoothed log-probs of P(word|label)
    :rtype: defaultdict 

    """
    
    labels = set(y)
    counts = defaultdict(float)
    doc_counts = defaultdict(float)

    vocab = set([k for c in x for k in c])
    for y_ in y:
        doc_counts[y_] += 1
    
    weights = defaultdict(float)
    for l in labels:
        log_probs = estimate_pxy(x, y, l, smoothing, vocab)
        for word, prob in log_probs.items():
            weights[(l, word)] = prob
        weights[(l, OFFSET)] = math.log(doc_counts[l] / len(y))

    return weights
# deliverable 3.4
def find_best_smoother(x_tr,y_tr,x_dv,y_dv,smoothers):
    """
    Find the smoothing value that gives the best accuracy on the dev data

    :param x_tr: training instances
    :param y_tr: training labels
    :param x_dv: dev instances
    :param y_dv: dev labels
    :param smoothers: list of smoothing values
    :returns: best smoothing value, scores
    :rtype: float, dict mapping smoothing value to score
    """

    labels = set(y_tr)
    acc = {}
    for smoothing in smoothers:
        theta_nb = estimate_nb(x_tr, y_tr, smoothing)
        y_dv_hat = clf_base.predict_all(x_dv, theta_nb, labels)
        acc[smoothing] = evaluation.acc(y_dv_hat, y_dv)

    best_sm = clf_base.argmax(acc)
    return best_sm, acc
    