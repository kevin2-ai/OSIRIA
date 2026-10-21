from commandes import reconnaitre_commande
contenu=[]
print("OSIRIA Démarre...")
while True:
    texte=input("Vous: ")
    if texte != "":
        if texte.lower() != "quitter":
            print(f"Commande reçue: {texte }")
            contenuT=contenu.append(texte)
            print(contenu)
            reconnaitre_commande(texte)
        else:
            break
    else:
        print("Que souhaitez-vous")