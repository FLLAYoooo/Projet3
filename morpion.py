""" import de la fonction random"""
from random import randint


cases={"a1":[" ","l"],"b1":[" ","l"],"c1":[" ","l"],"a2":[" ","l"],"b2":[" ","l"],"c2":[" ","l"],"a3":[" ","l"],"b3":[" ","l"],"c3":[" ","l"]}

print("  ___A__ ___B__ ___C__\n |      |      |      |\n1|   "+cases["a1"][0]+"  |   "+cases["b1"][0]+"  |   "+cases["c1"][0]+"  |\n |______|______|______|\n |      |      |      |\n2|   "+cases["a2"][0]+"  |   "+cases["b2"][0]+"  |   "+cases["b2"][0]+"  |\n |______|______|______|\n |      |      |      |\n3|   "+cases["a3"][0]+"  |   "+cases["b3"][0]+"  |   "+cases["c3"][0]+"  |\n |______|______|______|")

def jeux():
    """Jeux de morpion
    <-- rien
    --> rien """
    victoire = False
    nbtours = 0
    aqui = randint(1,2)
    case = "None"
    while not victoire and nbtours<9:
        print("c'est au tour du joueur",aqui,"de jouer ! ")
        while case not in cases or cases[case][1] != "l":
            case = str(input("Sur quel case voulez vous jouer? "))
        if aqui == 1:
            cases[case][0] = "X"
        else:
            cases[case][0] = "O"
        cases[case][1] = "o"

        print("  ___A__ ___B__ ___C__\n |      |      |      |\n1|   "+cases["a1"][0]+"  |   "+cases["b1"][0]+"  |   "+cases["c1"][0]+"  |\n |______|______|______|\n |      |      |      |\n2|   "+cases["a2"][0]+"  |   "+cases["b2"][0]+"  |   "+cases["c2"][0]+"  |\n |______|______|______|\n |      |      |      |\n3|   "+cases["a3"][0]+"  |   "+cases["b3"][0]+"  |   "+cases["c3"][0]+"  |\n |______|______|______|")
        victoire = victory()
        if aqui == 1:
            aqui = 2
        else:
            aqui = 1
        nbtours += 1
    if victoire:
        print("c'est le joueur",aqui,"qui a gagné la partie")
    else:
        print("égalitée")


def victory():
    """ Condition de victoire du morpion
    <-- rien
    --> bool gagné ou pas """
    gagne = False
    if cases["a1"][1] ==  cases["a2"][1] ==  cases["a3"][1] ==  cases["b1"][1] ==  cases["b2"][1] == cases["b3"][1] == "o":
        print("\n██████████████████\n█░░░░░░░░░░░░░░░░█\n█░██████░░██████░█\n█░█░░░░█░░█░░░░█░█\n█░█░░░░█░░█░░░░█░█\n█░██████░░██████░█\n█░░░░░░░░░░░░░░░░█\n█░██████░░██████░█\n█░█░░░░█░░█░░░░█░█\n█░█░░░░█░░█░░░░█░█\n█░██████░░██████░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n██████████████████\n\n Vous avez crafté une porte\n")
    if cases["a1"][0] == cases["b1"][0] == cases["c1"][0] != " " or cases["a1"][0] == cases["b1"][0] == cases["c1"][0] != " " or cases["a3"][0] == cases["b3"][0] == cases["c3"][0] != " " or cases["a1"][0] == cases["a2"][0] == cases["a3"][0] != " " or cases["b1"][0] == cases["b2"][0] == cases["b3"][0] != " " or cases["c1"][0] == cases["c2"][0] == cases["c3"][0] != " "  or cases["a1"][0] == cases["b2"][0] == cases["c3"][0] != " " or cases["a3"][0] == cases["b2"][0] == cases["c1"][0] != " ":
        gagne = True
    return gagne


jeux()
