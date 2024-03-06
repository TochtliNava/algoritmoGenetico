from tkinter import *

from res.values import colors

def castDataFrame(root_frame):

    global size
    global quantity
    global gen

    size_frame = Frame(root_frame, bg=colors.WHITE)
    size_frame.pack(side=TOP, fill=BOTH, padx=5, expand=True)

    size_label = Label(size_frame, text="Tamaño del cromosoma", font=("Arial", 15), bg=colors.WHITE)
    size_label.pack(side=LEFT, fill=X)

    size = Entry(size_frame, justify=RIGHT, bg=colors.WHITE)
    size.pack(side=LEFT, fill=X, expand=True)
    size.focus()

    # --------------------------------

    quantity_frame = Frame(root_frame, bg=colors.WHITE)
    quantity_frame.pack(side=TOP, fill=BOTH, padx=5, expand=True)

    quantity_label = Label(quantity_frame, text="Tamaño de la poblacion", font=("Arial", 15), bg=colors.WHITE)
    quantity_label.pack(side=LEFT, fill=X)

    quantity = Entry(quantity_frame, justify=RIGHT, bg=colors.WHITE)
    quantity.pack(side=LEFT, fill=X, expand=True)

    # ---------------------------------

    gen_frame = Frame(root_frame, bg=colors.WHITE)
    gen_frame.pack(side=TOP, fill=BOTH, padx=5, expand=True)

    gen_label = Label(gen_frame, text="Numero de Generaciones", font=("Arial", 15), bg=colors.WHITE)
    gen_label.pack(side=LEFT, fill=X)

    gen = Entry(gen_frame, justify=RIGHT, bg=colors.WHITE)
    gen.pack(side=LEFT, fill=X, expand=True)

def getSizeWidget():
        return size

def getQuantityWidget():
        return quantity

def getGenWidget():
        return gen