# -*- coding: utf-8 -*-

###############################################################################
# Game of Thrones Map Plotting
#  Objectives:
#   To test the Google Trends data retreival within Python
# Sources:
#   http://ric70x7.github.io/20190318_got.html
###############################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Loading libraries
import geopandas as gp
import numpy as np
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import LineString, MultiLineString
%matplotlib inline

# Paths and Constants #########################################################
INPUT_PATH = "../data/extracted/GoT/GoTRelease/"

# Loading datasets ############################################################
gotContinents = gp.GeoDataFrame.from_file(INPUT_PATH + 'continents.shp')
gotRivers = gp.GeoDataFrame.from_file(INPUT_PATH + 'rivers.shp')
gotLocations = gp.GeoDataFrame.from_file(INPUT_PATH + 'locations.shp')
gotIslands = gp.GeoDataFrame.from_file(INPUT_PATH + 'islands.shp')
gotCities = gotLocations.loc[gotLocations['type'] == 'City']


print(gotContinents)
print(gotRivers.head(3))

type(gotContinents.loc[0, 'geometry'])

# Printing a map ##############################################################
print(gotContinents.bounds)
xBounds = gotContinents.bounds[['minx', 'maxx']]
yBounds = gotContinents.bounds[['miny', 'maxy']]


# Creating canvas
fig, ax = plt.subplots(1, figsize=(8, 8))

# Adding continents
for i, gi in enumerate(gotContinents.geometry):
    ax.add_patch(PolygonPatch(gi, color='burlywood', ec='gray', lw=1))
    ax.text(gi.centroid.xy[0][0], gi.centroid.xy[1][0],
            s=gotContinents.iloc[i]['name'], fontsize=18, color='k')

# Adding islands
for gi in gotIslands.geometry:
    ax.add_patch(PolygonPatch(gi, color='burlywood', ec='k', lw=1))

# Adding rivers
for gi in gotRivers.geometry:
    if isinstance(gi, LineString):
        # Some rivers are defined as a single line
        ax.plot(gi.xy[0], gi.xy[1], color='cornflowerblue')
    elif isinstance(gi, MultiLineString):
        # Some are defined as multiple lines
        for j, lj in enumerate(gi):
            ax.plot(lj.xy[0], lj.xy[1], color='cornflowerblue')

# Adding cities
for i, gi in enumerate(gotCities.geometry):  # Add cities
    ax.plot(gi.xy[0], gi.xy[1], marker='o', color='maroon')
    ax.text(gi.xy[0][0]+1, gi.xy[1][0]+1,
            s=gotCities.iloc[i]['name'], color='k')

# Adding a grid
ax.grid(linestyle='--')
fig.savefig("./images/got.png",dpi=250)

# Closing the figure ##########################################################
plt.close()
