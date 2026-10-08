produit = "Clavier"
prix_ht = 19.90
quantity = 3
taux_tva = 0.20
prix_ttc = prix_ht * (1+taux_tva)
total_ht= prix_ht * quantity 
total_ttc = prix_ttc * quantity

print(f"{quantity} x {produit} : {total_ttc:.2f} euros TTC")
