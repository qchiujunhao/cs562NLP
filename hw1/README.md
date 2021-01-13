# Part 1

1. Program

   deserialize.py

   run "python deserialize.py data/*.xml.gz > deserialized.txt".


2. Sample terminal output

   deserialized_100.txt

   from "head -n 100 derserialized.txt > deserialized_100.txt" on linux

3. I used "wget -c -r -nd -k -L -p https://cslu.ohsu.edu/~bedricks/courses/cs662/resources/GW-cna_eng/" to download  the data. And then I wrote the program to read the data. As your tips, in the script, I used gzip and lxml.tree, and I dealt with the blank paragraphs using "etree.XMLParser(remove_blank_text=True)".

	Fortunately, I did not meet trouble.

# Part 2

 How many sentences are there in the CNA-GW corpus?

 	585064.

# Part 3

## Word counting & distribution

   part3.py solve this sub-part questions.

  1. How many unique types are present in this corpus? 
     
     143294

  2. How many unigram tokens?

     16676531

  3. Produce a rank-frequency plot (similar to those seen on the Wikipedia page for Zipf’s Law) for this corpus. 
  
  ![rand_frequency](https://github.com/qchiujunhao/cs562NLP/blob/main/hw1/part3_1_3.png)


  4. The thirty most common words:
	 
	 THE TO OF AND IN A THAT TAIWAN 'S SAID FOR ON WILL WITH IS AT AS BY HE BE FROM HAS CHINA WAS AN PERCENT ITS HAVE IT NOT

	 Stop and reflect: Are there entries in this list that do not look like what you might consider to be a “word”? How might you adjust your processing pipeline from Part 2 to correct for this?

	 	'S'. nltk.tokenize.TweetTokenizer can fix this problem
  
  5. You may notice that the most common are words that occur very frequently in the English language(stopwords). What happens to your  type/token counts if you remove stopwords using nltk.corpora’s stopwords list? 

     

     And the number of unique types are present in this corpus is 143156.

     And the number of unigram tokens is 10295204.

     So the number of unigram tokens has been reduced a lot although the number of types has not changed much.

  6. After removing stopwords, what are the thirty most common words?

     After removing stopwords, the thirtty most common words is "TAIWAN 'S SAID CHINA PERCENT GOVERNMENT ALSO CHEN PRESIDENT YEAR TAIPEI NT TWO MAINLAND PEOPLE US NEW CHINESE ACCORDING PARTY ECONOMIC BILLION FIRST NATIONAL ONE FOREIGN WOULD INTERNATIONAL OFFICIALS CITY".

     Stop and reflect: “What to count as stopwords” is an important design choice that is part of any NLP project. Look at the words contained in the nltk’s stopwords list. Does this list make sense? Are there entries that surprise you? Are there other words you would add?

     	I think it is very meaningful, because the words in the list are all words that do not affect the main meaning of the sentence, so they have little meaning for the training model. I haven't thought of adding any words for now.
     
     What might some important considerations be when generating a stopwords list?

     	These words appear frequently but do not affect the main meaning of the sentence. Removing it will reduce the need for computing resources.


## Word association metrics

   Recalling Emily Bender’s sage advice- “Look at your data!”- examine the 30 highest-PMI word pairs, along with their unigram and bigram frequencies. What do you notice?

      If the threshold is not set, the bigrams corresponding to the top 30 highest PMI values are just pairs of words that have only appeared once. Therefore, if the threshold is not set, the first 30 (even larger) PMI values are of no analytical significance.


  Experiment with a few different threshold values, and report on what you observe.

      The frequency of the two words corresponding to the maximum PMI is the closest to the set threshold. So if we want to get some suitable PMI values for analysis, we need to set a suitable threshold so that word pairs appear more frequently.
  

  With a threshold of 100, what are the 10 highest-PMI word pairs?

    ('SPONGIFORM', 'ENCEPHALOPATHY') pmi:  96208.30589177735 , ('SPONGIFORM', 'ENCEPHALOPATHY') freq:  105 ,  SPONGIFORM freq:  106 , ENCEPHALOPATHY freq:  106

    ('YING-', 'JEOU') pmi:  76640.81487633885 , ('YING-', 'JEOU') freq:  121 ,  YING- freq:  126 , JEOU freq:  129

    ('BOVINE', 'SPONGIFORM') pmi:  75786.60055746214 , ('BOVINE', 'SPONGIFORM') freq:  103 ,  BOVINE freq:  132 , SPONGIFORM freq:  106

    ('ALMA', 'MATER') pmi:  74371.96594427315 , ('ALMA', 'MATER') freq:  112 ,  ALMA freq:  136 , MATER freq:  114

    ('SRI', 'LANKA') pmi:  68982.24413073565 , ('SRI', 'LANKA') freq:  131 ,  SRI freq:  147 , LANKA freq:  133

    ('TOME', 'PRINCIPE') pmi:  51946.99018207289 , ('TOME', 'PRINCIPE') freq:  166 ,  TOME freq:  197 , PRINCIPE freq:  167

    ('KUALA', 'LUMPUR') pmi:  49730.53254579414 , ('KUALA', 'LUMPUR') freq:  202 ,  KUALA freq:  206 , LUMPUR freq:  203

    ('SAO', 'TOME') pmi:  46343.70606263811 , ('SAO', 'TOME') freq:  188 ,  SAO freq:  212 , TOME freq:  197

    ('AU', 'OPTRONICS') pmi:  43711.84228240087 , ('AU', 'OPTRONICS') freq:  164 ,  AU freq:  217 , OPTRONICS freq:  178

    ('ERIC', 'LILUAN') pmi:  42643.58707312753 , ('ERIC', 'LILUAN') freq:  139 ,  ERIC freq:  238 , LILUAN freq:  141


  Examine the PMI for “New York”. Explain in your own words why it is not higher.

    PMI for NEW YORK: 325.8864252413733. Because ‘new’ is often used with many other words, much more frequently than ‘york’.





  
