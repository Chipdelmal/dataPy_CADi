# -*- coding: utf-8 -*-

###############################################################################
# "osmnx" Geographic Networks
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

###############################################################################
# Parse a location into a network
G = ox.graph_from_place(
    'Queretaro, Mexico',
    network_type='drive'
)
fig, ax = ox.plot_graph(G)
fig.savefig("./images/queretaro.png", dpi=500)

###############################################################################
# Get some network stats
basic_stats = ox.basic_stats(G)
print(list(basic_stats.keys()))
print(basic_stats["edge_length_total"])

extended_stats = ox.extended_stats(G)
print(extended_stats['pagerank_max_node'])


###############################################################################
# Parse and plot an address
address = '2700 Shattuck Ave, Berkeley, CA'
G = ox.graph_from_address(address, network_type='drive', distance=750)
G_proj = ox.project_graph(G)
fig, ax = ox.plot_graph(
    G_proj, fig_height=10, node_color='orange',
    node_size=30, node_zorder=2, node_edgecolor='k'
)


###############################################################################
# Parse and plot an address specifying levels
place = {
    'city' : 'San Francisco',
    'state' : 'California',
    'country' : 'USA'
}
G = ox.graph_from_place(place, network_type='drive')
fig, ax = ox.plot_graph(G, fig_height=12, node_size=0, edge_linewidth=0.5)
