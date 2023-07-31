from tkinter import filedialog
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import docx
from genie_logiciel import GENIE_LOGICIEL
from Admin_systeme import ADMINISTRATION_SYSTEME
from telecom import TELECOM
from design import DESIGN

theme = "light" 
customtkinter.set_appearance_mode(theme)
def charger_diplome(self):
    if charger_diplome_champ.get() == "Charger diplome en PDF":
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "* pdf")])
        print(file_path)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "* .txt"), ("Word Files", "* docx")])
    if file_path:
        if file_path.endswith(".txt"):   
            with open(file_path, "r") as file:
                text = file.read()
                lettre.delete("1.0", END)
                lettre.insert(END, text)
        elif file_path.endswith(".docx"):
            doc  = docx.Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text+ "\n"
            lettre.delete("1.0", END)
            lettre.insert(END, text)
    
def valider_formulaire():
    nom = entry_nom.get()
    postNom = entry_post.get()
    prenom = entry_prenom.get()
    date_de_naissance = entry_date.get()
    genre = entry_genre.get()   
    etatCivil = entry_etat.get()
    adresse = entry_adresse.get()
    numero_telephone = entry_numero.get()
    email = entry_email.get()
    etablissement = entry_etablissement.get()
    annee_diplome = entry_diplome.get()
    tel_responsable = entry_tel_respo.get()
    lettre_motivation = lettre.get("1.0", END)
    filliere = filliere_champ.get()
    print(lettre_motivation, len(lettre_motivation))
    validation = False
    if nom == "":
        entry_nom.configure(border_color = "red")
        validation = False
    else:
        entry_nom.configure(border_color = "gray")
        validation = True
        
    if postNom == "":
        validation = False
        entry_post.configure(border_color = "red")
    else:
        entry_post.configure(border_color = "gray")
        validation = True
    if prenom == "":
        entry_prenom.configure(border_color = "red")
        validation = False
    else:
        entry_prenom.configure(border_color = "gray")
        validation = True
    
    if date_de_naissance == "" or date_de_naissance=="        /        /       ":
        entry_date.configure(border_color = "red")
        validation = False
    else:
        entry_date.configure(border_color = "gray")
        validation = True
    if genre == "":
        entry_genre.configure(border_color = "red")
        validation = False
    else:
        entry_genre.configure(border_color = "gray")
        validation = True
    if etatCivil == "":
        validation = False
        entry_etat.configure(border_color = "red")
    else:
        entry_etat.configure(border_color = "gray")
        validation = True
    if adresse == "" or adresse=="   av   / com  / ville   ":
        validation = False
        entry_adresse.configure(border_color = "red")
    else:
        validation = True
        entry_adresse.configure(border_color = "gray")
    if numero_telephone == "":
        validation = False
        entry_numero.configure(border_color = "red")
    else:
        validation = True
        entry_numero.configure(border_color = "gray")
    if email == "" or len(email) == 1:
        validation = False
        entry_email.configure(border_color = "red")
    else:
        validation = True
        entry_email.configure(border_color = "gray")
    if etablissement == "":
        validation = False
        entry_etablissement.configure(border_color = "red")
    else:
        validation = True
        entry_etablissement.configure(border_color = "gray")
    if annee_diplome == "":
        validation = False
        entry_diplome.configure(border_color = "red")
    else:
        validation = True
        entry_diplome.configure(border_color = "gray")
    if tel_responsable == "":
        validation = False
        entry_tel_respo.configure(border_color = "red")
    else:
        validation = True
        entry_tel_respo.configure(border_color = "gray")
    if lettre_motivation == "" or len(lettre_motivation) == 1:
        lettre.configure(border_color = "red")
        validation = False
        def reset_assistant():
            lettre_instructions.delete("1.0", END)
            lettre_instructions.insert(END, texte_instructions)
        lettre_instructions.delete("1.0", END)
        lettre_instructions.insert("1.0", "Avant de valider assurez vous d'avoir rempli correctement tout les champs")
        window.after(4000, reset_assistant)
    else:
        validation = True
        lettre.configure(border_color = "gray")
    if filliere == "":
        filliere_champ.configure(border_color = "red")
        validation = False
    else:
        filliere_champ.configure(border_color = "gray")  
        validation = True
    print(validation)  
        
    
    

