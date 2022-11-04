"""
Module Doc
"""
####################
# Libraries import #
####################

# We import the randint item frop random librarie so we can generate random numbers
from random import randint

#####################
# Variable settings #
#####################

# We create a p variable. The p stand for "Player"
player = -1 # pylint: disable=invalid-name

# We create a c variable. The c stand for "Computer"
computer = 0 # pylint: disable=invalid-name

# We create a g variable. The g stand for "Game"
game = 0 # pylint: disable=invalid-name

possibility = ["Pierre" , "Feuille" , "Ciseaux"]

######################
# Instructions chain #
######################

# While g != 2, we continue playing
while game != 2:
    # While p < 0 or p > 4, we continue to ask for a number
    while player < 0 or player > 4:
        player = int(input("Tapez 1 pour Pierre, 2 pour Feuille et 3 pour Ciseaux : "))
        # Error Message
        if player < 0 or player > 4:
            print("Erreur, arrête tes bêtises et met un chiffre disponible")
        player-= 1
    # We generate a random number betwin 0 and 2 for the computer
    computer = randint(0, 2)
    print("L'ordinateur à joué : " + possibility[computer])
    # In case of a tie
    if player == computer:
        print("Egalité !")
    # In case of a win
    elif player == (computer + 1) % 3:
        print("Bravo ! Tu as gagné !")
    # In case of an easter egg
    elif player == 3:
        print("Tricheur ! Le puit ne compte pas !")
    # In case of a second easter egg
    elif player == 4:
        print("Tu n'a pas fini avec tes bêtises ? Maintenant le volcan ?! Idiot !")
    # In case of a lose
    else:
        print("Mince, tu as perdu !")
    # We set the p variable to 0 so there is no bug
    player = -1 # pylint: disable=invalid-name
    # We ask if the player wish to continue
    game = int(input("Voulez vous continuer à jouer ? Si oui tapez 1 sinon tapez 2 : "))
    #Error Message
    if game < 1 or game > 2:
        print ('Bip bip bip - Ah, R2D2 te dit "Tu m'embêtes !"')
        break
