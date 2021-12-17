
#%%

import gensim
import pandas as pd
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, Phraser
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec

from gensim.models import Word2Vec

from sklearn.manifold import TSNE
import re
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# define training data

#%%
model = Word2Vec.load("/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Word2Vec/Core5e.model")


#%%
df = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/ReditCore.csv')
df.head()


#%%
removed = df.dropna(subset=['content'])  #remove all Rows whitout content
content = removed.content.apply(gensim.utils.simple_preprocess) # preprocess the data for the Word2Vec training. It tokenizes all the words and sets them to lower case


#%%
print(content[0])

# %%
model = gensim.models.Word2Vec(
    window = 10, # how many words bevore and after are used for training
    min_count = 2, #min words per sentence
    workers= 6
)
model.build_vocab(content, progress_per=1000)
model.corpus_count

#%%
model.epochs
#%%
model.train(content, total_examples=model.corpus_count, epochs=5)

# %%

model.save('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Word2Vec/Core5e.model')


# %%



words = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Words/wordskerngeschäft.csv')
words.head()

#%%

tool = words.loc[words["Tags"] == 'tool']

tool.head()

#%%

model.wv.most_similar('tool', topn=10)

#%%

model.wv.similar_by_word('plant', topn=10)

#%%

Words = []

for toolname in tool.itertuples():
    print(toolname.Name)
    try:
        result=model.wv.most_similar(str(toolname.Name), topn=10)
        additionalwords = []
        for word in result:
            additionalwords.append(word[0])
            print(word[0])
        Words.append({
           "word":toolname.Name,"mostsimilar":additionalwords})
    except Exception as e:
        print(e)
        Words.append({
           "word":toolname.Name,"mostsimilar":"nan"})
#     Words.append()

# print(len(Words))

# %%

print(Words[0])


# %%
Toolwords = pd.DataFrame(data=Words)
Toolwords.tail()
# %%

Toolwords.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Words/Tools.csv')
# %%
vocab = list(model.wv.key_to_index)
X = model.wv[vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.key_to_index)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()



# %%

vocab = list(model.wv.key_to_index)
X = model.wv[vocab]
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)
df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])

for word, pos in df.iterrows():
    ax.annotate(word, pos)

# plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.show()
# %%