# Creation de la fenetre principale
window = customtkinter.CTk()
window.title("Home")
#window.resizable(False, False)
window.geometry("1080x580")

# Ouverture des images

image_info = Image.open(r'images/info.png')
image_info.thumbnail((30, 30), Image.ANTIALIAS)
photo_info = ImageTk.PhotoImage(image_info)
image_logo_esis = Image.open(r'images/esislogo.png')
image_logo_esis.thumbnail((300, 300), Image.ANTIALIAS)
photo_logo_esis = ImageTk.PhotoImage(image_logo_esis)
image_etudiant = Image.open(r'images\eleves_heureux.jpg')
image_etudiant.thumbnail((500, 500), Image.ANTIALIAS)
photo_etudiant = ImageTk.PhotoImage(image_etudiant)


# Integration du Scrollable Frame || Permettant de scroller sur la fenetre
canvas = customtkinter.CTkCanvas(window, bd=0, highlightthickness=0)
canvas.configure(background=window.cget("background") )

# frame_scrollable est la frame principale du programme
frame_scrollable = customtkinter.CTkFrame(canvas, fg_color='transparent')
frame_scrollable.pack(expand = YES)

# Fonction affichant le formulaire d'inscriptiion
def Rejoindre_ESIS():
    frame_home.pack_forget()
    frame__label_inscription.pack(expand = YES)
    frame_identites.pack(expand = YES)  
    #frame_decouvrir_esis.pack_forget()
    frame_rejoindre.pack_forget()
    frame_decouvrir_esis.pack_forget()
    frame_identites_suite.pack(expand = YES)
    frame_decouvrir_esis.pack(expand = YES)
    

    
frame_home = customtkinter.CTkFrame(frame_scrollable, fg_color="transparent")
frame_home.pack(expand = YES, pady = 10)
label_logo = customtkinter.CTkLabel(frame_home, image=photo_logo_esis, text=" ECOLE SUPERIEURE D'INFORMATIQUE \nSALAMA", compound="left", font=("arial", 30, 'bold'))
label_logo.grid(row=1, column=0)
frame_home_button = customtkinter.CTkFrame(frame_home, fg_color="transparent")
frame_home_button.grid(row=3, column=0)
button_rejoindre = customtkinter.CTkButton(frame_home_button, text="Rejoiniez Nous !", height=50, corner_radius=20, command=Rejoindre_ESIS)
button_rejoindre.grid(row=0, column=0, padx=10)
button_decouvrir = customtkinter.CTkButton(frame_home_button, text="Aller sur le site", height=50, corner_radius=20, fg_color="green")
button_decouvrir.grid(row=0, column=1)

# Section decouvrir ESIS
frame_decouvrir_esis = customtkinter.CTkFrame(frame_scrollable, fg_color="transparent")
frame_decouvrir_esis.pack(expand=True)
GENIE_LOGICIEL(frame_decouvrir_esis)
ADMINISTRATION_SYSTEME(frame_decouvrir_esis)
TELECOM(frame_decouvrir_esis)
DESIGN(frame_decouvrir_esis)

frame_rejoindre = customtkinter.CTkFrame(frame_scrollable, corner_radius=50)
frame_rejoindre.pack(expand=True)
label_design= customtkinter.CTkLabel(frame_rejoindre,text="            ", compound="left", font=("arial", 30, 'bold'))
label_design.grid(row=0,column=0, pady=20)

label_image_design= customtkinter.CTkLabel(frame_rejoindre, image=photo_etudiant, text="", compound="left", font=("arial", 30, 'bold'))
label_image_design.grid(row=1, column=0, padx=10)
button_rejoindre = customtkinter.CTkButton(frame_rejoindre, text="Rejoiniez Les Meilleurs !", height=50, corner_radius=20, command=Rejoindre_ESIS)
button_rejoindre.grid(row=1, column=1, padx=10)
distance = customtkinter.CTkLabel(frame_rejoindre, text="")
distance.grid(row = 3, column=2)
distance = customtkinter.CTkLabel(frame_decouvrir_esis, text="")
distance.grid(row = 5, column=2)

frame__label_inscription_dis = customtkinter.CTkFrame(frame_scrollable, fg_color="transparent")
frame__label_inscription_dis.pack(expand = True, pady = 10)
frame__label_inscription = customtkinter.CTkFrame(frame_scrollable, fg_color="transparent")
frame__label_inscription.pack(expand = True, pady = 10)

