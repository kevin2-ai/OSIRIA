cmdList = {
    "ouvrir_application": ["ouvre"],
    "creer_": ["crée un dossier", "crée un fichier"],
    "obtenir_": ["donne l'heure", "donne la date"],
}


# def knows_file(text):
#     if len(text.split('.')) == 2:
#         return True


def reconnaitre_commande(text : str) -> tuple[str|None, str|None, str|None]:
    """
    Identifier l'intention de l'utilisateur et retourne une 
    action structurée que le programme pourra exécuter.

    Args:
        string: commande entrez par l'utilisateur

    Returns:
        tuple: renvoi une liste de 3 élements {action,parametres,reconnue}
    """
    mots = text.lower().strip().split()

    if not mots:
        return None, None, None

    action = None
    params = None
    reconnu = False

    for categorie, cmd in cmdList.items():
        for cm in cmd:
            if mots[0] == cm.split()[0]:
                action = categorie
                break
        if action:
            break

    if action == "creer_" and len(mots) == 4:
        reconnu = True
        if "fichier" in mots:
            action = action + "fichier"
        elif "dossier" in mots:
            action = action + "dossier"
        if mots[-1] not in ("fichier", "dossier"):
            params = mots[-1]

    if action == "ouvrir_application" and len(mots) == 2:
        reconnu = True
        params = mots[1]

    if action == "obtenir_":
        if mots[-1] == "date" or mots[-1] == "l'heure":
            reconnu = True
            params = mots[-1]

    return action, params, reconnu


result = reconnaitre_commande(input("Vous : "))
print(result)
