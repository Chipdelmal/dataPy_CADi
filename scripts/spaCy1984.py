# -*- coding: utf-8 -*-

###############################################################################
# "spaCy1984" demo
###############################################################################
#  Objectives:
#   Reading a text with spaCy and doing some basic text processing
#  Sources:
#   https://spacy.io/usage/examples
#   https://programminghistorian.org/en/lessons/counting-frequencies
#   https://stackoverflow.com/questions/45080698/make-frequency-histogram-from-list-with-tuple-elements
###############################################################################

%matplotlib inline
import spacy
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
nlp = spacy.load("en_core_web_sm")

file = open('../data/extracted/1984/1984.txt', mode='r')
lines = file.read().splitlines()
fullTxt = ' '.join(lines)

doc = nlp(fullTxt)
nouns = [chunk.text for chunk in doc.noun_chunks]
nouns[:10]


verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
verbs[:10]

unique_words = set(verbs)
counts = []
for words in unique_words:
    counts.append(verbs.count(words))

sns.lineplot(x=range(len(counts)),y=sorted(counts, reverse=True))


zipped = zip(unique_words, counts)
sortedList =  sorted(zipped, key=lambda x: x[1], reverse=True)

subsetList = sortedList[:25]
word, frequency = zip(*subsetList)
indices = np.arange(len(subsetList))
plt.bar(indices, frequency, color='r')
plt.xticks(indices, word, rotation='vertical')
plt.tight_layout()
plt.show()
