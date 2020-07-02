mport networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
import matplotlib.pyplot as plt
from networkx import *
ox.config(use_cache=True, log_console=True)
ox.__version__



graph = ox.graph_from_place("Montreal, QC, Canada",  network_type="drive_service")

fig,_ = ox.plot_graph(graph, node_zorder=4, node_color='w', bgcolor='k')
print(graph)
'''nodes, edges = ox.graph_to_gdfs(graph, nodes=True, edges=True,
        node_geometry=True,
        fill_edge_geometry=True)
'''

nodes, gdf_edges = ox.graph_to_gdfs(graph, nodes=True)

# list of lats and lngs
lngs = gdf_edges.head().centroid.map(lambda x: x.coords[0][0])
lats = gdf_edges.head().centroid.map(lambda x: x.coords[0][1])

print(nodes, "\n")
print(gdf_edges, "\n")
print(lngs, "\n")
print(lats, "\n")
# the lat, lng at the spatial center of the graph
lng, lat = gdf_edges.unary_union.centroid.coords[0]
center_point = lat, lng

node_id = list(graph.nodes())[0]
node2 = list(graph.nodes())[7]


#print(node_id, "\n")
#print(nodes)

print(graph.nodes[304699073])
print(node2)
#graph.nodes[node_id]['y']

#shortestPath = nx.shortest_path(G, source= list(G.nodes())[10], target=list(G.nodes())[0], weight="10")
#node_colors = ["blue" if n in shortestPath else "red" for n in G.nodes()]
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos=pos)
#nx.draw_networkx_edges(G, pos=pos)

