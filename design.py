import customtkinter
from tkinter import*
from PIL import Image, ImageTk

def DESIGN(frame_decouvrir_esis):
    image_design = Image.open(r'images\conception-mot-ecrit-au-dessus-formes-3d-geometriques-colorees_2227-1663.jpg')
    image_design.thumbnail((250, 250), Image.ANTIALIAS)
    photo_design = ImageTk.PhotoImage(image_design)
    # SECTION DESIGN
    frame_software_design= customtkinter.CTkFrame(frame_decouvrir_esis, fg_color="pink", corner_radius=20)
    frame_software_design.grid(row=0, column = 3)
    label_design= customtkinter.CTkLabel(frame_software_design,text="\n DESIGN\n ET MULTIMEDIA\n", compound="left", font=("arial", 30, 'bold'))
    label_design.grid(row=0,column=0, pady=20)

    label_image_design= customtkinter.CTkLabel(frame_software_design, image=photo_design, text="", compound="left", font=("arial", 30, 'bold'))
    label_image_design.grid(row=1, column=0)

    texte_sur_design = customtkinter.CTkTextbox(frame_software_design, width=270, height=300, wrap=WORD, fg_color="transparent")
    texte_sur_design.grid(row=2, column=0)
    bouton_savoir_plus = customtkinter.CTkButton(frame_software_design,text="En Savoir +", height=50, corner_radius=20)
    bouton_savoir_plus.grid(row=3, column=0)
    texte_design = """
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet."""
    texte_sur_design.insert(END, texte_design)
    texte_sur_design.configure(state = "disable")
    distance = customtkinter.CTkLabel(frame_software_design, text="")
    distance.grid(row = 3, column=0, pady=20)