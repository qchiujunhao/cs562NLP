import argparse

import string
from nltk.tokenize import sent_tokenize, word_tokenize 

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
args = parser.parse_args()

punct_set = set(string.punctuation)
punct_set = set.union(punct_set, ["``", "''", "--", "..."])

with open(args.file_name, 'r') as fin:
	text = fin.read().replace('\n', ' ').upper()

	sentences = sent_tokenize(text)
	for s in sentences:
		tokens = word_tokenize(s)
		tokens_no_punct = [t for t in tokens if t not in punct_set]
		print(" ".join(tokens_no_punct))


