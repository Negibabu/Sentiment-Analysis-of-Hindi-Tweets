#!/usr/bin/env python
# -*- coding: utf-8 -*-
# credit to : http://www.laurentluce.com/

# importing the Natural Language Toolkit library
import nltk
import Twitter_crawling_code
import codecs

# training data set 
# positive tweets datset
pos_tweets = codecs.open("pos_train.txt",'r','utf-8')

# negative tweets dataset
neg_tweets =  codecs.open("neg_train.txt",'r','utf-8')

# merging the two list in one big training tuple and filtering two letters words 
tweets = []
sentiment = "positive"
for words in pos_tweets.readlines():
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))

sentiment = "negative"
for words in neg_tweets.readlines():
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))



# getting word frequencies from the training data 

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


word_features = get_word_features(get_words_in_tweets(tweets))

# building a feature extractor
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)

    return features

# building the training set
training_set = nltk.classify.apply_features(extract_features, tweets)

# training the classifier 
classifier = nltk.NaiveBayesClassifier.train(training_set)

def fn1(tweet):
	#print tweet.split()
	return classifier.classify(extract_features(tweet.split()))

