import sys

task = {}

print("Bienvenue dans votre gestionnaire de tâches !")

def gdt():
    while True:
        try:
            choose = int(input("Que souhaitez-vous faire ?\n 1. Afficher les tâches\n 2. Ajouter une tâche\n 3. Supprimer une tâche\n 4. Définir une tâche comme accomplie\n 5. Quitter le gestionnaire de tâches"))
            if choose not in [1, 2, 3, 4]:
                raise ValueError("Erreur")

            if choose == 1:
                for keys, values in task.items():
                    print(f"{keys} {values}\n")

            elif choose == 2:
                print("Ajouter une tâche:")
                add_task_key = input()
                task[add_task_key] = "[ ]"
                print("Tâche ajouté !")

            elif choose == 3:
                print("Quelle tâche souhaitez-vous supprimer ?")
                delete_task_key = input()
                if delete_task_key in task:
                    del task[delete_task_key]
                    print("tâche supprimé!")
                else:
                    print("Erreur: cette tâche n'existe pas.")

            elif choose == 4:
                print("Quelle tâche souhaitez-vous marqué comme accomplie ?")
                finish_task_key = input()
                if finish_task_key in task.keys():
                    task[finish_task_key] = "[X]"
                    print("Tâche ajouté comme accomplie")
                else:
                    print("Erreur: cette tâche n'existe pas.")

            elif choose == 5:
                print("Au revoir!")
                sys.exit()

        except ValueError:
            print("Erreur, choissiez un nombre entre 1, 2, 3, 4 et 5.")
gdt()