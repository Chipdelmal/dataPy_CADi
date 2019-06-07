# -*- coding: utf-8 -*-

###############################################################################
# "Word-Ladder"
###############################################################################
#  Objectives:
#   To show some of scipy capabilites and do a basic "data-cleaning" exercise
#  Source:
#   https://docs.scipy.org/doc/scipy/reference/tutorial/csgraph.html
#   https://sudonull.com/posts/756-SciPy-graph-algorithms
#   https://www.geeksforgeeks.org/python-string-isalpha-application/
###############################################################################

###############################################################################
# Import libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import wordLadderAux as aux
from scipy.sparse.csgraph import dijkstra
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
%matplotlib inline

###############################################################################
# User inputs
n = 4
(start, end) = ("apex", "more")

###############################################################################
# Import libraries
word_list = open('/usr/share/dict/words').readlines()
word_list[:5]

###############################################################################
# Auxiliary function created to clean the strings
word_list = aux.cleanStrings(word_list, n)
len(word_list)
###############################################################################
# Convert list to array
word_list = np.asarray(word_list)
word_list.sort()
word_list[:10]

###############################################################################
# Convert into numbers and get only the first byte from each character
word_bytes = np.ndarray(
    (word_list.size, word_list.itemsize),
    dtype='int8',
    buffer=word_list.data
)
word_bytes.shape
word_bytes = word_bytes[:, ::word_list.itemsize//n]

###############################################################################
# Calculate the Hamming distance between elements
hamming_dist = pdist(word_bytes, metric='hamming')
graph = csr_matrix(squareform(hamming_dist < 1.001 / n))

###############################################################################
# Plot the sparse matrix
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(1, 1, 1)
# ax.matshow(graph.toarray(), cmap=plt.cm.binary)

###############################################################################
# Do the minimum distance path between words
(i1, i2) = map(word_list.searchsorted, [start, end])
(distances, predecessors) = dijkstra(
    graph,
    indices=i1,
    return_predecessors=True
)

###############################################################################
# Do the minimum distance path between words
(path, i) = ([], i2)
while i != i1:
    path.append(word_list[i])
    i = predecessors[i]
path.append(word_list[i1])
path.reverse()
print(path)
