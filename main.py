""" ce dictionnaire englogbe tout ce que la machine dispose comme marchandise
leur prix ainsi que leur ingredients """
MENU = {
    "espresso": {
        "ingredients": {
            "eau": 50,
            "café": 18,
        },
        "prix": 1000,
    },
    "latte": {
        "ingredients": {
            "eau": 200,
            "lait": 150,
            "café": 24,
        },
        "prix": 2000,
    },
    "cappuccino": {
        "ingredients": {
            "eau": 250,
            "lait": 100,
            "café": 24,
        },
        "prix": 3000,
    }
}
resources = {
    "eau": 300,
    "lait": 200,
    "café": 100,
}
def resource_suffisante(commande_ingredients   ):
    for item in commande_ingredients:
        if commande_ingredients[item]>=resources[item]:
            print(f"désolé il n'ya plus assez de {item}")
            return False
    return True
montant_accepte = (1000,500,2000)
def argent(total):

    somme = int(input("veuillez procedé au paiment svp : "))
    total +=somme
    return total

profit = 0
is_on = True

def paiement_reussie(argent_recu,prix_boisson):

    if argent_recu > prix_boisson:
        global profit
        profit += prix_boisson
        monnaie_rendue = argent_recu - prix_boisson
        print(f"votre {choix} ☕ est servi ! ")
        print(f"voici votre monnaie {monnaie_rendue} fcfa")
        print("a bientot ! ")
        return True
    elif argent_recu == prix_boisson:

        profit +=prix_boisson
        print(f"merci pour votre achat voici votre {choix} ☕ !" )

    else:
        print("fond insuffisant, remboursement en cour...")
        print("remboursé !")
        return False

"""la fonction point element permet de retrancher les ingredients deja utilisé de votre stock total 
a chque utilisation """
def point_elements(choix_element):
    if paiement_reussie and boisson == "latte":
        resources["eau"] -= boisson["ingredients"]["eau"]
        resources["lait"] -= boisson["ingredients"]["lait"]
        resources["café"] -= boisson["ingredients"]["café"]
    elif paiement_reussie and boisson == "cappuccino":
        resources["eau"] -= boisson["ingredients"]["eau"]
        resources["lait"] -= boisson["ingredients"]["lait"]
        resources["café"] -= boisson["ingredients"]["café"]
    else:
        resources["eau"] -= boisson["ingredients"]["eau"]
        resources["café"] -= boisson["ingredients"]["café"]
        
"""boucle principale 
                    """
while is_on: #ceci est la boucle principale
    choix = input("quel est votre commande ? (cappucino/ latte /espresso)")
    if choix == "off":
        is_on = False
    elif choix == "rapport": #tape rapport pour avoir acces au point de tes ressources et profit
        print(f"eau : {resources["eau"]}ml")
        print(f"lait : {resources["lait"]}ml")
        print(f"café : {resources['café']}g")
        print(f"profit : {profit} fcfa")
    else:
        boisson = MENU[choix]
        print(f"boisson : {boisson}")
        if resource_suffisante(boisson["ingredients"]):
            paiement = argent(0)
            paiement_reussie(paiement, boisson["prix"])
            point_elements(boisson["ingredients"])

