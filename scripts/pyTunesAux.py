from xml.etree.ElementTree import ElementTree
import os
from shutil import copyfile
from urllib.parse import unquote


def getSongsPaths(tree):
    songs = tree.findall('./dict/dict/dict/string')
    songsPaths = []
    for song in songs:
        if song.text[0:7] == "file://":
            myfile = unquote(song.text[7:])
            songsPaths.append(myfile)
    return(songsPaths)


def getSongsID(tree):
    songs = tree.findall('./dict/dict/')
    songsIds = []
    for song in songs:
        textId = song.text
        if (textId.isdigit()):
            songsIds.append(textId)
    return(songsIds)


def getSongsOrder(tree):
    songs = tree.findall('./dict/array/dict/array/dict/integer')
    ordersId = []
    for song in songs:
        ordersId.append(song.text)
    return(ordersId)


def getSongsDictionary(tree):
    sID = getSongsID(tree)
    sPA = getSongsPaths(tree)
    filenames = [i.split("/")[-1] for i in sPA]
    songsList = list(zip(sID, sPA, filenames))
    songsDict = {song[0]: [song[1], song[2]] for song in songsList}
    return(songsDict)


def getOrderedSongs(playlistXML):
    tree = ElementTree().parse(playlistXML)
    songsDict = getSongsDictionary(tree)
    sOR = getSongsOrder(tree)
    orderedSongs = [songsDict[i] for i in sOR]
    return(orderedSongs)


def getIOPaths(playlistXML, destiny, padSize=3):
    playlist = getOrderedSongs(playlistXML)
    listIO = []
    for (i, song) in enumerate(playlist):
        outPath = destiny + str(i + 1).rjust(padSize, "0") + "_" + song[1]
        listIO.append((song[0], outPath))
        # print("I: " + song[0] + "\n" + "O: " + outPath + "\n")
    return(listIO)
