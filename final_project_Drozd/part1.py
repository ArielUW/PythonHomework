"""Part 1 - Processing and cleaning the data
Replace abbreviated weekday names with english equivalents (full weekday names) - created_at column
Replace abbreviated month names with numerical equivalents (e.g. Jun to 06) - user_created_at column
Get all links to tweets and pass them to the list
Get all links found in tweets and pass them to the list (urls column)
Get all image links and pass them to the list (media column)
Remove all words marked as stopwords and pass the cleaned text to a new column called text_without_stopwords.
"""
import pandas as pd
import os

os.chdir("/Users/arieldrozd/Downloads/PythonHomework-1/final_project_Drozd")

df = pd.read_csv("dane5.csv")

# Replace abbreviated weekday names with english equivalents (full weekday names) - created_at column
for i in range(len(df["created_at"])):
    df["created_at"].iloc[(i)] = df["created_at"].iloc[(i)].replace("Mon", "Monday").replace("Tue", "Tuesday").replace("Wed", "Wednesday").replace("Thu", "Thursday").replace("Fri", "Friday").replace("Sat", "Saturday").replace("Sun", "Sunday")

# Replace abbreviated month names with numerical equivalents (e.g. Jun to 06) - user_created_at column
for i in range(len(df["user_created_at"])):
    df["user_created_at"].iloc[(i)] = df["user_created_at"].iloc[(i)].replace("Jan", "01").replace("Feb", "02").replace("Mar", "03").replace("Apr", "04").replace("May", "05").replace("Jun", "06").replace("Jul", "07").replace("Aug", "08").replace("Sep", "09").replace("Oct", "10").replace("Nov", "11").replace("Dec", "12")

#print(df["created_at"], df["user_created_at"])

# Get all links to tweets and pass them to the list
links_to_tweets = [link for link in df["tweet_url"]]
#print(links_to_tweets)

# Get all links found in tweets and pass them to the list (urls column)
links_in_tweets = [link for link in df["urls"] if type(link)==str]
#print(links_in_tweets)

#Get all image links and pass them to the list (media column)
media_in_tweets = [media for media in df["media"] if type(media)==str]
#print(media_in_tweets)

df.to_csv("new_dataset.csv")