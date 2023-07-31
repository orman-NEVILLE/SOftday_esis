import customtkinter
from tkinter import*
from PIL import Image, ImageTk

def GENIE_LOGICIEL(frame_decouvrir_esis):
    image_genie_logiciel = Image.open(r'images\Software-Engineering-1-840x628.jpg')
    image_genie_logiciel.thumbnail((300, 300), Image.ANTIALIAS)
    photo_genie_logiciel = ImageTk.PhotoImage(image_genie_logiciel)
    # SECTION SOFTWARE ENGINEERING
    frame_software_engineering = customtkinter.CTkFrame(frame_decouvrir_esis, corner_radius=20, fg_color="#DFFAAA")
    frame_software_engineering.grid(row=0, column = 0, pady = 10, padx = 5)
    label_GL = customtkinter.CTkLabel(frame_software_engineering,text=" GENIE LOGICIEL ET MSI  \n", compound="left", font=("arial", 30, 'bold'))
    label_GL.grid(row=0,column=0, pady=10)

    label_image_GL = customtkinter.CTkLabel(frame_software_engineering, image=photo_genie_logiciel, text="", compound="left", font=("arial", 30, 'bold'))
    label_image_GL.grid(row=1, column=0, padx=10)
    
    label__GL = customtkinter.CTkLabel(frame_software_engineering, text="GL", compound="left", font=("arial", 20, 'bold'))
    label__GL.grid(row=2, column=0, padx=10)
    
    texte_sur_GL = customtkinter.CTkTextbox(frame_software_engineering, width=250, height=200, wrap=WORD , fg_color="#B2B4DB")
    texte_sur_GL.grid(row=3, column=0, pady=5)
    label__msi = customtkinter.CTkLabel(frame_software_engineering, text="MSI", compound="left", font=("arial", 20, 'bold'))
    label__msi.grid(row=4, column=0, padx=10)
    texte_sur_msi = customtkinter.CTkTextbox(frame_software_engineering, width=250, height=200, wrap=WORD , fg_color="gray")
    texte_sur_msi.grid(row=5, column=0, pady=5)
    
    bouton_savoir_plus = customtkinter.CTkButton(frame_software_engineering,text="En Savoir +", height=50, corner_radius=20)
    bouton_savoir_plus.grid(row=6, column=0)
    texte_gl = """
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet."""
    texte_sur_GL.insert(END, texte_gl)
    texte_sur_GL.configure(state = "disable")
    texte_sur_msi.insert(END, texte_gl)
    
    distance = customtkinter.CTkLabel(frame_software_engineering, text="")
    distance.grid(row = 4, column=0)