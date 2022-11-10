"""
Module Doc
"""

####################
# Libraries import #
####################

# We import the randint item frop random librarie so we can generate random numbers
from random import randint

########################
# Functions definition #
########################


board={"a1":[" ","l"],"b1":[" ","l"],"c1":[" ","l"],"a2":[" ","l"],\
    "b2":[" ","l"],"c2":[" ","l"],"a3":[" ","l"],"b3":[" ","l"],"c3":[" ","l"]}

print("  ___A__ ___B__ ___C__\n |      |      |      |\n1|   " +
board["a1"][0] +
"  |   " +
board["b1"][0] +
"  |   "+board["c1"][0] +
"  |\n |______|______|______|\n |      |      |      |\n2|   " +
board["a2"][0] +
"  |   " +
board["b2"][0] +
"  |   " +
board["b2"][0] +
"  |\n |______|______|______|\n |      |      |      |\n3|   " +
board["a3"][0] +
"  |   " +
board["b3"][0] +
"  |   " +
board["c3"][0] +
"  |\n |______|______|______|")

def game():
    """Morpion game
    <-- nothing
    --> nothing """
    victory = False
    turnsnumber = 0
    who = randint(1,2)
    square = "None"
    while not victory and turnsnumber<9:
        print("c'est au tour du joueur",who,"de jouer ! ")
        while square not in board or board[square][1] != "l":
            square = str(input("Sur quel square voulez vous jouer? ")).lower()
        if who == 1:
            board[square][0] = "X"
        else:
            board[square][0] = "O"
        board[square][1] = "o"

        print("  ___A__ ___B__ ___C__\n |      |      |      |\n1|   " +
        board["a1"][0] +
        "  |   " +
        board["b1"][0] +
        "  |   " +
        board["c1"][0] +
        "  |\n |______|______|______|\n |      |      |      |\n2|   " +
        board["a2"][0] +
        "  |   " +
        board["b2"][0] +
        "  |   " +
        board["c2"][0] +
        "  |\n |______|______|______|\n |      |      |      |\n3|   " +
        board["a3"][0] +
        "  |   " +
        board["b3"][0] +
        "  |   " +
        board["c3"][0] +
        "  |\n |______|______|______|")
        victory = gamewin()
        if who == 1:
            who = 2
        else:
            who = 1
        turnsnumber += 1
    if victory:
        print("C'est le joueur",who,"qui a gagné la partie")
    else:
        print("Egalitée")


def gamewin():
    """ Win conditions
    <-- nothing
    --> bool win or no"""
    win = False
    if board["a1"][1] ==  board["a2"][1] ==  board["a3"][1] ==  board["b1"]\
        [1] ==  board["b2"][1] == board["b3"][1] == "o" \
        and board["c1"][1] ==  board["c2"][1] == board["c3"][1] == "l":
        print("\n██████████████████\n█░░░░░░░░░░░░░░░░█\n█░██████░░██████░█\n" + \
        "█░█░░░░█░░█░░░░█░█\n█░█░░░░█░░█░░░░█░█\n█░██████░░██████░█\n" + \
        "█░░░░░░░░░░░░░░░░█\n█░██████░░██████░█\n█░█░░░░█░░█░░░░█░█\n" + \
        "█░█░░░░█░░█░░░░█░█\n█░██████░░██████░█\n█░░░░░░░░░░░░░░░░█\n" + \
        "█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n" + \
        "█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░█\n" + \
        "██████████████████\n\n Vous avez crafté une porte\n")
    if board["a1"][0] == board["b1"][0] == board["c1"][0] != " " or board["a1"]\
    [0] == board["b1"][0] == board["c1"][0] != " " or board["a3"][0] == board["b3"]\
    [0] == board["c3"][0] != " " or board["a1"][0] == board["a2"][0] == board["a3"]\
    [0] != " " or board["b1"][0] == board["b2"][0] == board["b3"]\
    [0] != " " or board["c1"][0] == board["c2"][0] == board["c3"]\
    [0] != " "  or board["a1"][0] == board["b2"]\
    [0] == board["c3"][0] != " " or board["a3"]\
    [0] == board["b2"][0] == board["c1"][0] != " ":
        win = True
    return win

######################
# Instructions chain #
######################

game()
