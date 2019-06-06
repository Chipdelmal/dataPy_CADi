# -*- coding: utf-8 -*-

###############################################################################
# "osmnx" Buildings
###############################################################################
#  Objectives:
#
#  Source:
#   https://github.com/gboeing/osmnx-examples
#   https://github.com/gboeing/osmnx
#   https://geoffboeing.com/publications/osmnx-complex-street-networks/
#   https://www.researchgate.net/publication/326799779_Urban_Spatial_Order_Street_Network_Orientation_Configuration_and_Entropy
###############################################################################
#  Important instructions!
#   The steps followed to make the package work in MacOS were:
#       conda create --override-channels -c conda-forge -n OSMNX python=3 osmnx
#       conda install -c conda-forge geopandas
#       pip uninstall pyproj
#       conda install pyproj
#       pip install pyproj
###############################################################################

###############################################################################
# Import Libraries
import networkx as nx
import osmnx as ox
import matplotlib.cm as cm
# import matplotlib.pyplot as plt
import matplotlib.colors as colors
# pyproj.__path__
%matplotlib inline


gdf = ox.footprints.footprints_from_place(place='Piedmont, California, USA')
gdf_proj = ox.project_gdf(gdf)
fig, ax = ox.footprints.plot_footprints(
    gdf_proj, bgcolor='#333333', color='w',
    save=True, show=False, close=True,
    filename='piedmont_bldgs', dpi=500
)
gdf_save = gdf.drop(labels='nodes', axis=1)
gdf_save.to_file('../data/extracted/osmnx/piedmont_bldgs')
