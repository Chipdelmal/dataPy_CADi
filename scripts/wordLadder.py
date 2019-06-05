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
import numpy as np
import wordLadderAux as aux
from scipy.sparse.csgraph import dijkstra
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix

###############################################################################
# Import libraries
word_list = open('/usr/share/dict/words').readlines()
word_list[:5]

word_list = aux.cleanStrings(word_list)
len(word_list)

word_list = np.asarray(word_list)
word_list.sort()
word_list.dtype


word_bytes = np.ndarray(
    (word_list.size, word_list.itemsize),
    dtype='uint8',
    buffer=word_list.data
)
word_bytes = word_bytes[:, ::word_list.itemsize//3]
word_bytes.shape

hamming_dist = pdist(word_bytes, metric='hamming')
graph = csr_matrix(squareform(hamming_dist < 1.5 / 3))

i1 = word_list.searchsorted('ape')
i2 = word_list.searchsorted('man')


distances, predecessors = dijkstra(
    graph,
    indices=i1,
    return_predecessors=True
)
print(distances[i2])


path = []
i = i2
while i != i1:
    path.append(word_list[i])
    i = predecessors[i]
path.append(word_list[i1])
print(path[::-1])
