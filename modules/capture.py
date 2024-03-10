from tkinter import *

from res.values import colors

class Capture:
        
        def __init__(self, root):
                
                self.size_frame = Frame(root, bg=colors.WHITE)
                self.size_frame.pack(side=TOP, fill=BOTH, padx=5, expand=True)

                self.size_label = Label(self.size_frame, text="Tamaño del cromosoma", font=("Arial", 15), bg=colors.WHITE)
                self.size_label.pack(side=LEFT, fill=X)

                self.size = Entry(self.size_frame, justify=RIGHT, bg=colors.WHITE)
                self.size.pack(side=LEFT, fill=X, expand=True)
                self.size.focus()

                # -------------------------------

                self.quantity_frame = Frame(root, bg=colors.WHITE)
                self.quantity_frame.pack(side=TOP, fill=BOTH, padx=5, expand=True)

                self.quantity_label = Label(self.quantity_frame, text="Tamaño de la poblacion", font=("Arial", 15), bg=colors.WHITE)
                self.quantity_label.pack(side=LEFT, fill=X)

                self.quantity = Entry(self.quantity_frame, justify=RIGHT, bg=colors.WHITE)
                self.quantity.pack(side=LEFT, fill=X, expand=True)
        
                # ---------------------------------

                self.gen_frame = Frame(root, bg=colors.WHITE)
                self.gen_frame.pack(side=TOP, fill=BOTH, padx=5, expand=True)

                self.gen_label = Label(self.gen_frame, text="Numero de Generaciones", font=("Arial", 15), bg=colors.WHITE)
                self.gen_label.pack(side=LEFT, fill=X)

                self.gen = Entry(self.gen_frame, justify=RIGHT, bg=colors.WHITE)
                self.gen.pack(side=LEFT, fill=X, expand=True)
        
        def getSize(self):
                return int(self.size.get())

        def getQuantity(self):
                return int(self.quantity.get())

        def getGen(self):
                return int(self.gen.get())