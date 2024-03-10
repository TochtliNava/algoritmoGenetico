from tkinter import *
import random

from modules.cromosoma import cromosoma

def Generate(render, capture):

    cromosoma.clearCromosomas()
    cromosoma.clearFitness()

    render.delete(1.0, END)

    for x in range(int(capture.getQuantity())):
        temp_cromosoma = ""

        for _ in range(int(capture.getSize())):
            temp_cromosoma = temp_cromosoma + str(random.randint(0,1))

        render.insert(INSERT, f"{x + 1} : {temp_cromosoma} Fitness: {cromosoma.getFitness(temp_cromosoma)}")
        render.insert(INSERT, "\n")
        cromosoma.addFitness(temp_cromosoma)
        cromosoma.addCromosoma(temp_cromosoma)

