print("OSIRIA démarre...")

actif = True

while actif:
    commande = input("Vous : ")

    if commande.lower() == "quitter":
        print("OSIRIA s'arrête. À bientôt !")
        actif = False
    else:
        print("Commande reçue :", commande)
