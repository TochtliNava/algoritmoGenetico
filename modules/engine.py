from tkinter import *

from res.values import colors
from modules.log import log
from modules.cromosoma import cromosoma
from modules.functions import generate, draw

class Engine:

    def __init__(self, root):

        self.upper_row = Frame(root, bg=colors.WHITE)
        self.upper_row.pack(side=TOP, fill=X, expand=True)

        self.button_start = Button(self.upper_row, text="Generar", font=("Arial", 12), command=lambda:self.step(lambda:self.start()))
        self.button_start.pack(side=LEFT, expand=True, padx=2)

        self.button_breed = Button(self.upper_row, text="Cruce", font=("Arial", 12), command=lambda:self.step(lambda:self.breeding()))
        self.button_breed.pack(side=LEFT, expand=True, padx=2)

        self.button_mutation = Button(self.upper_row, text="Mutacion", font=("Arial", 12), command=lambda:self.step(lambda:self.mutation()))
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

    def check(self):
        if(cromosoma.getLength()%2 == 1 or cromosoma.getSize()%2 == 1):
            self.button_breed["state"] = "disable"
        if(cromosoma.getLength()%2 == 0 and cromosoma.getSize()%2 == 0):
            self.button_breed["state"] = "active"

    def step(self, function):
        log.clear()
        function()
        self.check()
        
    def start(self):
        generate(self.frame, self.capture)

    def mutation(self):
        cromosoma.mutate()
        draw(self.frame)

    def breeding(self):
        cromosoma.breed()
        draw(self.frame)