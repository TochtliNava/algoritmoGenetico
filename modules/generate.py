from tkinter import *
import random

from modules.getInputs import getSize, getQuantity, getGen
from modules.cromosomas import clearCromosomas

def generar(frame):

    clearCromosomas()

    frame.delete(1.0, END)

    for _ in range(getQuantity()):
        temp_cromosoma = ""

        for _ in range(getSize()):
            temp_cromosoma = temp_cromosoma + str(random.randint(0,1))

        frame.insert(INSERT, temp_cromosoma)
        frame.insert(INSERT, "\n")