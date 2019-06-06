
def cleanStrings(rawList, n=3):
    cleanList = map(str.strip, rawList)
    cleanList = [word for word in cleanList if len(word) == n]
    cleanList = [word for word in cleanList if word[0].islower()]
    cleanList = [word for word in cleanList if word.isalpha()]
    cleanList = list(map(str.lower, cleanList))
    return cleanList
