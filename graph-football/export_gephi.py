import pandas as pd

df = pd.read_csv("transfers_clean.csv")

# garder colonnes utiles
edges = df[["from_team_name", "to_team_name", "weight"]]

# renommer pour Gephi
edges.columns = ["Source", "Target", "Weight"]

# sauvegarde
edges.to_csv("gephi_edges.csv", index=False)

print("✅ Fichier gephi_edges.csv prêt")
