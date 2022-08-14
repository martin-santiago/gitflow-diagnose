# most retweeted tweets
import json
from read_dataset import read_tweets
def top_retweeted():
    
    tweets = read_tweets()
    print('\n Los 10 tweets más retweeteados')
    print(tweets.nlargest(10, 'retweetCount').filter(items=['id','url', 'date', 'retweetCount']))
