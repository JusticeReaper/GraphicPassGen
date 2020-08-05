from tkinter import *
import secrets
import string

def generate_password():
    stringSource  = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)
    for i in range(Length_scale.get()-4):
        password += secrets.choice(stringSource)
    char_list = list(password)
    secrets.SystemRandom().shuffle(char_list)
    password = ''.join(char_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# Créer une fenêtre
window = Tk()
window.title("PassGen")
window.geometry("516x200")
window.minsize(516, 200)
window.maxsize(516, 200)
window.iconbitmap("../resources/LD.ico")
window.config(background='#383838')

# Créer la frame principale
frame = Frame(window, bg='#383838')

# Création d'image
width = 96
height = 125
image = PhotoImage(file="../resources/redlock.png")
canvas = Canvas(frame, width=width, height=height, bg='#383838', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W, padx=10)

# Créer une sous-boîte
right_frame = Frame(frame, bg ='#383838', borderwidth=5, relief=SOLID)

# Créer un titre
Label_title = Label(right_frame, text ="Mot de passe :", font=("Helvetica", 20), bg='#383838', fg='white')
Label_title.pack()

# Créer un champs/entrée
password_entry = Entry(right_frame, font=("Helvetica", 15), bg='#383838', fg='white', width=35, relief=SOLID, selectbackground='black')
password_entry.pack()

# Créer un slider
Length_scale = Scale(right_frame, orient=HORIZONTAL, from_=4, to=30, bg='#383838', fg='white', font=("Helvetica",10), cursor='hand2', activebackground='#383838', borderwidth=0,troughcolor='#5e5e5e', sliderrelief=SOLID, label="Longueur du mot de passe :", highlightthickness=0)
Length_scale.pack(fill=X)

# Créer un bouton
Generate_password_button = Button(right_frame, text ="Générer", font=("Helvetica", 20), bg='#383838', fg='white', command=generate_password, cursor='hand2', relief=FLAT, activebackground='#5e5e5e')
Generate_password_button.pack(fill=X)

# on place la sous boîte à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# Afficher la frame
frame.pack(expand=YES)

# Afficher la fenêtre
window.mainloop()