distance = customtkinter.CTkLabel(frame__label_inscription_dis, text="                                                               ")
distance.pack(expand = True, padx=50)

label_inscription = customtkinter.CTkLabel(frame__label_inscription, text="Fiche d'inscription", font=("arial", 20, 'bold'))
label_inscription.pack(expand = True, pady = 10)


# Identites
frame_identites = customtkinter.CTkFrame(frame_scrollable)
frame_identites.pack(expand = True)
frame_identites.pack_forget()
label_nom = customtkinter.CTkLabel(frame_identites, text= " Nom : ")
label_nom.grid(row=0, column=0, padx = 5)
entry_nom = customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_nom.grid(row = 0, column = 1, pady = 10, padx = 30)    

label_post = customtkinter.CTkLabel(frame_identites, text= " Post-nom : ")
label_post.grid(row=1, column=0, padx = 5, pady = 10)
entry_post = customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_post.grid(row = 1, column = 1, pady = 10, padx = 30)   

label_prenom = customtkinter.CTkLabel(frame_identites, text= " Prenom : ")
label_prenom.grid(row=2, column=0, padx = 5, pady = 10)
entry_prenom = customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_prenom.grid(row = 2, column = 1) 

label_date = customtkinter.CTkLabel(frame_identites, text= " Date de Naissance : ")
label_date.grid(row=3, column=0, padx = 5, pady = 10)
entry_date= customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_date.grid(row = 3, column = 1, padx = 30)   
entry_date.insert(0, "        /        /       ")

label_genre = customtkinter.CTkLabel(frame_identites, text= " Genre : ")
label_genre.grid(row=4, column=0, padx = 5, pady = 10)
entry_genre = customtkinter.CTkComboBox(frame_identites, values= ["", "Masculin", "Feminin"], width=200)
entry_genre.grid(row = 4, column = 1) 

label_etat = customtkinter.CTkLabel(frame_identites, text= " Etat Civil : ")
label_etat.grid(row=5, column=0, padx = 5, pady = 10)
entry_etat = customtkinter.CTkComboBox(frame_identites, values= ["", "Celibataire", "Marié(e)"], width=200)
entry_etat.grid(row = 5, column = 1) 

label_adresse = customtkinter.CTkLabel(frame_identites, text= " Adresse de résidence : ")
label_adresse.grid(row=6, column=0, padx = 5, pady = 10)
entry_adresse= customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_adresse.grid(row = 6, column = 1)   
entry_adresse.insert(0, "   av   / com  / ville   ")

label_numero = customtkinter.CTkLabel(frame_identites, text= " Téléphone : ")
label_numero.grid(row=7, column=0, padx = 5, pady = 10)
entry_numero = customtkinter.CTkEntry(frame_identites, width=200)
entry_numero.grid(row = 7, column = 1) 

label_email = customtkinter.CTkLabel(frame_identites, text= " E-mail : ")
label_email.grid(row=8, column=0, padx = 5, pady = 10)
entry_email = customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_email.grid(row = 8, column = 1) 
# Info sup

label_etablissement = customtkinter.CTkLabel(frame_identites, text= " Etablissement : ")
label_etablissement.grid(row=0, column=2, padx = 5, pady = 10)
entry_etablissement = customtkinter.CTkComboBox(frame_identites, values= ["", "ITI SAINT FRANCOIS XAVIER", "IT SALAMA"], width=200)
entry_etablissement.grid(row = 0, column = 3) 

label_option = customtkinter.CTkLabel(frame_identites, text= " Année Obtention Diplome : ")
label_option.grid(row=1, column=2, padx = 5, pady = 10)
entry_diplome = customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_diplome.grid(row = 1, column = 3) 

