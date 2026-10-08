 
def convertir_note(texte):
    """12,5 -> 12.5 ; texte invalide -> None""" 
    try:
        return float(texte.strip().replace(",","."))
    except ValueError:
        return None
def moyenne(valeurs):
        if not valeurs:
            return None
        return sum(valeurs) / len(valeurs) 
def mention(note):
        if note >= 16:
            return "Très bien"
        elif note >= 14:
            return "bien"
        elif note >= 12:
            return "assez bien"
        elif note >= 10:
            return "insuffisant"

        