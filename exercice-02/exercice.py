temperatures = [-3, 0, 15, 31]
for temperature in temperatures:
    if temperature < 0:
        categorie = "Gel"
    elif temperature < 15:
        categorie = "Froid"
    elif temperature < 31:
        categorie = "Doux"
    else:
        categorie = "Chaud"

    print(f"{temperature}\t{categorie}")
annees = [2024, 1900, 2000]

for annee in annees:
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")
