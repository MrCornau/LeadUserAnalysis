
# %% Final Pattern

import pandas as pd
from spacy.matcher import Matcher
import spacy
import matcherFunctions
import re
import numpy as np
from imp import reload
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.ticker as ticker
import json
from spacy.matcher import PhraseMatcher


# %%
reload(matcherFunctions)

#%%
nlp = spacy.load("en_core_web_md")

# %%
df = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Trend/Reddit/Phase_2.csv', lineterminator='\n')
df.head()


#%%
df.shape

# doc = nlp("I used a Hedge Trimmer lastly. Also i haaad a big big wrench")
# matches = Toolmatcher(doc)


# for match_id, start, end in matches:
#  span = doc[start:end]
#  print(span.text)




#%%

SubjectMatcher = PhraseMatcher(nlp.vocab, attr="LOWER")
SubjectsSpecificWords = ['garden','outdoor','tree','grass','lawn','trunk','branch','leaf','forestry','harvesting','tool','tool','drilling machine','chain saw','wood cutter','hedge trimmer','axe', 'estwing', 'spokeshave', 'klopp', 'sbt', 'igorot', 'rehandle', 'metalwork', 'wiss', 'hatchet', 'gague', 'excavator', 'lovechild', 'alaskan', 'antique', 'estwing', 'deermanagement', 'ibanez','lawnmower', 'rider', 'toro', 'mowers', 'tractor', 'snapper', 'mowr', 'propelled', 'hustler',
'chainsaw','rock cutter', 'cut-off machine', 'cut-off saw', 'high pruner', 'power saws', 'hedge trimmers', 'hedge cutter', 'wood trimmer', 'hatchet', 'axe', 'mower', 'lawn mower','garden shears', 'branch saws', 'loppers','forestry tools','protective equipment',
'garden shredder','lawn trimmer','power scythes', 'robotic mower', 'mulching lawn mower', 'lawn aerator', 'scarifier', 'motor hoes', 'power hoes', 'power tillers', 'ride-on mower', 'riding mower', 'earth drilling rigs', 'sprayers','wrench','harvesting','sapling','stump','bush','shrub','pines','branches','tress','dogwood','conifer','backyard','gardens','yard','patio','plot','beds','flowerbed','bed','planter','farming','shrub','prune']


SubjectPattern = [nlp(Subject) for Subject in SubjectsSpecificWords]

SubjectMatcher.add("SubjectPattern", SubjectPattern)



# %%
print(df.shape)
removed = df.drop_duplicates(subset=['content'])
removed.shape


#%%
removed.head()


#%%

NewNew = removed
identifyer = []
for idx, row in removed.iterrows():
    identifyer.append(idx+3500000)

print(len(identifyer))
# NewNew.head()

# %%
removed['identifyer'] = identifyer
removed.head()



# %%


def Match(content):

    matcher = False
    sortedWord = None
    markedSent = None
    result = matcherFunctions.singlesearch(
        SubjectMatcher, str(content))
    
    if(result['detected']):
        matcher = True
        selector = result['word1']
        selectorShort = result['word1'][-1].lemma_
        markedSent = result['markedSent']
    else:
        matcher = False
        selector = None
        selectorShort = None
    
    return {"Matcher": matcher, "Selector": str(selector), "selectorShort": str(selectorShort), "MarkedSent": str(markedSent), "sortedWord": str(sortedWord)}


interestingcommment = {}
interestingcommment["interestingcomments"] = []
counter = 0
Newfile = []
df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin', 'result', 'Selector', 'selectorShort', 'MarkedSent', 'sortedWord','removed','score','comments','media','medialink','identifyer'
                            ])
#for idx, row in removed.iloc[5000:].iterrows():
for idx, row in removed.iloc[:5000].iterrows():
    newrow = []
    # print(idx)
    MatchResults = None
    newrow.append(row)
    # print('analysed ', idx, 'from:',
    #       df.shape[0], '  Progress:', round(100/df.shape[0]*idx, 0), '%')
    MatchResults = Match(row['content'])
    newrow.append(MatchResults)

    df3.loc[idx] = [row.autor, row.date, row.content,
                    row.link, row.origin, row.suborigin, MatchResults['Matcher'], MatchResults['Selector'], MatchResults['selectorShort'], MatchResults['MarkedSent'], MatchResults['sortedWord'],row.removed,row.score,row.comments,row.media,row.medialink,row.identifyer]
    if(counter == 1000):
        counter = 0
        with open('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Trend/Reddit/Phase_1_3.json', 'w') as outfile:
            ad = df3.to_json(orient="records")
            interestingcommment["interestingcomments"] = json.loads(ad)
            interestingcommment['name'] = 'Matchertest'
            json.dump(interestingcommment, outfile)
        print('1000')
    counter += 1



#%%
with open('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Trend/Reddit/Phase_1_3.json', 'w') as outfile:
    ad = df3.to_json(orient="records")
    interestingcommment["interestingcomments"] = json.loads(ad)
    interestingcommment['name'] = 'Matchertest'
    json.dump(interestingcommment, outfile)
#%%
df3.shape
#%%

df3.groupby('result').count()
# df3.head()
#%%
Selected=df3.loc[df3["result"] == True]


#%%
Selected.to_csv('selectedTwitter.csv')


# %%
with open('Core_Twitter_Selected.json', 'w') as outfile:
    ad = Selected.to_json(orient="records")
    interestingcommment["interestingcomments"] = json.loads(ad)
    interestingcommment['name'] = 'Matchertest'
    json.dump(interestingcommment, outfile)

# %%
print(eval(Selected.loc[6695,'autor'])['username'])
#%%

def GetUsername(username):
    return eval(username)['username']
    # return(test.split('/')[4])

Selected['autor_infomation'] = Selected['autor']

# Selected['autor']
Selected['autor']= Selected['autor'].apply(GetUsername)

Selected.head()

# %%


# %%
with open('Core_Twitter_Selected.json', 'w') as outfile:
    ad = Selected.to_json(orient="records")
    interestingcommment["interestingcomments"] = json.loads(ad)
    interestingcommment['name'] = 'Matchertest'
    json.dump(interestingcommment, outfile)

# %%

