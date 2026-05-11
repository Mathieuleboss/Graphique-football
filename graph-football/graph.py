import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

df = pd.read_csv("transfers_clean.csv")

G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(row["from_team_name"], row["to_team_name"], weight=row["weight"])

# Supprimer petits nœuds
G.remove_nodes_from([n for n in G.nodes() if G.degree(n) < 5])

# Layout amélioré
pos = nx.spring_layout(G, k=0.5, iterations=100, seed=42)

# Communautés
communities = community.greedy_modularity_communities(G)

node_colors = {}
for i, com in enumerate(communities):
    for node in com:
        node_colors[node] = i

colors = [node_colors[n] for n in G.nodes()]

# Taille des nœuds
node_sizes = [G.degree(n) * 50 for n in G.nodes()]

plt.figure(figsize=(16,12))

nx.draw(
    G, pos,
    node_size=node_sizes,
    node_color=colors,
    cmap=plt.cm.tab20,
    edge_color="gray",
    width=0.5,
    with_labels=False
)

plt.title("Réseau des transferts (filtré et structuré)")
plt.show()