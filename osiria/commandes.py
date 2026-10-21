def reconnaitre_commande(texte): 
    actions=["ouvrir_application","creer_dossier","creer_fichier"," obtenir_heure","obtenir_date"]
    action="RIEN FAIRE"
    parametres="AUCUN"
    reconnue=False
    if texte == "":
        return  print("texte est vide")
    if"ouvre" in texte.lower() and "bloc-note" in texte.lower():
        action=actions[0]
        parametres="bloc-notes"
        reconnue=True    
        action= actions[0]
        parametres="calculatrice"
        reconnue=True 
    elif "ouvre" in texte.lower() and "explorateur de fichiers" in texte.lower():
        action= actions[0]
        parametres="explorateur de fichiers"
        reconnue=True 
    elif"crée un dossier" in texte.lower():
        i = texte.index("crée un dossier")
        if i+1< len("crée un dossier"):
            action=action[1]
            parametres=texte[i+1]
            reconnue=True    
    elif"crée un fichier" in texte.lower():
        i = texte.index("crée un fichier")
        if i+1< len("crée un fichier"):
            action=actions[2]
            parametres=texte[i+1]
            reconnue=True   
    elif "donne" in texte.lower() and "heure" in texte.lower():
        action=actions[3]
        reconnue=True  
    elif "donne" in texte.lower() and "date" in texte.lower():
        action=actions[4]
        reconnue=True  
    else:
        print("Entrer une commande valide")        
       
    
    return print(f"je dois {action} de {parametres} et la commande est: {reconnue}")
