from tkinter import *
import random

from modules.cromosoma import cromosoma

def generate(frame, capture):

    cromosoma.clearCromosomas()
    cromosoma.clearFitness()
    cromosoma.setLength(capture.getSize())

    frame.delete(0, END)

    for x in range(int(capture.getQuantity())):
        temp_cromosoma = ""

        for _ in range(int(capture.getSize())):
            temp_cromosoma = temp_cromosoma + str(random.randint(0,1))

        frame.insert(END, f"{x + 1} : {temp_cromosoma} Fitness: {cromosoma.getFitness(temp_cromosoma)}")
        frame.insert(END, "\n")
        cromosoma.addFitness(temp_cromosoma)
        cromosoma.addCromosoma(temp_cromosoma)

def draw(frame):

    frame.delete(0, END)

    for c in range(cromosoma.getSize()):
        frame.insert(END, f"{c + 1} : {cromosoma.cromosomas[c]} Fitness: {cromosoma.getFitness(cromosoma.cromosomas[c])}")
        frame.insert(END, "\n")

