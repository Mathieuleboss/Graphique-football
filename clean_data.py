import pandas as pd

# Charger les données
df = pd.read_csv("transfer_history.csv")

# Supprimer les faux clubs
df = df[
    (~df["from_team_name"].isin(["Retired", "Without Club"])) &
    (~df["to_team_name"].isin(["Retired", "Without Club"]))
]

# Supprimer les équipes jeunes / réserves (option mais recommandé)
df = df[
    ~df["from_team_name"].str.contains("U", na=False) &
    ~df["to_team_name"].str.contains("U", na=False) &
    ~df["from_team_name"].str.contains("II", na=False) &
    ~df["to_team_name"].str.contains("II", na=False)
]

# Garder colonnes utiles
df = df[[
    "from_team_name",
    "to_team_name",
    "transfer_fee"
]]

# Nettoyer les valeurs
df = df.dropna()
df["transfer_fee"] = df["transfer_fee"].fillna(0)

# Regrouper transferts
edges = df.groupby(["from_team_name", "to_team_name"]).agg({
    "from_team_name": "count",
    "transfer_fee": "sum"
}).rename(columns={"from_team_name": "weight"}).reset_index()

# Filtrer pour lisibilité (très important)
edges = edges[edges["weight"] > 8]

# Sauvegarde
edges.to_csv("transfers_clean.csv", index=False)

print("✅ Données nettoyées prêtes")