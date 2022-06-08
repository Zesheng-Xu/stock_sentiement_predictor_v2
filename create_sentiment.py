from textblob import TextBlob
import nltk
from textblob.sentiments import NaiveBayesAnalyzer
import tweepy
import numpy


def returnComputedSentiment(inputString):
  opinion = TextBlob(inputString, analyzer=NaiveBayesAnalyzer())
  return opinion.sentiment
