ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]


ca_par_produit = {v["produit"]: v["prix"] * v["quantite"] for v in ventes}
total = sum(ca_par_produit.values())
meilleur = max(ca_par_produit, key=ca_par_produit.get)
print(ca_par_produit)
print(f"Total : {total:.2f} euros")
print(f"Meilleur produit : {meilleur}")


