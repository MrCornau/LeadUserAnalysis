# %%
from os.path import isfile, join
from os import listdir
from os import walk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.ticker as ticker
import json
import os
import re
import numpy as np
from datetime import datetime
import spacy


nlp = spacy.load("/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Word2Vec/Core20e.model")

#%%
datapath = '/Users/joshcornau/Code/SpaCy_FirstModel/Big_Data/Photrio_Format.json'


#%%
mypath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Reddit'
Paths = []
for (dirpath, dirnames, filenames) in walk(mypath):

    for file in filenames:
        if file.endswith('.xlsx'):
            Paths.append(file)
    break

print(Paths)


#%%

df = []


for idx, File in enumerate(Paths):
    path = mypath+"/"+File
    res = pd.read_excel(
        path)
    df.append({
        "name": File.replace('.xlsx', ''),
        "content": res
    })

print(df[0])

#%%

print(len(df))

#%%
def countWords(Analyse):
    doc = nlp(Analyse)
    i=0
    for token in doc:
        if(token.pos_ !='PUNCT'):
            i+=1
    return(i)


interestingcomments = {}
interestingcomments['interestingcomments'] = []

for idx, file in enumerate(df):
    for idx2, comment in enumerate(file['content'].selftext):
        try:
            if isinstance(comment, str) and isinstance(df[idx]['content'].title[idx2], str):
                analyse = df[idx]['content'].title[idx2] + ' /!/ ' + comment
            elif isinstance(comment, str) and not isinstance(df[idx]['content'].title[idx2], str):
                analyse = comment
            elif not isinstance(comment, str) and isinstance(df[idx]['content'].title[idx2], str):
                analyse = df[idx]['content'].title[idx2]
            else:
                analyse = ' '
        except Exception as e:
            analyse = ' '

        interestingcomments['interestingcomments'].append({
                "origin": "Reddit",
                "suborigin": str(df[idx]['content'].subreddit[idx2]),
                "removed": str(df[idx]['content'].removed_by_category[idx2]),
                "autor":  str(df[idx]['content'].author[idx2]),
                "link":  str(df[idx]['content'].full_link[idx2]),
                "title": str(df[idx]['content'].title[idx2]),
                "text": str(df[idx]['content'].selftext[idx2]),
                "content":analyse,
                "score": int(df[idx]['content'].score[idx2]),
                "upvote_ratio": df[idx]['content'].upvote_ratio[idx2],
                "date": str(datetime.utcfromtimestamp(df[idx]['content'].created_utc[idx2])),
                "comments":int(df[idx]['content'].num_comments[idx2]),
                "media":str(df[idx]['content'].post_hint[idx2]),
                "medialink":str(df[idx]['content'].url[idx2]),
                # "length":countWords(analyse)
        })
    print(idx)

# print(interestingcomments['interestingcomments'][3])


#%%

# data = json.loads(f.read())
allfiles = pd.json_normalize( interestingcomments, record_path=['interestingcomments'])
removedDuplicates = allfiles.drop_duplicates()
removedDuplicates.shape





#%%








test = "blaaaa ( blaaaaa) ' blaaaaa ' https://www.ritter-sport.com/long-term-partnerships .. ."


len(test)

doc = nlp(test)

len(doc)
i=0

# %%
removedDuplicates.groupby('suborigin').count()

# %%
Redd = removedDuplicates.loc[removedDuplicates["suborigin"] == 'nan']

Redd.tail()
# %%

test='https://www.reddit.com/r/arduino/comments/mjtu'



print()
# %%


def RemoveNum(test):
    return(test.split('/')[4])


Redd['suborigin'] = Redd['link'].apply(RemoveNum)

Redd.head()
# %%

new = Redd = removedDuplicates.loc[removedDuplicates["suborigin"] != 'nan']

corecorp = pd.concat([new,Redd])

corecorp.groupby('suborigin').count()
# %%

corecorp.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/ReditCore.csv')
# %%



doc1 = nlp("I shit in the shower.")
# doc2 = nlp("I invented a new machine")
doc2 = nlp("To help myself, I created a Map Editor system based on WordPress a few years ago, and photography friends also got interested and started using it.")
doc1.similarity(doc2)
# %%
