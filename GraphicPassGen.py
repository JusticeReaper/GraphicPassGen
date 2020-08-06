import tkinter as tk
import secrets
import string

def generate_password():
    stringSource  = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)
    for i in range(tk.Length_scale.get()-4):
        password += secrets.choice(stringSource)
    char_list = list(password)
    secrets.SystemRandom().shuffle(char_list)
    password = ''.join(char_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Créer une fenêtre
tk.window = tk.Tk()
tk.window.title("Graphic Password Generator")
tk.window.geometry("516x184")
tk.window.minsize(516, 184)
tk.window.maxsize(516, 184)
tk.window.iconbitmap("resources/lock.ico")
tk.window.config(background='#383838')

# Créer la frame principale
tk.frame = tk.Frame(tk.window, bg='#383838')

# Création d'image
tk.width = 96
tk.height = 125
tk.image = tk.PhotoImage(file="resources/redlock.png")
tk.canvas = tk.Canvas(tk.frame, width=tk.width, height=tk.height, bg='#383838', bd=0, highlightthickness=0)
tk.canvas.create_image(tk.width/2, tk.height/2, image=tk.image)
tk.canvas.grid(row=0, column=0, sticky=tk.W, padx=10)

# Créer une sous-boîte
tk.right_frame = tk.Frame(tk.frame, bg ='#383838', borderwidth=5, relief=tk.SOLID)

# Créer un titre
tk.Label_title = tk.Label(tk.right_frame, text ="Mot de passe :", font=("Helvetica", 20), bg='#383838', fg='white')
tk.Label_title.pack()

# Créer un champs/entrée
password_entry = tk.Entry(tk.right_frame, font=("Helvetica", 15), bg='#383838', fg='white', width=35, relief=tk.SOLID, selectbackground='black')
password_entry.pack()

# Créer un slider
tk.Length_scale = tk.Scale(tk.right_frame, orient=tk.HORIZONTAL, from_=4, to=30, bg='#383838', fg='white', font=("Helvetica",10), cursor='sb_h_double_arrow', activebackground='#383838', borderwidth=0,troughcolor='#5e5e5e', sliderrelief=tk.SOLID, label="Longueur du mot de passe :", highlightthickness=0)
tk.Length_scale.pack(fill=tk.X)

# Créer un bouton
tk.Generate_password_button = tk.Button(tk.right_frame, text ="Générer", font=("Helvetica", 20), bg='#383838', fg='white', command=generate_password, cursor='hand2', relief=tk.FLAT, activebackground='#5e5e5e')
tk.Generate_password_button.pack(fill=tk.X)

# on place la sous boîte à droite de la frame principale
tk.right_frame.grid(row=0, column=1, sticky=tk.W)

# Afficher la frame
tk.frame.pack(expand=tk.YES)

# Afficher la fenêtre
tk.window.mainloop()