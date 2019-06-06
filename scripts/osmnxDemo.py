# conda create --override-channels -c conda-forge -n OSMNX python=3 osmnx
# conda install -c conda-forge geopandas
# pip uninstall pyproj
# conda install pyproj
# pip install pyproj

import networkx as nx
import osmnx as ox
import matplotlib.cm as cm
import matplotlib.colors as colors
import pyproj
pyproj.__path__

G = ox.graph_from_place(
    'Manhattan Island, New York City, New York, USA',
    network_type='drive'
)
ox.plot_graph(G)


basic_stats = ox.basic_stats(G)
print(basic_stats['circuity_avg'])

extended_stats = ox.extended_stats(G)
print(extended_stats['pagerank_max_node'])



G = ox.graph_from_place('Piedmont, California, USA', network_type='drive')
fig, ax = ox.plot_graph(G)




# what sized area does our network cover in square meters?
G_proj = ox.project_graph(G)
nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
graph_area_m = nodes_proj.unary_union.convex_hull.area
graph_area_m


more_stats = ox.extended_stats(G, ecc=True, bc=True, cc=True) #use arguments to turn other toplogical analyses on/off
for key in sorted(more_stats.keys()):
    print(key)
# ox.save_graph_shapefile(G, filename='../data/extracted/OSMNX/mynetwork_shapefile')
# ox.save_graphml(G, filename='../data/extracted/OSMNX/mynetwork.graphml')



# edge closeness centrality: convert graph to line graph so edges become nodes and vice versa
edge_centrality = nx.closeness_centrality(nx.line_graph(G))

# list of edge values for the orginal graph
ev = [edge_centrality[edge + (0,)] for edge in G.edges()]

# color scale converted to list of colors for graph edges
norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
cmap = cm.ScalarMappable(norm=norm, cmap=cm.inferno)
ec = [cmap.to_rgba(cl) for cl in ev]

# color the edges in the original graph with closeness centralities in the line graph
fig, ax = ox.plot_graph(G, bgcolor='k', axis_off=True, node_size=0,
                        edge_color=ec, edge_linewidth=1.5, edge_alpha=1)
