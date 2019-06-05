
def cleanStrings(rawList):
    cleanList = map(str.strip, rawList)
    cleanList = [word for word in cleanList if len(word) == 3]
    cleanList = [word for word in cleanList if word[0].islower()]
    cleanList = [word for word in cleanList if word.isalpha()]
    cleanList = list(map(str.lower, cleanList))
    return cleanList
