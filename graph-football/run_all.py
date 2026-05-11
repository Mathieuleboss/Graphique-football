import os

print("🔄 Nettoyage des données...")
os.system("python clean_data.py")

print("📊 Génération du graphe...")
os.system("python graph.py")

print("📈 Analyse...")
os.system("python analysis.py")

print("✅ Projet terminé")