"""Part 3 - Natural language processing

Work on the text column:

Extract people (persName) and add them to a column called persons
Extract places (placeName) and add them to a column called places
Extract organisations (orgName) and place them in the column called organisations"""

import pandas as pd
import spacy
import random
import os

os.chdir("/Users/arieldrozd/Downloads/PythonHomework-1/final_project_Drozd")

df = pd.read_csv("dane5.csv")
df.info()

nlp = spacy.load("pl_core_news_md")

# Extract people (persName) and add them to a column called persons
# Extract places (placeName) and add them to a column called places
# Extract organisations (orgName) and place them in the column called organisations
df.insert(35, "persons", "")
df.insert(36, "places", "")
df.insert(37, "organisations", "")
#df.info()
for i in range(len(df)):
    tokens = nlp(df["text"].iloc[i])
    df.iat[i,35] = []
    df.iat[i,36] = []
    df.iat[i,37] = []
    for token in tokens:
        if token.ent_type_ == "persName" and token.lemma_ not in df.iloc[i,35]:
            #print(token, token.lemma_, token.ent_type_)
            df.iloc[i,35].append(token.lemma_)
            #print(df.iloc[i,35])
        elif token.ent_type_ == "placeName" and token.lemma_ not in df.iloc[i,36]:
            #print(token, token.lemma_, token.ent_type_)
            df.iloc[i,36].append(token.lemma_)
            #print(df.iloc[i,36])
        elif token.ent_type_ == "orgName" and token.lemma_ not in df.iloc[i,37]:
            print(token, token.lemma_, token.ent_type_)
            df.iloc[i,37].append(token.lemma_)
            print(df.iloc[i,37])

# random testing
for i in range(10):
    num = random.randint(0, len(df)-1)
    print(df["text"].iloc[num], df["persons"].iloc[num], df["places"].iloc[num], df["organisations"].iloc[num])