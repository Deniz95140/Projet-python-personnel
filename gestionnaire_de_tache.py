import sys

task = {}

print("Bienvenue dans votre gestionnaire de tâches !")

def afficher_tache():
    if not task:
        print("Il n'y a aucune tâche.")
    else:
        for keys, values in task.items():
            print(f"{keys} {values}\n")

def ajouter_tache():
    print("Ajouter une tâche: ")
    add_task_key = input()
    task[add_task_key] = "[ ]"
    print("Tâche ajouté !")

def supprimer_tache():
    print("Quelle tâche souhaitez vous supprimer ? : ")
    delete_task_key = input()
    if delete_task_key in task.keys():
        del task[delete_task_key]
        print("Tâche supprimé !")
    else:
        print("Erreur, cette tâche n'existe pas.")

def definir_tache():
    print("Quelle tâche souhaitez-vous marqué comme accomplie ? : ")
    finish_task_key = input()
    if finish_task_key in task.keys():
        task[finish_task_key] = "[X]"
        print("Tâche défini comme accomplit !")
    else:
        print("Erreur, cette tâche n'existe pas.")

def gdt():
    while True:
        try:
            choose = int(input("\nQue souhaitez-vous faire ?\n\n 1. Afficher les tâches\n 2. Ajouter une tâche\n 3. Supprimer une tâche\n 4. Définir une tâche comme accomplie\n 5. Quitter le gestionnaire de tâches\n"))
            if choose == 1:
                afficher_tache()

            if choose == 2:
                ajouter_tache()

            if choose == 3:
                supprimer_tache()

            if choose == 4:
                definir_tache()
            elif choose == 5:
                print("Au revoir!")
                sys.exit()

        except ValueError:
            print("Erreur, choissiez un nombre entre 1, 2, 3, 4 et 5.")

if __name__ == '__main__':
    gdt()
