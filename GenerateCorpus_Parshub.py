
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
#Parshub
#Structure:
# "Post": [
#   {
#    "name": "Weathering with precautions",
#    "url": "https://devpost.com/software/weathering-with-precautions",
#    "Likes": "0",
#    "Comments": "0",
#    "Description": "Inspiration - to help peoples to save them from weather damage\nWhat it does- it helps to know the right weather to us and get ready for the precautions\nHow we built it - By using knowledge of c , c++ and java\nChallenges we ran into- lots of challenges like time saving , errors\nAccomplishments that we're proud of\nWhat we learned-too much knowledge\nWhat's next for Weathering with precautions --many more to do this for make it better"
#   },

datapath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_devpost.json'


with open(datapath, 'r') as f:
        jsonFile = json.loads(f.read())
res= pd.json_normalize(jsonFile,record_path=['Post'])
res.head()

#%%
res.shape
#%%

df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in res.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.name,
         "date":'nan', 
         "content":row.Description,
         "link":row.url,
         "origin": 'Devpost',
         "suborigin": 'Devpost',
         "removed":"Nan",
         "score":row.Likes,
         "comments":row.Comments,
         "media":'nan',
         "medialink":'nan',
         "identifyer":idx+3000000
    })


#df = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv',dtype={"Unnamed: 0": int, "autor": "string","date": "float64","content": "string","link": "string","origin": "string","suborigin": "string","removed": "string","score": "string","comments": "string","media": "string","medialink": "string","identifyer": "int64"})
# df.head()
#dtype={"Unnamed: 0": int, "autor": "string","date": "float64","content": "string","link": "string","origin": "string","suborigin": "string","removed": "string","score": "string","comments": "string","media": "string","medialink": "string","identifyer": "int64"}
# df.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/test.csv',)


#%%
AnalyseFile= pd.DataFrame(data=Corpus)
AnalyseFile.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv')
AnalyseFile.head()



#-––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# "Category": [
#   {
#    "Category_Name": "Forestry Forum Pod Casts",
#    "Thread": [
#     {
#      "Threadname": "Podcast",
#      "Post": [
#       {
#        "Body": "I would listen to a podcast for sure. This Newbie needs a lot of help learning.",
#        "Author": "Kemp",
#        "Date": "« on: February 13, 2019, 04:34:47 AM »"
#       },
#       {
#        "Body": "Yeah, sounds like a great idea!",
#        "Author": "dltimbertech",
#        "Date": "« Reply #1 on: February 19, 2019, 01:46:23 PM »"
#       },
#       {
#        "Body": "Thats two",
#        "Author": "Kemp",
#        "Date": "« Reply #2 on: February 19, 2019, 03:16:24 PM »"
#       },
#       {
#        "Body": "I’m another for that route. Heck, I would be inclined to participate and talk but I don’t know if I would have anything pertinent to say, just a slightly different way of looking at life. But I’m still here (for now)!\nAfter all, who wants to hear from someone with a 25yr background in selling automotive and equipment parts? Automotive, I was top notch. Equipment, I would like to think I was a rookie at best!\nBut the customers like me because of attitude. That can’t be taught. Learned, yes. You just have to pay attention.\nTwo ears and one mouth. God gave us this as a reminder: listen twice as much as you talk! Easy to see, but hard to teach. Just be humble.\nI’m far, FAR from being a preacher, my life is to “colorful” for that. But my father-in-law is. He knows my life and doesn’t look down on me. I’ve asked for his ear and he’s willing to give it. And he’s asked for advice on a few things that I know about that are specialized and I give it to him. In fact, they are planning to come up from MS next weekend. Maybe they will come up close to Magic Man, but we’ll not count on the planets being in perfect alignment. But a man can dream!",
#        "Author": "Tacotodd",
#        "Date": "« Reply #3 on: January 11, 2021, 02:10:11 AM »"
#       },
#       {
#        "Body": "Hi there, can you guide me a little bit? I really want to listen to the podcast, but I can't find it.",
#        "Author": "stillc",
#        "Date": "« Reply #4 on: April 05, 2021, 12:01:36 AM »"
#       },
#       {
#        "Body": "I’m just wondering if @jeff is seeing this. I know he is, but no response as of yet.",
#        "Author": "Tacotodd",
#        "Date": "« Reply #5 on: April 05, 2021, 12:43:15 AM »"
#       },
#       {
#        "Body": "I'm strongly considering something a step up from a podcast, but too much on my plate at the moment to dive into it, but id strongly suggest following and getting subscribed to the Forestry Forum youtube channel",
#        "Author": "Jeff",
#        "Date": "« Reply #6 on: April 05, 2021, 11:42:02 AM »"
#       },
#       {
#        "Body": "10-4! Message received & understood!",
#        "Author": "Tacotodd",
#        "Date": "« Reply #7 on: April 05, 2021, 04:11:20 PM »"
#       }
#      ]
#     },

#Body, Author, Date, 



#%%
datapath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_Forestry_hopefullywithurl.json'


with open(datapath, 'r') as f:
        jsonFile = json.loads(f.read())
res= pd.json_normalize(jsonFile,record_path=['Category'])
res.head()



#%%

print(len(jsonFile['Category']))
print(jsonFile['Category'][0]['Category_Name'])

# print(jsonFile['Category'][0]['Thread'][0]['Post'])
#%%
Corpus=[]
for idx, file in enumerate(jsonFile['Category']):
    suborigin = file['Category_Name']
    print(suborigin)
    try:
        for idx2, thread in enumerate(file['Thread']):
            # print(len(thread['Post']))
            for idx3, post in enumerate(thread['Post']):
                try:
                    autor = post['Author']
                except Exception as e:
                    autor='Nan'
                try:
                    content = post['Body'],
                except Exception as e:
                    content = 'Nan'
                try:
                    link = post['Link_url'],
                    date = post['Date'],
                except Exception as e:
                    link = 'Nan'
                    date = 'Nan'

                Corpus.append({
                    "autor": autor,
                    "date":date, 
                    "content":content,
                    "link":link,
                    "origin": 'Forestry',
                    "suborigin": suborigin,
                    "removed":"Nan",
                    "score":'Nan',
                    "comments":'Nan',
                    "media":'nan',
                    "medialink":'nan',
                    "identifyer":idx+4000000
                })
    except Exception as e:
        print('none')
print('done')



#%%

print(len(Corpus))
#%%
res.shape
#%%

df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in res.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.name,
         "date":'nan', 
         "content":row.Description,
         "link":row.url,
         "origin": 'Devpost',
         "suborigin": 'Devpost',
         "removed":"Nan",
         "score":row.Likes,
         "comments":row.Comments,
         "media":'nan',
         "medialink":'nan',
         "identifyer":idx+3000000
    })







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
new.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/Forestry.csv')
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





#%%

df = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv')
df.head()
# %%
df.dtypes
# %%
 
