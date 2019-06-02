# -*- coding: utf-8 -*-

###############################################################################
# "sentiment" example
###############################################################################
#  Objectives:
#   To test the Google Trends data retreival within Python
#  Sources:
#   https://pypi.org/project/tweet-preprocessor/
#   https://towardsdatascience.com/having-fun-with-textblob-7e9eed783d3f
###############################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import libraries
from textblob import TextBlob
import pandas as pd
import spacy
import seaborn as sns
import matplotlib.pyplot as plt
nlp = spacy.load("en_core_web_sm")
# python -m spacy download en_core_web_sm
# python -m textblob.download_corpora

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Load data
data = pd.read_csv(
    "../data/extracted/spaCy/verses.csv",
    header=None,
    names=["verse", "rating"]
)
versesList = list(data["verse"])

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Exploring
v = versesList[15]
blob = TextBlob(v)
blob.tags
blob.noun_phrases

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Exploring
polarities = []
subjectivities = []
for v in versesList:
    blob = TextBlob(v)
    (polarity, subjectivity) = blob.sentiment
    polarities.append(polarity)
    subjectivities.append(subjectivity)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Add the sentiments to the dataframe
data["polarity"] = polarities
data["subjectivity"] = subjectivities
data.to_csv("../data/extracted/spaCy/versesOut.tsv", sep='\t', index=False)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plotting Histograms
num_bins = 8
n, bins, patches = plt.hist(
    data.polarity, num_bins, facecolor='blue', alpha=0.5
)
plt.xlabel('Polarity')
plt.ylabel('Count')
plt.title('Histogram of polarity')
plt.savefig('./images/sentiment01.png', dpi=500)



plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(
    data.subjectivity, num_bins, facecolor='blue', alpha=0.5
)
plt.xlabel('Subjectivity')
plt.ylabel('Count')
plt.title('Histogram of subjectivity')
plt.savefig('./images/sentiment02.png', dpi=500)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plotting Distributions
sns.distplot(polarities)
sns.violinplot(polarities)
