#%%
import gensim
import pandas as pd
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, Phraser


#%%
df = pd.read_csv('YourDataCorpus')
df.head()


#%%
removed = df.dropna(subset=['content'])  #remove all Rows whitout content
content = removed.content.apply(gensim.utils.simple_preprocess) # preprocess the data for the Word2Vec training. It tokenizes all the words and sets them to lower case 