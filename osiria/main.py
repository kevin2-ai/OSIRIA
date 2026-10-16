print("Osiria demarre")
print("\nEntrez une commande")

while True: 
    cmdUser = input("Vous : ").strip()
    if cmdUser.upper() == "QUITTER":
        break    
    print("Commande reçu: ",cmdUser)