# https://docs.scipy.org/doc/scipy/reference/tutorial/csgraph.html
# https://www.geeksforgeeks.org/python-string-isalpha-application/

from scipy.optimize import minimize


word_list = open('/usr/share/dict/words').readlines()
word_list[:5]

word_list = map(str.strip, word_list)
word_list = [word for word in word_list if len(word) == 3]
word_list = [word for word in word_list if word[0].islower()]
word_list = [word for word in word_list if word.isalpha()]
word_list = list(map(str.lower, word_list))
