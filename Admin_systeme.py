import customtkinter
from tkinter import*
from PIL import Image, ImageTk
def ADMINISTRATION_SYSTEME(frame_decouvrir_esis):
    image_genie_administration_systeme = Image.open(r'images/Administrateur-description-du-métier.jpg')
    image_genie_administration_systeme.thumbnail((250, 250), Image.ANTIALIAS)
    photo_genie_administration_systeme = ImageTk.PhotoImage(image_genie_administration_systeme)
    # SECTION ADMINISTRATION SYSTEME
    frame_software_administration_systeme = customtkinter.CTkFrame(frame_decouvrir_esis, fg_color="#ACDAEA" , corner_radius=20)
    frame_software_administration_systeme.grid(row=0, column = 1, pady = 10, padx = 5)
    label_AS = customtkinter.CTkLabel(frame_software_administration_systeme,text=" ADMINISTRATION\n SYSTEME  \n", compound="left", font=("arial", 30, 'bold'))
    label_AS.grid(row=0,column=0, pady=20)

    label_image_AS = customtkinter.CTkLabel(frame_software_administration_systeme, image=photo_genie_administration_systeme, text="", compound="left", font=("arial", 30, 'bold'))
    label_image_AS.grid(row=1, column=0, padx=10)

    texte_sur_AS = customtkinter.CTkTextbox(frame_software_administration_systeme, width=270, height=300, wrap=WORD, fg_color="transparent")
    texte_sur_AS.grid(row=2, column=0)
    bouton_savoir_plus = customtkinter.CTkButton(frame_software_administration_systeme,text="En Savoir +", height=50, corner_radius=20, fg_color="gray")
    bouton_savoir_plus.grid(row=3, column=0)
    texte_as = """
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet."""
    texte_sur_AS.insert(END, texte_as)
    texte_sur_AS.configure(state = "disable")
    distance = customtkinter.CTkLabel(frame_software_administration_systeme, text="")
    distance.grid(row = 4, column=0)