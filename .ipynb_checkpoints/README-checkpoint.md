Digital Lead User Analysis with Spacy and Gensim

1. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

2. Install all necessary requirements

```
pip3 install . -r requirements.txt
```

Depending on which system you are working - Windows/[Linux,Mac] - you have to change the Spacy Model you are working with.
You seperately have to download the spacy English model. We used the en_core_web_md modell

```
python -m spacy download en_core_web_md modell
```

## 0.Prepare your data corpus

We used date from different forum like reddit, github, devpost, twitter to collect subject specific data.
To use the Matcher you should use the following format for your data. In this[comming soon] series we will explain how we collected the data and formated the corpus.

<table><tbody><tr><th>origin</th><th>suborigin</th><th>autor</th><th>link</th><th>content</th><th>date</th><th>length</th><th>media</th><th>medialink</th><th>score</th></tr><tr><td>Reddit</td><td>r/photography</td><td>MrCornau</td><td>https://</td><td>UsergeneratedContent goes here</td><td> timestamp</td><td>wordcount</td><td>is there Media in the UGC</td><td>link to that media</td><td>Score/Likes/etc.</td></tr></tbody></table>

## 1. Word 2 Vec

Create a Word 2 Vec Model to find word embeddings in your data corpus. Therefore we used Gensim.

```
import gensim
import pandas as pd
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, Phraser

df = pd.read_csv('YourFile.csv')

```

At First we prepared our data

```
#remove all rows of the datacorpus whitout content
removed = df.dropna(subset=['content'])

# Preprocess the data for the Word2Vec training. It tokenizes all the words and sets them to lower case.
content = removed.content.apply(gensim.utils.simple_preprocess)

#This outputs following structure. From every sentence a list is generated. Each word is saved seperately as a token. Also the punktuation and unnecessary words like 'a' have been removed, as they are not important for the vord2vec model.
['my', 'germination', 'process', 'is', 'so', 'far', 'so', 'good', 'next', 'step', 'is', 'to', 'transplant', 'into', 'soil']

```

Following we set up the gensim modle

```
model = gensim.models.Word2Vec(
    window = 10, # how many words bevore and after are used for training
    min_count = 2, # min words per sentence
    workers= 6 #defines the cores of your machine which are used seperately, if you have only 4 use 4
)

model.build_vocab(content, progress_per=1000)

```

Train the Model

```
model.train(content, total_examples=model.corpus_count, epochs=model.epochs)
```

Save the model for later use

```
model.save('YOURFILEPATH.model')
```

Use the Model to find similar words in your context

```
model.wv.most_similar('diy')
```
