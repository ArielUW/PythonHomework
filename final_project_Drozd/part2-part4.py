"""Part 2 - Exploratory data analysis

List the top 5 tweets with the highest number of likes.
List the top 5 tweets with the highest number of retweets.
Show only tweets that are not considered 'sensitive' (possibly_sensitive column).
Show the tweets of the user who created the account earliest (of all users in the dataset) (user_created_at column).
Show the tweets of the user with the most followers.
Show only verified users (user_verified column).
Indicate on which day of the week the tweets in the dataset were most frequently published."""

import pandas as pd
import sqlite3 as sql
import os
from collections import Counter
import matplotlib.pyplot as plt

os.chdir("/Users/arieldrozd/Downloads/PythonHomework-1/final_project_Drozd")

conn = sql.connect("database.db")
cursor = conn.cursor()

df = pd.read_csv("dane5.csv")
#df.info()
df.to_sql('twitter', conn, if_exists='replace', index = False)

#List the top 5 tweets with the highest number of likes.
#print(df["favorite_count"])
cursor.execute("SELECT text, favorite_count FROM twitter ORDER BY favorite_count DESC LIMIT 5")
results = cursor.fetchall()
print("\n-- 💙 Top 5 results with the highest number of likes 💙 --\n")
i = 1
for text, likes in results:
    print(f"- Tweet #{i} -\nText: {text}\nLikes: {likes}\n")
    i+=1

#List the top 5 tweets with the highest number of retweets.
cursor.execute("SELECT text, retweet_count FROM twitter ORDER BY retweet_count DESC LIMIT 5")
results = cursor.fetchall() # this has the same tweet 5 times, but there are multiple records like that in the original data as well – I can't do anything about it! 
i = 1
print("-- 🔃 Top 5 results with the highest number of retweets 🔃 --\n")
for text, retweets in results:
    print(f"- Tweet #{i} -\nText: {text}\nRetweets: {retweets}\n")
    i+=1

#Show only tweets that are not considered 'sensitive' (possibly_sensitive column).
#print(df["possibly_sensitive"].to_string(index=False))
cursor.execute("SELECT text FROM twitter WHERE possibly_sensitive != False")
texts = cursor.fetchall()
print("-- 😬 Possibly sensitive tweets 😬 --\n")
i=1
for text in texts:
    print(f"- Tweet #{i} -\n{text[0]}\n")
    i+=1

#Show the tweets of the user who created the account earliest (of all users in the dataset) (user_created_at column).
cursor.execute("SELECT user_name, user_created_at FROM twitter ORDER BY user_created_at DESC LIMIT 1")
user, date = cursor.fetchone()
cursor.execute(f"SELECT text FROM twitter WHERE user_name = '{user}'")
texts = cursor.fetchall()
print(f"-- ⏳ User {user} has created the account the earliest of all the users in the dataset ⌛️ --\n\nThe account was created on {date}.\nThose are their tweets:\n")
i=1
for text in texts:
    print(f"- Tweet #{i} -\n{text[0]}\n")
    i+=1

#Show the tweets of the user with the most followers.
cursor.execute("SELECT user_name, user_followers_count FROM twitter ORDER BY user_followers_count DESC LIMIT 1")
user, followers = cursor.fetchone()
cursor.execute(f"SELECT text FROM twitter WHERE user_name = '{user}'")
texts = cursor.fetchall()
print(f"-- ✨ User {user} has the most followers of all the users in the dataset✨ --\n\nThey have {followers} followers.\nThose are the tweets from {user}'s account:\n")
i=1
for text in texts:
    print(f"- Tweet #{i} -\n{text[0]}\n")
    i+=1

#Show only verified users (user_verified column).
cursor.execute("SELECT user_name FROM twitter WHERE user_verified = True")
users = cursor.fetchall()
print(f"-- ✅ Users with verified accounnts ✅ --\n")
for user in users:
    print(user[0])

#Indicate on which day of the week the tweets in the dataset were most frequently published.
c = Counter()
cursor.execute("SELECT created_at FROM twitter")
dates = cursor.fetchall()
for date in dates:
    day=date[0][:3]
    c[day]+=1
dayOfTheWeek, count = c.most_common(1)[0]
dayOfTheWeek = dayOfTheWeek.replace("Mon", "Monday").replace("Tue", "Tuesday").replace("Wed", "Wednesday").replace("Thu", "Thursday").replace("Fri", "Friday").replace("Sat", "Saturday").replace("Sun", "Sunday")
print(f"\n-- 📈 Most tweets in the dataset ({count}) were published on {dayOfTheWeek} 📈 --\n")

"""Part 4 - Problem solving/interpreting documentation skills

Using the matplotlib package, create a graph showing the number of tweets per day of the week."""

#print(c["Mon"], c["Tue"], c["Wed"], c["Thu"], c["Fri"], c["Sat"], c["Sun"])
#df = pd.DataFrame.from_dict(c, orient="index")
#print(df)

x = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y = [c[i] for i in x]
annotations = y

plt.style.use('dark_background')
plt.rcParams["font.family"] = "monospace"

fig, ax = plt.subplots(figsize=(8,6))
fig.tight_layout(pad=8)

ax.stem(x, y, linefmt="--", markerfmt="")
ax.scatter(x, y, marker="o", c=y, cmap="autumn_r", zorder=2)
ax.set_ybound(0, 120)

for xi, yi, text in zip(x,y,annotations):
    ax.annotate(text,
                xy=(xi, yi), xycoords="data",
                xytext=(3, 3), textcoords="offset points")

fig.suptitle("Number of tweets per day of the week", fontsize=18, x=0.5, y=0.93, bbox={'pad': 10, 'color':"m"})
ax.set_xlabel("Day of the week", fontsize = 14, labelpad = 22)
ax.set_ylabel("Number of tweets", fontsize = 14, labelpad = 20)

plt.show()