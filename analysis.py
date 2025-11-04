import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

G = nx.read_edgelist("data/facebook_combined.txt")

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Basic Graph Info:")
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

degrees = [G.degree(n) for n in G.nodes()]
avg_degree = sum(degrees) / num_nodes
print(f"Average degree: {avg_degree:.2f}")

print("\nShortest Path Analysis:")

try:
    # This only works if the graph is fully connected
    avg_path = nx.average_shortest_path_length(G)
    print(f"Average shortest path length: {avg_path:.2f}")

except nx.NetworkXError:
    # If the graph is not connected, we analyze the largest component
    print("Graph is not fully connected. Analyzing the largest component.")

    components = list(nx.connected_components(G))
    largest_component = max(components, key=len)

    G_largest = G.subgraph(largest_component)

    print(f"Largest component has {G_largest.number_of_nodes()} nodes.")

    avg_path_largest = nx.average_shortest_path_length(G_largest)
    print(f"Average shortest path (largest component): {avg_path_largest:.2f}")

print("\nCentrality Analysis:")

degree_centrality = sorted(G.degree, key=lambda item: item[1], reverse=True)

print("Top 5 Nodes by Degree (Most connected):")
for i in range(5):
    node_id = degree_centrality[i][0]
    degree = degree_centrality[i][1]
    print(f"  Node {node_id} with {degree} connections")

print("\nBetweenness Centrality:")

betweenness_centrality = nx.betweenness_centrality(G, k=200, normalized=True)

sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda item: item[1], reverse=True)

print("\nTop 5 Nodes by Betweenness (Best 'bridges'):")
for i in range(5):
    node_id = sorted_betweenness[i][0]
    score = sorted_betweenness[i][1]
    print(f"  Node {node_id} with score: {score:.4f}")

print("\nCommunity Detection using Louvain method:")

communities = community.louvain_communities(G)

print(f"\nFound {len(communities)} communities.")

communities_by_size = sorted(communities, key=len, reverse=True)

print("\nTop 5 largest communities:")
for i in range(5):
    community_set = communities_by_size[i]
    print(f"  Community {i}: {len(community_set)} members")

print("\nVisualizing:")
print("Preparing visualization of the largest community...")

largest_community_nodes = communities_by_size[0]
G_viz = G.subgraph(largest_community_nodes)

plt.figure(figsize=(15, 15))
plt.title(f"Visualization of Largest Community")

pos = nx.spring_layout(G_viz, k=0.15)

nx.draw_networkx(
    G_viz,
    pos,
    with_labels=False,
    node_size=20,
    node_color="blue",
    edge_color="#eeeeee",
    width=0.5
)

plt.axis("off")
save_path = "visualizations/largest_community.png"
plt.savefig(save_path)
print(f"Graph visualization saved to: {save_path}")
plt.show()