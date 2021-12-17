
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


nlp = spacy.load("en_core_web_md")

#%%
datapath = '/Users/joshcornau/Code/SpaCy_FirstModel/Big_Data/Photrio_Format.json'


#%%
mypath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Twitter_Core/'
Paths = []
for (dirpath, dirnames, filenames) in walk(mypath):

    for file in filenames:
        if file.endswith('.json'):
            Paths.append(file)
    break

print(Paths)


#%%

List = []
for idx, File in enumerate(Paths):
    path = mypath+File
    res = pd.read_json(path, lines=True)
    List.append(res
    )

#%%
alltweets= pd.concat(List)
alltweets.shape
#%%

df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in alltweets.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.user,
         "date":row.date, 
         "content":row.renderedContent,
         "link":row.url,
         "origin": 'Twitter',
         "suborigin": row.hashtags,
         "removed":"Nan",
         "score":row.likeCount,
         "comments":row.replyCount,
         "media":row.media,
         "medialink":row.media,
         "identifyer":row.id
    })
#%%
print(len(Corpus))
# df3.shape
#%%

new= pd.DataFrame(data=Corpus)
new.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/TwitterID_Full.csv')
new.head()
#%%
new.shape
#%%

#%%
def countWords(Analyse):
    doc = nlp(Analyse)
    i=0
    for token in doc:
        if(token.pos_ !='PUNCT'):
            i+=1
    return(i)

