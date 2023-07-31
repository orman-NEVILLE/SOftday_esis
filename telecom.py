import customtkinter
from tkinter import*
from PIL import Image, ImageTk

def TELECOM(frame_decouvrir_esis):
    image_telecom = Image.open(r'images/Telecoms.png')
    image_telecom.thumbnail((250, 250), Image.ANTIALIAS)
    photo_telecom = ImageTk.PhotoImage(image_telecom)
    # SECTION TELECOMMUNICATION
    frame_software_telecom = customtkinter.CTkFrame(frame_decouvrir_esis, fg_color="#B5FAAC", corner_radius=20)
    frame_software_telecom.grid(row=0, column = 2, padx=10)
    label_telecom = customtkinter.CTkLabel(frame_software_telecom,text="\n TELECOMMUNICATIONS \n\n\n", compound="left", font=("arial", 30, 'bold'))
    label_telecom.grid(row=0,column=0)

    label_image_telecom = customtkinter.CTkLabel(frame_software_telecom, image=photo_telecom, text="", compound="left", font=("arial", 30, 'bold'))
    label_image_telecom.grid(row=1, column=0, padx=10)

    texte_sur_telecom = customtkinter.CTkTextbox(frame_software_telecom, width=250, height=300, wrap=WORD, fg_color="transparent")
    texte_sur_telecom.grid(row=2, column=0)
    bouton_savoir_plus = customtkinter.CTkButton(frame_software_telecom,text="En Savoir +", height=50, corner_radius=20, fg_color="green")
    bouton_savoir_plus.grid(row=3, column=0)
    texte_telecom = """
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet.
    Le génie logiciel est une discipline qui concerne la conception, le développement et la maintenance de logiciels de qualité. Il englobe des activités telles que l'analyse des besoins, la conception de l'architecture logicielle, la programmation, les tests et la gestion de projet."""
    texte_sur_telecom.insert(END, texte_telecom)
    texte_sur_telecom.configure(state= "disable")
    distance = customtkinter.CTkLabel(frame_software_telecom, text="")
    distance.grid(row = 3, column=0)