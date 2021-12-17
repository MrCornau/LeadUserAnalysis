
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

# %%
nlp = spacy.load("en_core_web_md")

# %%
df = pd.read_csv(
    '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/Toolsinaction.csv', lineterminator='\n')
df.head()


# %%
df.shape

# doc = nlp("I used a Hedge Trimmer lastly. Also i haaad a big big wrench")
# matches = Toolmatcher(doc)


# for match_id, start, end in matches:
#  span = doc[start:end]
#  print(span.text)


# %%

SubjectMatcher = PhraseMatcher(nlp.vocab, attr="LOWER")
SubjectsSpecificWords = ['tool', 'tool', 'drilling machine', 'chain saw', 'wood cutter', 'hedge trimmer', 'axe', 'estwing', 'spokeshave', 'klopp', 'sbt', 'igorot', 'rehandle', 'metalwork', 'wiss', 'hatchet', 'gague', 'excavator', 'lovechild', 'alaskan', 'antique', 'estwing', 'deermanagement', 'ibanez', 'lawnmower', 'rider', 'toro', 'mowers', 'tractor', 'snapper', 'mowr', 'propelled', 'hustler',
                         'chainsaw',
                         'rock cutter',
                         'cut-off machine',
                         'cut-off saw',
                         'high pruner',
                         'power saws',
                         'hedge trimmers',
                         'hedge cutter',
                         'wood trimmer',
                         'hatchet',
                         'axe',
                         'mower',
                         'lawn mower',
                         'garden shears',
                         'branch saws',
                         'loppers',
                         'forestry tools',
                         'protective equipment',
                         'garden shredder',
                         'lawn trimmer',
                         'power scythes',
                         'freischneider',
                         'robotic mower',
                         'rasenmäher',
                         'mulching lawn mower',
                         'lawn aerator',
                         'scarifier',
                         'motor hoes',
                         'power hoes',
                         'power tillers',
                         'ride-on mower',
                         'riding mower',
                         'earth drilling rigs',
                         'sprayers', 'wrench']

SubjectPattern = [nlp(Subject) for Subject in SubjectsSpecificWords]

SubjectMatcher.add("FRUIT_PATTERN", SubjectPattern)


# %%

InventionMatcher = Matcher(nlp.vocab)
Personal = Matcher(nlp.vocab)
IdeaMatcher = Matcher(nlp.vocab)
TestMatcher = Matcher(nlp.vocab)
SortouttMatcher = Matcher(nlp.vocab)


ToolWords = ['tool', ]


speak_lemmas0 = ['i', 'we', 'us', 'me', 'our',
                 'my', 'I', 'We', 'Us', 'Me', 'Our', 'My']
speak_lemmas1 = ['invent', 'design', 'introduce', 'create', 'develop', 'build'
                 'improve', 'diye', 'engineer', 'develope', 'make', 'prototype']
innovationverb = [
    {"POS": "PRON", "LEMMA": {"IN": speak_lemmas0}},
    {"POS": "AUX",  "OP": "*"},
    {"POS": "VERB",  "OP": "*"},
    {"POS": "PART",  "OP": "*"},
    {"POS": "ADV",  "OP": "*"},
    {"LEMMA": {"IN": speak_lemmas1}},
]

# nouns
diywords = ['diy', 'prototyp']
diy = [
    {"POS": "PROPN", "LEMMA": {"IN": diywords}},
    {"POS": "PUNCT", "OP": "*"},
    {"POS": "NOUN", "LEMMA": "project", "OP": "*"},
]

test = [{
    "LOWER": {"IN": ['diy', 'prototyp']}
}]

Nouns = ['creation', 'invention', 'enhancement']
InnovationNouns = [
    {"POS": "PRON", "LEMMA": {"IN": speak_lemmas0}},
    {"POS": "ADJ", "OP": "*"},
    {"LOWER": {"IN": Nouns}},
]

cameUpWith = [
    {"POS": "VERB", "LEMMA": "come"},
    {"POS": "ADP", "LEMMA": "up"},
    {"POS": "ADP", "LEMMA": "with"},
]

Sent_start_Word = ['create', 'design', 'develop', 'engineer', 'improve']
Sent_start = [
    {"POS": "VERB", "LEMMA": {"IN": Sent_start_Word}, "IS_SENT_START": True},
]

# Do it yourself
diy2 = [
    {"LEMMA": "do"}, {"LEMMA": "it"},
    {"LEMMA": "yourself"},
]

# DIYed
pattern3d = [
    {"LEMMA": "3d"},
    {"POS": "PUNCT", "OP": "*"},
    {"LEMMA": "print"},
]


PersonalMatcher = [{"POS": "VERB", "LEMMA": {"IN": speak_lemmas1}}, ]
Idea = [{"LEMMA": "idea"}, ]

InventionMatcher.add("InventionMatcher", [diy2, pattern3d, InnovationNouns, cameUpWith,
                     Sent_start, innovationverb, test])
