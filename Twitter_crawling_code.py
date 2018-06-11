# -*- coding: utf-8 -*-
import codecs
import tweepy
import time
import  sys
import csv
import json
from tweepy import OAuthHandler
import nltk
import re
import classifier


#required tokens for working with data from twitter using Tweepy
access_token = "103589925-PYiNRi6sAoSAFCau7Q5zDAqF7Kt8WwsK5EunWL3I"
access_token_secret = "u8N1nS93eN5npmtBOAxCwJgZE0W4wPCNe1CEuCB9lEIys"
consumer_key = "IIFBxSZv8YnhRJuvvDJVkR4ht"
consumer_secret = "zou3XOVMDXp9esingDNEowUeEPmTKkY4daZGYdmalovyd9JCxr"




auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
               wait_on_rate_limit_notify=True)

#Authenticating with given tokens
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)


def twitter_miner(query):
    tweetCount=0
    maxTweets=1000
    neg=0
    pos=0
    cnt=0
    while tweetCount < maxTweets:
        try:
           

            #crawling in hindi and hence the option of 'hi'
            newTweets=api.search(q=query, lang="hi", count=100)
            for tweet in newTweets:
                # printing only tweet
                #print (tweet.text)
                #print "####************************####"
                Tweet = tweet.text
                #Convert www.* or https?://* to URL
                Tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',Tweet)
                
                #Convert @username to User
                Tweet = re.sub('@[^\s]+','TWITTER_USER',Tweet)
                
                #Remove additional white spaces
                Tweet = re.sub('[\s]+', ' ', Tweet)
                
                #Replace #word with word Handling hashtags
                Tweet = re.sub(r'#([^\s]+)', r'\1', Tweet)
                
                #trim
                Tweet = Tweet.strip('\'"')
                
                #Deleting happy and sad face emoticon from the tweet 
                a = ':)'
                b = ':('
                Tweet = Tweet.replace(a,'')
                Tweet = Tweet.replace(b,'')
                
                #Deleting the Twitter @username tag and reTweets
                tag = 'TWITTER_USER' 
                rt = 'RT'
                url = 'URL'
                Tweet = Tweet.replace(tag,'')
                tweetCount+=1
                if rt in Tweet:
                  continue
                #Tweet = Tweet.replace(rt,'')
                Tweet = Tweet.replace(url,'')
                """l1= []
                for word in l:
                  if not word.isalpha() and not word[0]=='#' and not word[0]=='@' and not word[0]=='h':
                     l1.append(word)"""
                #print Tweet
                
                res=classifier.fn1(Tweet)
                print res
                if res == "negative":
                  neg=neg+1
                elif res == "positive":
                  pos=pos+1
                cnt=cnt+1
                #csvWriter.writerow([tweet.text])

        except tweepy.TweepError as e:
            print("some error : " + str(e))
            print("retrying in 20 seconds")
            time.sleep(20)
    
    per1=((float(pos)/cnt)*100)
    per2=((float(neg)/cnt)*100)
    return per1,per2
    print("POSITIVE {0}%".format(per1))
    print("NEGATIVE {0}%".format(per2))

def main(keyword):
  print("\nFetching'{0}':\n".format(keyword))
  per1,per2=twitter_miner(keyword)
  return per1,per2
  
if __name__ == "__main__":
  main()