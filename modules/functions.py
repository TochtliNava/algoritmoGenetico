from tkinter import *
import random

from modules.cromosoma import cromosoma

def generate(content, capture):

    cromosoma.clearCromosomas()
    cromosoma.clearFitness()
    cromosoma.clearTag()
    cromosoma.setLength(capture.getSize())

    content.delete(0, END)

    for x in range(int(capture.getQuantity())):
        temp_cromosoma = ""
        cromosoma.addTag(str(x + 1))
        for _ in range(int(capture.getSize())):
            temp_cromosoma = temp_cromosoma + str(random.randint(0,1))
        content.insert(END, f"{cromosoma.tag[x]} : {temp_cromosoma} Fitness: {cromosoma.getFitness(temp_cromosoma)}")
        content.insert(END, "\n")
        cromosoma.addFitness(temp_cromosoma)
        cromosoma.addCromosoma(temp_cromosoma)

def draw(content):

    content.delete(0, END)

    for c in range(cromosoma.getSize()):
        content.insert(END, f"{cromosoma.tag[c]} : {cromosoma.cromosomas[c]} Fitness: {cromosoma.getFitness(cromosoma.cromosomas[c])}")
        content.insert(END, "\n")

