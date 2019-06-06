# -*- coding: utf-8 -*-

###############################################################################
# "osmnx" Geographic Networks Analyses
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
# Parse another location into a network
G = ox.graph_from_place(
    'Berkeley, California, USA',
    network_type='drive'
)
fig, ax = ox.plot_graph(G)
fig.savefig("./images/berkeley.png", dpi=500)

###############################################################################
# Do additional statistical analyses
G_proj = ox.project_graph(G)
nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
graph_area_m = nodes_proj.unary_union.convex_hull.area
graph_area_m

###############################################################################
# Do additional statistical analyses
more_stats = ox.extended_stats(G, ecc=True, bc=True, cc=True)
for key in sorted(more_stats.keys()):
    print(key)
# ox.save_graph_shapefile(G, filename='../data/extracted/OSMNX/mynetwork_shapefile')
# ox.save_graphml(G, filename='../data/extracted/OSMNX/mynetwork.graphml')

###############################################################################
# Calculate network metrics
edge_centrality = nx.closeness_centrality(nx.line_graph(G))
ev = [edge_centrality[edge + (0,)] for edge in G.edges()]

norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
cmap = cm.ScalarMappable(norm=norm, cmap=cm.inferno)
ec = [cmap.to_rgba(cl) for cl in ev]
fig, ax = ox.plot_graph(
    G, bgcolor='k', axis_off=True,
    node_size=0, edge_color=ec, edge_linewidth=1.5,
    edge_alpha=1
)
fig.savefig("./images/berkeleyCentrality.png", dpi=500)

###############################################################################
# Find and plot the nearest distance between two points
orig_node = ox.get_nearest_node(G, (37.8812, -122.2842))
dest_node = ox.get_nearest_node(G, (37.8812, -122.215006))
route = nx.shortest_path(G, orig_node, dest_node, weight='length')
fig, ax = ox.plot_graph_route(G, route, node_size=0)
fig.savefig("./images/berkeleyRoad.png", dpi=500)
