
import sys
import os
import playlistAux as aux
from shutil import copyfile


###############################################################################
# Define IO
# src = "/Users/glados/Desktop/Mixtape108_TheSpaceBetween.xml"
# dst = "/Users/glados/Desktop/playlist/"
(src, dst) = (sys.argv[1], sys.argv[2])

###############################################################################
# Get the playlist in shape
files = aux.getIOPaths(src, dst)
print(files)

###############################################################################
# Do the copy in disk
if not os.path.exists(dst):
    os.mkdir(dst)
[copyfile(song[0], song[1]) for song in files]
