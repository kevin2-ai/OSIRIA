print(f"{'='*30}\n\tOSIRIA démarre...\n{'='*30}")
while True:
    print("\nEntrez une commande")
    commande = input("Vous : ").strip()
    if commande.lower() == "quitter":
        break
    print("Commande reçue:",commande)