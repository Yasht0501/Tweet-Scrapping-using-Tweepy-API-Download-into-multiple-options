#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tweepy
import time
import pandas as pd
import os
from datetime import datetime


# In[10]:


API_KEY='uJUfRK2GdxfdqOyo43RWmkCbd'
API_KEY_SECRET='sK6WNrfYZKBhFKXyneWv6URESMwq7GwcLbKQER1D7B50WSkwdj'
BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAO1flAEAAAAA1ARt9PdBK5PTEzycA2S9siuzUpw%3D53nUrEuyuF01fEnl8R96x755zy9GNicLEnN2lUXkqlEAHx9zEj'
ACCESS_TOKEN='2551921020-ZkWwPqeqRgtJtESKnd5nnAWbVa12oK56WT1zBEB'
ACCESS_TOKEN_SECRET='PIKiOs0eewDKqsaKiPqQ99L7lrYCqa9clrqm5QMrqrX0m'

consumer_key = API_KEY
consumer_secret = API_KEY_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.API(auth)


# In[15]:


username = input("Enter the Username: ")
data = []
tweets = api.user_timeline(screen_name=username, count=50, tweet_mode='extended')
    
# Create a list to store the tweet data
tweet_data = []
    
# Loop through each tweet and extract relevant information
for tweet in tweets:
    tweet_data.append({
        'created_at': tweet.created_at,
        'text': tweet.full_text,
        'user': tweet.user.screen_name,
        'retweet_count': tweet.retweet_count,
        'favorite_count': tweet.favorite_count
    })
        
# Create a Pandas data frame from the tweet data
df3 = pd.DataFrame(tweet_data)
date_columns = df3.select_dtypes(include=['datetime64[ns, UTC]']).columns
    
for date_column in date_columns:
    df3[date_column] = df3[date_column].dt.date
    
print("1 - Show Tweets.")
print("2 - Download Tweets.")
print("3 - Get Tweets by date.")
s = input("Select a option from the above: ")
if s == "1":
    display(df3)
elif s == "2":
    print("1 - Excel")
    print("2 - CSV")
    print("3 - JSON")
    d = input("Select a download option from above: ")
    if d == "1":
        f = input("Enter the Name of the file: ")
        if os.path.isfile(f+".xlsx"):
            print("File already Exists.")
        else:
            df.to_excel(f+".xlsx",index=False)
    elif d == "2":
        f1 = input("Enter the Name of the file: ")
        if os.path.isfile(f1+".csv"):
            print("File already Exists.")
        else:
            df3.to_csv(f1+".csv",index=False)
    elif d == "3":
        f2 = input("Enter the Name of the file: ")
        if os.path.isfile(f2+".json"):
            print("File already Exists.")
        else:
            df3.to_json(f2+".json")
    else:
        print("Invalid Input.")
elif s == "3":
    username = input("Enter the username: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Create a list to store the tweet data
    data = []
    
    # Retrieve tweets from the user's timeline
    query = f"from:{username} since:{start_date} until:{end_date}"
    tweets = api.search_tweets(q=query)
    
    for tweet in tweets:
        data.append([tweet.created_at,tweet.user.screen_name,tweet.text,tweet.retweet_count,tweet.favorite_count])
        
    if data != []:
        columns = ['Date', 'User', 'Tweet','Retweet','Favorite']
        pd.set_option('display.max_colwidth', None) 
        df = pd.DataFrame(data, columns=columns)
        date_columns = df.select_dtypes(include=['datetime64[ns, UTC]']).columns
        
        for date_column in date_columns:
            df[date_column] = df[date_column].dt.date
            
        print("1 - Show Tweets.")
        print("2 - Download Tweets.")
        print("3 - Show tweets by keyword.")
        s = input("Select a option from the above: ")
        if s == "1":
            display(df)
        elif s == "2":
            print("1 - Excel")
            print("2 - CSV")
            print("3 - JSON")
            d = input("Select a download option from above: ")
            if d == "1":
                f = input("Enter the Name of the file: ")
                if os.path.isfile(f+".excel"):
                    print("File already Exists.")
                else:
                    df.to_excel(f+".xlsx",index=False)
            elif d == "2":
                f1 = input("Enter the Name of the file: ")
                if os.path.isfile(f1+".csv"):
                    print("File already Exists.")
                else:
                    df.to_csv(f1+".csv",index=False)
            elif d == "3":
                f2 = input("Enter the Name of the file: ")
                if os.path.isfile(f2+".json"):
                    print("File already Exists.")
                else:
                    df.to_json(f2+".json")
            else:
                print("Invalid Input.")
        elif s == "3":
            keyword = input("Enter Keywords: ")
            data = []

            for i, status in enumerate(tweepy.Cursor(api.search_tweets, q=keyword).items(50)):
                data.append({
                'created_at': status.created_at,
                'text': status.text,
                'user': status.user.screen_name,
                'retweet_count': status.retweet_count,
                'favorite_count': status.favorite_count
            })

            df = pd.DataFrame(data)
            date_columns = df.select_dtypes(include=['datetime64[ns, UTC]']).columns
            for date_column in date_columns:
                df[date_column] = df[date_column].dt.date
            print("1 - Show Tweets.")
            print("2 - Download Tweets.")
            s = input("Select a option from the above: ")
            if s == "1":
                display(df)
            elif s == "2":
                print("1 - Excel")
                print("2 - CSV")
                print("3 - JSON")
                d = input("Select a download option from above: ")
                if d == "1":
                    f = input("Enter the Name of the file: ")
                    if os.path.isfile(f+".excel"):
                        print("File already Exists.")
                    else:
                        df.to_excel(f+".xlsx",index=False)
                elif d == "2":
                    f1 = input("Enter the Name of the file: ")
                    if os.path.isfile(f1+".excel"):
                        print("File already Exists.")
                    else:
                        df.to_csv(f1+".csv",index=False)
                elif d == "3":
                    f2 = input("Enter the Name of the file: ")
                    if os.path.isfile(f2+".excel"):
                        print("File already Exists.")
                    else:
                        df.to_json(f2+".json")
                else:
                    print("Invalid Input.")
            else:
                print("Invalid Input.")
    else:
        print("DATA NOT FOUND!")
        