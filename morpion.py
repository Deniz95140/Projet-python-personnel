class Morpion:
    def __init__(self):
        self.plateau = [[' ' for _ in range(3)] for _ in range(3)]
        self.joueur_actuel = 'X'

    def afficher_plateau(self):
        for ligne in self.plateau:
            print('|'.join(ligne))
            print('-' * 5)

    def jouer(self, ligne, colonne):
        if self.plateau[ligne][colonne] == ' ':
            self.plateau[ligne][colonne] = self.joueur_actuel
            self.joueur_actuel = 'O' if self.joueur_actuel == 'X' else 'X'
        else:
            print("La case est déjà occupée. Essayez une autre case.")

    def verifier_victoire(self):
        for i in range(3):
            if self.plateau[i][0] == self.plateau[i][1] == self.plateau[i][2] != ' ':
                return True
            if self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] != ' ':
                return True
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != ' ':
            return True
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != ' ':
            return True
        return False

morpion = Morpion()
morpion.afficher_plateau()

while True:
    try:
        ligne = int(input("Entrez le numéro de ligne (0, 1, ou 2) : "))
        colonne = int(input("Entrez le numéro de colonne (0, 1, ou 2) : "))
        morpion.jouer(ligne, colonne)
        morpion.afficher_plateau()
        if morpion.verifier_victoire():
            print("Joueur", morpion.joueur_actuel, "a gagné !")
            break
    except ValueError:
        print("Veuillez entrer des numéros valides pour la ligne et la colonne.")
