from tkinter import *

from res.values import colors
from modules.cromosoma import cromosoma
from modules.generate import Generate

class Engine:

    def __init__(self, root):

        self.upper_row = Frame(root, bg=colors.WHITE)
        self.upper_row.pack(side=TOP, fill=X, expand=True)

        self.button_start = Button(self.upper_row, text="Generar", font=("Arial", 12), command=self.start)
        self.button_start.pack(side=LEFT, expand=True, padx=2)

        self.button_breed = Button(self.upper_row, text="Cruce", font=("Arial", 12))
        self.button_breed.pack(side=LEFT, expand=True, padx=2)

        self.button_mutation = Button(self.upper_row, text="Mutacion", font=("Arial", 12))
        self.button_mutation.pack(side=LEFT, expand=True, padx=2)

        # --------------------------------------

        self.lower_row = Frame(root, bg=colors.WHITE)
        self.lower_row.pack(side=TOP, fill=X, expand=True)

        self.button_selection = Button(self.lower_row, text="Seleccion", font=("Arial", 12))
        self.button_selection.pack(side=LEFT, expand=True, padx=2)

        self.button_next = Button(self.lower_row, text="Siguiente", font=("Arial", 12))
        self.button_next.pack(side=LEFT, expand=True, padx=2)

        self.button_exit = Button(self.lower_row, text="Salir", font=("Arial", 12), command=lambda:root.winfo_toplevel().destroy())
        self.button_exit.pack(side=LEFT, expand=True, padx=2)
    
    def setRenderFrame(self, frame):
        self.frame = frame
    
    def setCapture(self, capture):
        self.capture = capture

    def start(self):
        Generate(self.frame, self.capture)
        if(cromosoma.getLength()%2 == 1):
            print("true")
            self.button_breed["state"] = "disable"
        if(cromosoma.getLength()%2 == 0):
            self.button_breed["state"] = "active"