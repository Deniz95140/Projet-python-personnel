import math
import random
import sys

print("Bienvenu dans le quiz mathématique, il y a 3 types de niveau. Choisissez un des 3 niveaux.",
      "Niveau 1: Facile \n Niveau 2: Normal \n Niveau 3: Difficile")
def quiz_mathematique():
      while True:
        try:
            choose_level = int(input("Si vous souhaitez faire le niveau 1, tapez 1, Si vous souhaitez faire le niveau 2, tapez 2 et si vous souhaitez faire le niveau 3, tapez 3."))
            if choose_level not in [1, 2, 3]:
                raise ValueError("Veuillez entrer uniquement 1,2 ou 3.")
            break
        except ValueError:
            print("Erreur, veuillez réessayer.")
      if choose_level == 1:
            print("Bienvenue au niveau 1 (facile) !")
            point = 0
            for i in range(10):
                  nombre1 = random.randint(1,500)
                  nombre2 = random.randint(1,500)
                  operateur = random.choice(["+", "-", "*", "/"])
                  if operateur == "+":
                        resultat = nombre1 + nombre2
                  elif operateur == "-":
                        resultat = nombre1 - nombre2
                  elif operateur == "*":
                        resultat = nombre1 * nombre2
                  else:
                        resultat = nombre1 / nombre2

                  question = print(f"Question {i+1} Calculez: {nombre1} {operateur} {nombre2} = ")
                  while True:
                      try:
                        reponse_utilisateur = float(input())
                        break
                      except ValueError:
                        print("Erreur, veuillez réessayer.")
                  if reponse_utilisateur == resultat:
                        print("Correct!")
                        point = point + 1
                  else:
                        print(f"Incorrect! La réponse était {resultat}")
                  print()
            note = (point / 10) * 20
            print(f"Fin du quizz, votre résultat: {note} / 20")

      if choose_level == 2:
            print("Bienvenue au niveau 2 (moyen) !")
            point = 0
            for i in range(10):
                  type_question = random.choice(["fraction", "decimal", "pourcentage", "equation"])
                  if type_question == "fraction":
                        numerateur = random.randint(1,10)
                        denominateur = random.randint(numerateur + 1, 20)
                        resultat = numerateur / denominateur
                        question = print(f"Question {i + 1} : Simplifiez la fraction {numerateur}/{denominateur}: ")
                  elif type_question == "decimal":
                        nombre_decimal = round(random.uniform(1, 10), 2)
                        resultat = nombre_decimal
                        question = print(f"Question {i + 1} : Convertissez le nombre {nombre_decimal} en fraction: ")
                  elif type_question == "pourcentage":
                        nombre = random.randint(1, 100)
                        pourcentage = random.randint(1,100)
                        resultat = nombre * pourcentage / 100
                        question = print(f"Question {i + 1} : Quel est %{pourcentage} de {nombre} ? ")
                  else:
                        a = random.randint(1,10)
                        b = random.randint(1,10)
                        resultat = (b - a) / a
                        question = print(f"Question {i + 1} : Résolvez l'équation {a}x + {b} = 0 : ")
                  while True:
                      try:
                        reponse_utilisateur = float(input())
                        break
                      except ValueError:
                        print("Erreur, veuillez réessayer.")
                  if reponse_utilisateur == resultat:
                        print("Correct!")
                        point = point + 1
                  else:
                        print(f"Incorrect! Le résultat était {resultat}")
                  print()
            note = (point / 10) * 20
            print(f"Fin du quizz, votre résultat: {note} / 20")

      if choose_level == 3:
            print("Bienvenue au niveau 3 (difficile) !")
            point = 0
            for i in range(10):
                  type_question = random.choice(["racine_carree", "exponentielle", "logarithme"])
                  if type_question == "racine_carree":
                        nombre = random.randint(1, 100)
                        resultat = math.sqrt(nombre)
                        print(f"Question {i + 1} : Quel est la racine carrée de {nombre} ? ")
                  elif type_question == "exponentielle":
                        nombre = random.randint(1, 10)
                        resultat = math.exp(nombre)
                        print(f"Question {i + 1} : Calculez e^{nombre} : ")
                  else:
                        nombre = random.randint(1, 100)
                        resultat = math.log10(nombre)
                        print(f"Question {i + 1} : Calculez log({nombre}) : ")
                  while True:
                      try:
                        reponse_utilisateur = float(input())
                        break
                      except ValueError:
                        print("Erreur, veuillez réessayer.")
                  if reponse_utilisateur == resultat:
                        print("Correct!")
                        point = point + 1
                  else:
                        print(f"Incorrect! Le résultat était {resultat}")
                  print()
            note = (point / 10) * 20
            print(f"Fin du quizz, votre résultat: {note} / 20")

quiz_mathematique()
while True:
      try:
        choose = int(input("Souhaitez vous rejouer ? Si oui, tapez 1, Si non, tapez 2 :"))
        if choose not in [1, 2]:
            raise ValueError("Veuillez entrer uniquement 1 ou 2.")
      except ValueError:
        choose = int((input("Erreur, Souhaitez vous rejouer ? Si oui, tapez 1, Si non, tapez 2 :")))
      if choose == 1:
            quiz_mathematique()
      if choose == 2:
            print("Au revoir!")
            sys.exit()