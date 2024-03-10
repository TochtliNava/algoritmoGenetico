from tkinter import *
from tkinter import scrolledtext

from modules.capture import Capture
from modules.render import Engine
from res.values import colors

root = Tk()
root.title("Algoritmo genético")

width = 900
height = 500

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

center_x = int(width_screen//2 - width//2)
center_y = int(height_screen//2 - height//2)

root.geometry(f"{width}x{height}+{center_x}+{center_y}")
root.resizable(False, False)
root.config(bg=colors.BACKGROUND)

main_frame = Frame(root, bg=colors.BACKGROUND)
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

left_frame = Frame(main_frame, bg=colors.BACKGROUND)
left_frame.pack(side=LEFT, fill=BOTH, expand=True)

# -------Data Frame------------

left_top_data = Frame(left_frame, bg=colors.WHITE)
left_top_data.pack(side=TOP, fill=BOTH, expand=True)
left_top_data.pack_propagate(False)

data_top = Frame(left_top_data, bg=colors.LIGHT, height=60)
data_top.pack(side=TOP, fill=X)

data_top_label = Label(data_top, text="Datos", bg=colors.LIGHT)
data_top_label.pack()

data_frame = Frame(left_top_data, bg=colors.WHITE)
data_frame.pack(side=TOP, fill=BOTH, expand=True)
data_frame.pack_propagate(False)

capture = Capture(data_frame)

# -------Buttons Frame------------

left_top_button = Frame(left_frame, bg=colors.WHITE)
left_top_button.pack(side=TOP, fill=BOTH, expand=True, pady=10)
left_top_button.pack_propagate(False)

comandos_top = Frame(left_top_button, bg=colors.LIGHT, height=60)
comandos_top.pack(side=TOP, fill=X)

comandos_label = Label(comandos_top, text="Comandos", bg=colors.LIGHT)
comandos_label.pack()

buttons_frame = Frame(left_top_button, bg=colors.WHITE)
buttons_frame.pack(side=TOP, fill=BOTH, expand=True)
buttons_frame.pack_propagate(False)



# --------Filler Frame----------------

left_top_blank = Frame(left_frame, bg=colors.BACKGROUND)
left_top_blank.pack(side=TOP, fill=BOTH, expand=True)

# ---------middle filler Frame--------------

middle_frame = Frame(main_frame, bg=colors.BACKGROUND, width=10)
middle_frame.pack(side=LEFT, fill=Y)

# --------Poblacion Frame---------------

right_frame = Frame(main_frame, bg=colors.WHITE)
right_frame.pack(side=LEFT, fill=BOTH, expand=True)

upper_frame = Frame(right_frame, bg="red", height=25)
upper_frame.pack(side=TOP, fill=X)

labels_frame = Frame(upper_frame, bg=colors.LIGHT, height=25)
labels_frame.pack(side=TOP, fill=X)

cromosoma_label = Label(labels_frame, text="Cromosoma", bg=colors.LIGHT)
cromosoma_label.pack(side=LEFT, fill=X, expand=True)

lower_frame = Frame(right_frame, bg="blue")
lower_frame.pack(side=TOP, fill=BOTH, expand=True)
lower_frame.pack_propagate(False)

cromosoma = scrolledtext.ScrolledText(lower_frame, width=53)
cromosoma.pack(side=LEFT, fill=BOTH, expand=True)

engine = Engine(buttons_frame)
engine.setRenderFrame(cromosoma)
engine.setCapture(capture)

root.mainloop()