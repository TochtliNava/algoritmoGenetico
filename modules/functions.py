from tkinter import *
import random

from modules.cromosoma import cromosoma

def generate(content, capture):

    cromosoma.clearCromosomas()
    cromosoma.clearFitness()
    cromosoma.clearTag()
    cromosoma.resetGen()
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

    cromosoma.clearFitness()
    content.delete(0, END)

    for c in range(cromosoma.getSize()):
        content.insert(END, f"{cromosoma.tag[c]} : {cromosoma.cromosomas[c]} Fitness: {cromosoma.getFitness(cromosoma.cromosomas[c])}")
        content.insert(END, "\n")
        cromosoma.addFitness(cromosoma.cromosomas[c])

def select():

    def s(n):
        s = int(n.get())
        n.winfo_toplevel().destroy()
        cromosoma.select(s)

    select = Toplevel()
    n_frame = LabelFrame(select, text="Cuantos cromosomas serán seleccionados?")
    n_frame.pack()
    n = Entry(n_frame)
    n.focus()
    n.pack(side=LEFT, fill=X, expand=True)
    b = Button(n_frame, text="OK", command=lambda:s(n))
    b.pack(side=LEFT)
    select.wait_window()
