# conda create --override-channels -c conda-forge -n OSMNX python=3 osmnx
# conda install -c conda-forge geopandas
# pip uninstall pyproj
# conda install pyproj
# pip install pyproj

import networkx as nx
import osmnx as ox
from keys import google_elevation_api_key
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


# use arguments to turn other toplogical analyses on/off
more_stats = ox.extended_stats(G, ecc=True, bc=True, cc=True)
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


# get the nearest network node to each point
orig_node = ox.get_nearest_node(G, (37.828903, -122.245846))
dest_node = ox.get_nearest_node(G, (37.812303, -122.215006))



# find the route between these nodes then plot it
route = nx.shortest_path(G, orig_node, dest_node, weight='length')
fig, ax = ox.plot_graph_route(G, route, node_size=0)





# make query an unambiguous dict to help the geocoder find specifically what you're looking for
place = {
    'city' : 'San Francisco',
    'state' : 'California',
    'country' : 'USA'
}
G = ox.graph_from_place(place, network_type='drive')
fig, ax = ox.plot_graph(G, fig_height=12, node_size=0, edge_linewidth=0.5)


address = '2700 Shattuck Ave, Berkeley, CA'
G = ox.graph_from_address(address, network_type='drive', distance=750)
G_proj = ox.project_graph(G)
fig, ax = ox.plot_graph(G_proj, fig_height=10, node_color='orange', node_size=30,
                        node_zorder=2, node_edgecolor='k')
