# Importing required libraries
# Fuente del código correspondiente a la documentación del dataset
#  --> https://www.kaggle.com/code/prathamsharma123/clean-raw-json-tweets-data
import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")


def read_tweets():
    raw_tweets = pd.read_json(r'farmers-protest-tweets-2021-03-5.json', lines=True)
    raw_tweets = raw_tweets[raw_tweets['lang']=='en']
    print("Shape: ", raw_tweets.shape)
    return raw_tweets
