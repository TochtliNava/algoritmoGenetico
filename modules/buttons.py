from tkinter import *

from modules.generate import generar

from res.values import colors

def castButtonFrame(root, main, cromosoma):

    # -----------------------------------

    upper_row = Frame(root, bg=colors.WHITE)
    upper_row.pack(side=TOP, fill=X, expand=True)

    button_start = Button(upper_row, text="Generar", font=("Arial", 12), command=lambda:generar(cromosoma))
    button_start.pack(side=LEFT, expand=True, padx=2)

    button_breed = Button(upper_row, text="Cruce", font=("Arial", 12))
    button_breed.pack(side=LEFT, expand=True, padx=2)

    button_mutation = Button(upper_row, text="Mutacion", font=("Arial", 12))
    button_mutation.pack(side=LEFT, expand=True, padx=2)

    # --------------------------------------

    lower_row = Frame(root, bg=colors.WHITE)
    lower_row.pack(side=TOP, fill=X, expand=True)

    button_selection = Button(lower_row, text="Seleccion", font=("Arial", 12))
    button_selection.pack(side=LEFT, expand=True, padx=2)

    button_next = Button(lower_row, text="Siguiente", font=("Arial", 12))
    button_next.pack(side=LEFT, expand=True, padx=2)

    button_exit = Button(lower_row, text="Salir", font=("Arial", 12), command=lambda:main.destroy())
    button_exit.pack(side=LEFT, expand=True, padx=2)