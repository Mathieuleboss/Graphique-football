import pandas as pd
import networkx as nx

df = pd.read_csv("transfers_clean.csv")

G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(row["from_team_name"], row["to_team_name"], weight=row["weight"])

# Centralité
degree = nx.degree_centrality(G)

top = sorted(degree.items(), key=lambda x: x[1], reverse=True)

print("\n🏆 Top clubs les plus connectés :")
for club, score in top[:10]:
    print(f"{club} : {score:.3f}")

print("\n📊 Stats :")
print("Clubs :", G.number_of_nodes())
print("Connexions :", G.number_of_edges())