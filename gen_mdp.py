# Bibliothèque
import tkinter as tk
from tkinter import messagebox
import random
import string

# Fonction pour générer le mot de passe
def generate_password():
    length = 16
    characters = ''

    if uppercase_var.get():
        characters += string.ascii_uppercase + string.ascii_lowercase
    if number_var.get():
        characters += string.digits
    if special_chars_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Attention", "Aucune option n'a été sélectionnée. Le mot de passe ne peut pas être généré.")
        return

    # Génère le mot de passe aléatoire
    password = ''.join(random.choice(characters) for _ in range(length))

    # Met à jour le champ de texte avec le mot de passe généré
    password_display.config(state='normal')  # Permet la modification temporaire
    password_display.delete(0, tk.END)  # Efface le texte précédent
    password_display.insert(0, password)  # Insère le nouveau mot de passe
    password_display.config(state='readonly')  # Repasser en lecture seule

# Fonction pour copier le mot de passe dans le presse-papier
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display.get())
    messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papier !")

# Interface
root = tk.Tk()
root.title("Générateur de mot de passe")
root.geometry("400x300")

# Variables pour les options de génération
uppercase_var = tk.BooleanVar()
number_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

# Boutons
tk.Checkbutton(root, text="Mélanger majuscules et minuscules", variable=uppercase_var).grid(row=0, column=0, sticky='w', padx=20, pady=5)
tk.Checkbutton(root, text="Inclure des chiffres", variable=number_var).grid(row=1, column=0, sticky='w', padx=20, pady=5)
tk.Checkbutton(root, text="Inclure des caractères spéciaux", variable=special_chars_var).grid(row=2, column=0, sticky='w', padx=20, pady=5)

# Champ de texte pour afficher le mot de passe généré
password_display = tk.Entry(root, width=50)
password_display.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Bouton pour générer le mot de passe
generate_button = tk.Button(root, text="Générer", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Bouton pour copier le mot de passe dans le presse-papier
copy_button = tk.Button(root, text='Copier sur le presse-papier', command=copy_to_clipboard)
copy_button.grid(row=5, column=0, columnspan=2, pady=10)

# Boucle principale
root.mainloop()