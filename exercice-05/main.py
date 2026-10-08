from outils import convertir_note, moyenne, mention

notes_brutes = ["12.5", "15", "abc", "9", "18.25"]
notes = []
ignore = 0

for texte in notes_brutes:
    note = convertir_note(texte)
    if note is None: ignore += 1
    else: notes.append(note)
    moy = moyenne(notes)
    print(f"Notes ignorées : {ignore}")
    print(f"Moyenne :{moy:.2f}")
    print(f"Mention : {mention(moy)}")
