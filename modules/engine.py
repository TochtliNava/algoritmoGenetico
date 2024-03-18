from tkinter import *

from res.values import colors
from modules.log import log
from modules.cromosoma import cromosoma
from modules.functions import generate, draw, select

class Engine:

    def __init__(self, root):

        self.upper_row = Frame(root, bg=colors.WHITE)
        self.upper_row.pack(side=TOP, fill=X, expand=True)

        self.button_start = Button(self.upper_row, text="Generar", font=("Arial", 12), command=lambda:self.step(lambda:self.start()))
        self.button_start.pack(side=LEFT, expand=True, padx=2)

        self.button_breed = Button(self.upper_row, text="Cruce", font=("Arial", 12), command=lambda:self.step(lambda:self.breeding()))
        self.button_breed.pack(side=LEFT, expand=True, padx=2)
        self.button_breed["state"] = "disable"

        self.button_mutation = Button(self.upper_row, text="Mutacion", font=("Arial", 12), command=lambda:self.step(lambda:self.mutation()))
        self.button_mutation.pack(side=LEFT, expand=True, padx=2)
        self.button_mutation["state"] = "disable"

        # --------------------------------------

        self.lower_row = Frame(root, bg=colors.WHITE)
        self.lower_row.pack(side=TOP, fill=X, expand=True)

        self.button_selection = Button(self.lower_row, text="Seleccion", font=("Arial", 12), command=lambda:self.step(lambda:self.selection()))
        self.button_selection.pack(side=LEFT, expand=True, padx=2)
        self.button_selection["state"] = "disable"

        self.button_next = Button(self.lower_row, text="Siguiente", font=("Arial", 12), command=lambda:self.step(lambda:self.siguiente()))
        self.button_next.pack(side=LEFT, expand=True, padx=2)
        self.button_next["state"] = "disable"

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
        
    def start(self):
        generate(self.frame, self.capture)
        self.check()
        log.write(f"Generación {cromosoma.gen}")
        self.button_mutation["state"] = "active"
        self.button_selection["state"] = "disable"
        self.button_next["state"] = "disable"

    def mutation(self):
        cromosoma.mutate()
        self.button_selection["state"] = "active"
        self.button_breed["state"] = "disable"
        self.button_mutation["state"] = "disable"
        draw(self.frame)

    def breeding(self):
        cromosoma.breed()
        self.button_selection["state"] = "active"
        self.button_breed["state"] = "disable"
        self.button_mutation["state"] = "disable"
        draw(self.frame)
    
    def selection(self):
        self.button_selection["state"] = "disable"
        self.button_next["state"] = "active"
        select()
        draw(self.frame)

    def siguiente(self):
        self.button_start["state"] = "disable"
        self.button_mutation["state"] = "active"
        self.button_breed["state"] = "active"
        self.button_next["state"] = "disable"
        if(cromosoma.gen == self.capture.getGen() or cromosoma.getSize() == 1):
            self.stop()
        else:
            cromosoma.setGen(cromosoma.gen + 1)
            log.write(f"Generación {cromosoma.gen}")
            self.check()
    
    def stop(self):
        self.button_mutation["state"] = "disable"
        self.button_breed["state"] = "disable"
        self.button_selection["state"] = "disable"
        self.button_next["state"] = "disable"
        self.button_start["state"] = "active"
        log.write(f"El mejor fit es de: {cromosoma.getBest()}")