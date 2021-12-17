

#%%
from os.path import isfile, join
from os import listdir
from os import walk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.ticker as ticker
import json
from pandas import date_range, Series
import os
import re
import numpy as np
from datetime import datetime
import pandas as pd


#%%
path = "/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Trend/Github/selectedGithub.csv"
data = pd.read_csv(path)

#%%
data.head()
#%%
path = "/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost_Core.json"
with open(path, 'r') as f:
        jsonFile = json.loads(f.read())
data= pd.json_normalize(jsonFile,record_path=['interestingcomments'])
data.head()

# %%
def PDDate(Daylie):
    try:
        return pd.to_datetime(Daylie)
    except Exception as e:
        return pd.to_datetime('Nov 20, 2021')


data['date'] = data['date'].apply(PDDate)


# %%
data.head()
# %%
pattern = '\d\d\d\d'


def YearlyDate(Daylie):
    test_string = str(Daylie)
    date = re.findall(pattern, test_string)
    try:
        return str(date[0])
    except Exception as e:
        return None

data['year'] = data['date'].apply(YearlyDate)
data.head()
dates = data.groupby('year').count()
dates.head(15)

#%%
newdata = data[360000:]

#%%
data.shape
# %%
SelectedP = data.loc[data["result"] == True]
SelectedP.shape
# %%


# %%
words = SelectedP.groupby('selectorShort').count()
index = words.index
w_list = list(index)
print(w_list)


# %%
# iterating the columns
dates = SelectedP.groupby('year').count()
index = dates.index
a_list = list(index)
print(a_list)
# %%

# %%
files = SelectedP.groupby('suborigin').count()
test = files.index
s_list = list(test)
print(s_list)



# %%
Name = "ReddSortedOut"
Output = SelectedP
interestingcommment = {}
interestingcommment["interestingcomments"] = []

folder = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Reddit/Selected_Posts_Round2/'


for sub in s_list:
    redpath = folder+sub.replace("/", "_")
    print(redpath)
    os.mkdir(redpath)
    for item in a_list:
        for word in w_list:
            Name = word+sub+item
            Df_00 = Output.loc[Output["selectorShort"] == word]
            Df_01 = Df_00.loc[Df_00["year"] == item]
            Df_File = Df_01.loc[Df_01["suborigin"] == sub]
            interestingcommment = {}
            interestingcommment["interestingcomments"] = []
            if Df_File.shape[0] > 0:
                with open(redpath+'/'+Name+'.json', 'w') as outfile:
                    filetojson = Df_File.to_json(orient="records")
                    interestingcommment["interestingcomments"] = json.loads(
                        filetojson)
                    interestingcommment['name'] = Name
                    json.dump(interestingcommment, outfile)

# %%
SelectedP.shape
# %%
data.shape
# %%


#
# %%
Name = "ReddSortedOut"
Output = SelectedP
interestingcommment = {}
interestingcommment["interestingcomments"] = []

folder = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Trend/Github/Github/'

for sub in s_list:
    redpath = folder+sub
    print(redpath)
    os.mkdir(redpath)
    for word in w_list:
        Name = word+sub
        Df_00 = Output.loc[Output["selectorShort"] == word]
        Df_File = Df_00.loc[Df_00["suborigin"] == sub]
        interestingcommment = {}
        interestingcommment["interestingcomments"] = []
        if Df_File.shape[0] > 0:
            with open(redpath+'/'+Name+'.json', 'w') as outfile:
                filetojson = Df_File.to_json(orient="records")
                interestingcommment["interestingcomments"] = json.loads(
                    filetojson)
                interestingcommment['name'] = Name
                json.dump(interestingcommment, outfile)

# %%
