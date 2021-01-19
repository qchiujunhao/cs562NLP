from collections import Counter

import pandas as pd
import numpy as np

# deliverable 1.1
def bag_of_words(text):
    """
    Count the number of word occurrences for a given document
    
    :param text: a document, as a single string
    :returns: a Counter representing a single document's word counts
    :rtype: Counter
    """

    words_list = [word for word in text.split()]
    counter = Counter(words_list)

    return counter
    

# deliverable 1.2
def aggregate_counts(bags_of_words):
    """
    Aggregate bag-of-words word counts across an Iterable of documents into a single bag-of-words.
    
    :param bags_of_words: an iterable of bags of words, produced from the bag_of_words() function above
    :returns: an aggregated bag of words for the whole corpus
    :rtype: Counter
    """

    counter = Counter()
    for bow in bags_of_words:
    	counter = counter + bow

    return counter
    
    
# deliverable 1.3
def compute_oov(bow1, bow2):
    """
    Return a set of words that appears in bow1, but not bow2

    :param bow1: a bag of words
    :param bow2: a bag of words
    :returns: the set of words in bow1, but not in bow2
    :rtype: set
    """
    diff = bow1.keys() - bow2.keys()
    return diff
    
    
    
# deliverable 1.4
def prune_vocabulary(training_counts, target_data, min_counts):
    """
    Prune target_data to only include words that occur at least min_counts times in training_counts
    
    :param training_counts: aggregated Counter for the training data
    :param target_data: list of Counters containing dev bow's
    :returns: new list of Counters, with pruned vocabulary
    :returns: list of words in pruned vocabulary
    :rtype list of Counters, set
    """
    counters_list = []
    for c in target_data:
    	new_c = {k:v for k,v in c.items() if (k in training_counts.keys() and training_counts[k]>=min_counts)}
    	counters_list.append(Counter(new_c))

    words_list = set(filter(lambda x: training_counts[x] >= min_counts, training_counts))

    return counters_list, words_list

    
    

# Helper functions

def read_data(fname, label='Era', preprocessor=bag_of_words): 
    df = pd.read_csv(fname)
    return (df[label].values, [preprocessor(string) for string in df['Lyrics'].values])
    
def oov_rate(bow1, bow2):
    return len(compute_oov(bow1, bow2)) / len(bow1.keys())