Personal.add("InventionMatcher2", [PersonalMatcher])
IdeaMatcher.add("Idea", [Idea])

# Sourtout_Words = [{
#     "LEMMA": {"IN": ['skill', 'film', 'video', 'role', 'roll', 'repair', 'tutorial', 'remedy']}
# }]

# SortouttMatcher.add('testmatcher', [Sourtout_Words])
# TestMatcher.add('testmatcher', [Sourtout_Words])


# # %%

# test = ['I made a picture of my rock cutter',
#         'We developed all films from the shoot last']


# for sent in test:
#     nlpContent = nlp(sent.lower_)
#     print(matcherFunctions.singlesearch(SubjectMatcher, nlpContent))
#     # print(matcherFunctions.doublesearch(IdeaMatcher, Personal, nlpContent))

# # matcherFunctions.singlesearch(InventionMatcher, nlp(test[0].lower()))):


# %%


# %%
print(df.shape)
removed = df.drop_duplicates(subset=['content'])
removed.shape
# %%
removed.at[3, 'content'] = 'I have created a new kind of garden.'


# %%
removed.head()

# %%


def Match(content):

    matcher = False
    sortedWord = None
    markedSent = None
    result = matcherFunctions.singlesearch(
        SubjectMatcher, str(content))
    # print(result)
    if(result['detected']):
        InnovationResult = matcherFunctions.singlesearch(
            InventionMatcher, str(content))
        if(InnovationResult['detected']):
            matcher = True
            selector = InnovationResult['word1']
            selectorShort = InnovationResult['word1'][-1].lemma_
            markedSent = InnovationResult['markedSent']
        else:
            InnovationResult = matcherFunctions.doublesearch(
                IdeaMatcher, Personal, content)
            if(InnovationResult['detected']):
                selector = [InnovationResult['word1'],
                            InnovationResult['word2']]
                selectorShort = InnovationResult['word1'][-1].lemma_
                matcher = True
                markedSent = InnovationResult['markedSent']
            else:
                matcher = False
                selector = None
                selectorShort = None
    else:
        matcher = False
        selector = None
        selectorShort = None

    # if(matcher):

    #     sortedOut = matcherFunctions.singlesearch(
    #         SortouttMatcher, result['sent'])
    #     if(sortedOut['detected']):
    #         matcher = False
    #         markedSent = sortedOut['markedSent']
    #         sortedWord = sortedOut['word1'][-1].lemma_

    return {"Matcher": matcher, "Selector": str(selector), "selectorShort": str(selectorShort), "MarkedSent": str(markedSent), "sortedWord": str(sortedWord)}


interestingcommment = {}
interestingcommment["interestingcomments"] = []
counter = 0
Newfile = []
df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin', 'result', 'Selector', 'selectorShort', 'MarkedSent', 'sortedWord', 'removed', 'score', 'comments', 'media', 'medialink', 'identifyer'
                            ])
for idx, row in removed.iterrows():
    newrow = []
    # print(idx)
    MatchResults = None
    newrow.append(row)
    # print('analysed ', idx, 'from:',
    #       df.shape[0], '  Progress:', round(100/df.shape[0]*idx, 0), '%')
    MatchResults = Match(row['content'])
    newrow.append(MatchResults)

    df3.loc[idx] = [row.autor, row.date, row.content,
                    row.link, row.origin, row.suborigin, MatchResults['Matcher'], MatchResults['Selector'], MatchResults['selectorShort'], MatchResults['MarkedSent'], MatchResults['sortedWord'], row.removed, row.score, row.comments, row.media, row.medialink, row.identifyer]
    if(counter == 1000):
        counter = 0
        df3.to_csv(
            '/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/ToolsInAction.csv')

    counter += 1


# %%
df3.shape
# %%

df3.groupby('result').count()
# df3.head()
# %%
Selected = df3.loc[df3["result"] == True]


# %%
df3.to_csv(
    '/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/ForestryAnalysed.csv')


# %%
with open('Core_Twitter_Selected.json', 'w') as outfile:
    ad = Selected.to_json(orient="records")
    interestingcommment["interestingcomments"] = json.loads(ad)
    interestingcommment['name'] = 'Matchertest'
    json.dump(interestingcommment, outfile)

# %%
print(eval(Selected.loc[6695, 'autor'])['username'])
# %%


def GetUsername(username):
    return eval(username)['username']
    # return(test.split('/')[4])


Selected['autor_infomation'] = Selected['autor']

# Selected['autor']
Selected['autor'] = Selected['autor'].apply(GetUsername)

Selected.head()

# %%


# %%
with open('Core_Twitter_Selected.json', 'w') as outfile:
    ad = Selected.to_json(orient="records")
    interestingcommment["interestingcomments"] = json.loads(ad)
    interestingcommment['name'] = 'Matchertest'
    json.dump(interestingcommment, outfile)

# %%
