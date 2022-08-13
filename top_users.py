# users with most tweets
import json

def top_users:
    tweetsList = []
    print("Started Reading JSON ")
    with open('farmers-protest-tweets-2021-03-5.json') as f:
        for jsonObj in f:
            tweetDict = json.loads(jsonObj)
            tweetsList.append(tweetDict)
    pass