label_tel_respo = customtkinter.CTkLabel(frame_identites, text= " Telephone du responsable : ")
label_tel_respo.grid(row=2, column=2, padx = 5, pady = 10)
entry_tel_respo = customtkinter.CTkEntry(frame_identites, width=200, border_color="gray")
entry_tel_respo.grid(row = 2, column = 3, padx=20) 
label_filliere = customtkinter.CTkLabel(frame_identites, text= " Filliere : ")
label_filliere.grid(row=3, column=2, padx = 5, pady = 10)
filliere_champ = customtkinter.CTkComboBox(frame_identites, values=["","GENIE LOGICIEL", "ADMINISTRATION SYSTEME", "TELECOMMUNICATIONS", "DESIGN ET MULTIMEDIA"], width=200)
filliere_champ.grid(row=3, column=3)
label_diplome = customtkinter.CTkLabel(frame_identites, text="Diplome")
label_diplome.grid(row=4, column=2, padx=5)
charger_diplome_champ = customtkinter.CTkOptionMenu(frame_identites, values=["Charger diplome en PDF", "ignorer"], command=charger_diplome, corner_radius=0)
charger_diplome_champ.grid(row=4, column=3)
"""frame_assistant = customtkinter.CTkFrame(frame_identites, fg_color="transparent")
frame_assistant.grid(row = 8, column = 3) 

label_image_info = customtkinter.CTkLabel(frame_assistant, text="", image=photo_info)
label_image_info.grid(row=0, column=0)
texte_instructions = "Assistant \nLa lettre de motivation doit etre redigée en suivant certaines regles, suivez correctement les instructions pour rediger la lettre. vous avez la possiblité de charger un fichier Word ou TXT..."
lettre_instructions = customtkinter.CTkTextbox(frame_assistant, width=200, height=100, border_width=0, fg_color="#225AB3", wrap = WORD, corner_radius=20)
lettre_instructions.grid(row=0, column=1)
lettre_instructions.insert(END, texte_instructions)"""

frame_identites_suite = customtkinter.CTkFrame(frame_scrollable, fg_color="transparent")
frame_identites_suite.pack()
label_lettre = customtkinter.CTkLabel(frame_identites_suite, text="Lettre de Motivation", font=("arial", 15, 'bold'))
label_lettre.grid(row=0, column=0,pady = 10)
lettre = customtkinter.CTkTextbox(frame_identites_suite, width=500, height=300, border_width=2, corner_radius=0, border_color="gray")
lettre.grid(row=1, column=0, pady = 10, padx = 10)

label_image_info = customtkinter.CTkLabel(frame_identites_suite, text="", image=photo_info)
label_image_info.grid(row=1, column=2)
texte_instructions = "Assistant \nLa lettre de motivation doit etre redigée en suivant certaines regles, suivez correctement les instructions pour rediger la lettre. vous avez la possiblité de charger un fichier Word ou TXT..."
lettre_instructions = customtkinter.CTkTextbox(frame_identites_suite, width=250, height=150, border_width=0, fg_color="#225AB3", wrap = WORD, corner_radius=20)
lettre_instructions.grid(row=1, column=3, pady = 10)
lettre_instructions.insert(END, texte_instructions)
frame_commandes = customtkinter.CTkFrame(frame_identites_suite,fg_color="transparent")
frame_commandes.grid(row=2, column=0,padx=10)
charger_fichier = customtkinter.CTkButton(frame_commandes, text="Charger fichier", command=open_file)
charger_fichier.grid(row=0, column=0,padx=10)
valider = customtkinter.CTkButton(frame_commandes, text="valider", command=valider_formulaire)
valider.grid(row=0, column=1)
distance_command = customtkinter.CTkLabel(frame_commandes, text="")
distance_command.grid(row=1, column=0)   

frame_identites_suite.pack_forget()
frame__label_inscription.pack_forget()
# Coloration des widjet en fonction du focus

def on_get(event):
    lettre.configure(border_color='blue')
def out_get(event):
    lettre.configure(border_color='gray')
lettre.bind("<FocusIn>", on_get)
lettre.bind("<FocusOut>", out_get) 

def on_get_entry_nom(event):
    entry_nom.configure(border_color='blue')
def out_get_entry_nom(event):
    entry_nom.configure(border_color='gray')
entry_nom.bind("<FocusIn>", on_get_entry_nom)
entry_nom.bind("<FocusOut>", out_get_entry_nom) 

# Creation du scoll et integration du canvas dans la frame_scollable
scroll = customtkinter.CTkScrollbar(window, orientation='vertical', command=canvas.yview)
scroll.pack(side = 'right', fill='y')
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(expand=True, fill='both')
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 *(event.delta / 120)), "units"))
frame_scrollable.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=frame_scrollable,anchor='nw' )

window.mainloop()
