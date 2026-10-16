print("Osiria demarre")

while True: 
    cmdUser = input("Vous : ").strip()
    print("Commande : ",cmdUser)
    if cmdUser.upper() == "QUITTER":
        break    