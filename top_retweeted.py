# most retweeted tweets
import json

def top_retweeted():
    tweetsList = []
    print("Started Reading JSON ")
    with open('farmers-protest-tweets-2021-03-5.json') as f:
        for jsonObj in f:
            tweetDict = json.loads(jsonObj)
            tweetsList.append(tweetDict)
    final_list = tweetsList.sort(reverse=True, key=sortMethod )
    print(final_list)
    print('los 10 tweets más retweeteados')
    
def sortMethod(e):
    return e["retweetCount"]

top_retweeted()