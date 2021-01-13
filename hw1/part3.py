import argparse
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import collections
import matplotlib
import matplotlib.pyplot as plt
import operator
from nltk.corpus import stopwords

def compute_pmi(prob_unis, prob_bigrams, freqdist, threshold=0):


	dict_freqdist = dict(freqdist)
	dict_prob_unis = dict(prob_unis)
	
	pmi = [(pb[0], pb[1]/(dict_prob_unis[pb[0][0]]*dict_prob_unis[pb[0][1]])) for pb in prob_bigrams if dict_freqdist[pb[0]] > threshold]
	sorted_pmi = sorted(pmi, key=lambda x: x[1], reverse=True)

	return sorted_pmi

	


def compute_prob_unigrams(tokens_count, freqdist):
	
	prob_unis = [(f[0], f[1]/tokens_count) for f in freqdist]

	return prob_unis

def compute_prob_bigrams(tokens):
	
	bigrams_list = nltk.bigrams(tokens)

	fdist_bigrams = (FreqDist(bigrams_list))

	sorted_fdist_bigrams = sorted(fdist_bigrams.items(), key=lambda x: x[1], reverse=True)
	len_fb = len(list(nltk.bigrams(tokens)))

	prob_bigrams = [(f[0], f[1]/len_fb) for f in sorted_fdist_bigrams]

	return prob_bigrams, fdist_bigrams
	
	
	

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("file_name")
	args = parser.parse_args()

	with open(args.file_name, 'r') as fin:
		text = fin.read()

	tokens = word_tokenize(text)

	#print(type(tokens))

	print("The count of unique types:")
	print(len(set(tokens)))
	print("The count of unigram tokens:")
	print(len(tokens))

	fdist = dict(FreqDist(tokens))
	fdist = sorted(fdist.items(), key=lambda x: x[1], reverse=True)

	ranks = range(1, len(fdist)+1)
	freqs = [f[1] for f in fdist]

	plt.loglog(ranks, freqs)
	plt.title("ranks-freqs plot")
	plt.ylabel('log(freqs)', fontsize=14)
	plt.xlabel('log(ranks)', fontsize=14)
	plt.savefig('part3_1_3.png')


	print("The thirty most common words:")
	thirty_list = []
	for f in fdist[:30]:
		thirty_list.append(f[0])

	print(" ".join(thirty_list))

	stops = set(stopwords.words('english'))

	tokens_no_stopwords = []
	for t in tokens:
		if t.lower() not in stops:
			tokens_no_stopwords.append(t)

	fdist_no_stop = (FreqDist(tokens_no_stopwords))

	sorted_fdist_no_stop = sorted(fdist_no_stop.items(), key=lambda x: x[1], reverse=True)

	print("The new thirty most common words:")
	thirty_list_no_stop = []
	for f in sorted_fdist_no_stop[:30]:
		thirty_list_no_stop.append(f[0])

	print(" ".join(thirty_list_no_stop))

	print("The count of unique types without stopwords:")
	print(len(set(tokens_no_stopwords)))
	print("The count of unigram tokens without stopwords:")
	print(len(tokens_no_stopwords))

	prob_unis = compute_prob_unigrams(len(tokens_no_stopwords), sorted_fdist_no_stop)
	prob_bigrams, fdist_bigrams = compute_prob_bigrams(tokens_no_stopwords)

	sorted_pmi_0 = compute_pmi(prob_unis, prob_bigrams, fdist_bigrams, 0)
	sorted_pmi_10 = compute_pmi(prob_unis, prob_bigrams, fdist_bigrams, 10)
	sorted_pmi_100 = compute_pmi(prob_unis, prob_bigrams, fdist_bigrams, 100)
	sorted_pmi_200 = compute_pmi(prob_unis, prob_bigrams, fdist_bigrams, 200)

	dict_sorted_pmi_100 = dict(sorted_pmi_100)
	dict_sorted_fdist_no_stop = dict(sorted_fdist_no_stop)
	dict_fdist_bigrams = dict(fdist_bigrams)


	print('Threshold is 0')
	for spmi in sorted_pmi_0[:30]:
		print(str(spmi[0]),'pmi: ',str(spmi[1]),',',str(spmi[0]),'freq: ',str(dict_fdist_bigrams[spmi[0]]),', ',str(spmi[0][0]), 'freq: ' ,str(dict_sorted_fdist_no_stop[spmi[0][0]]),', '+str(spmi[0][1]),'freq: ',str(dict_sorted_fdist_no_stop[spmi[0][1]]))

	print('Threshold is 10')
	for spmi in sorted_pmi_10[:30]:
		print(str(spmi[0]),'pmi: ',str(spmi[1]),',',str(spmi[0]),'freq: ',str(dict_fdist_bigrams[spmi[0]]),', ',str(spmi[0][0]), 'freq: ' ,str(dict_sorted_fdist_no_stop[spmi[0][0]]),', '+str(spmi[0][1]),'freq: ',str(dict_sorted_fdist_no_stop[spmi[0][1]]))


	print('Threshold is 100')
	for spmi in sorted_pmi_100[:30]:
		print(str(spmi[0]),'pmi: ',str(spmi[1]),',',str(spmi[0]),'freq: ',str(dict_fdist_bigrams[spmi[0]]),', ',str(spmi[0][0]), 'freq: ' ,str(dict_sorted_fdist_no_stop[spmi[0][0]]),', '+str(spmi[0][1]),'freq: ',str(dict_sorted_fdist_no_stop[spmi[0][1]]))


	print('Threshold is 200')
	for spmi in sorted_pmi_200[:30]:
		print(str(spmi[0]),'pmi: ',str(spmi[1]),',',str(spmi[0]),'freq: ',str(dict_fdist_bigrams[spmi[0]]),', ',str(spmi[0][0]), 'freq: ' ,str(dict_sorted_fdist_no_stop[spmi[0][0]]),', '+str(spmi[0][1]),'freq: ',str(dict_sorted_fdist_no_stop[spmi[0][1]]))

	print('PMI for NEW YORK')
	print(dict_sorted_pmi_100[('NEW', 'YORK')])

