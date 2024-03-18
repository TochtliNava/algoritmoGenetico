from tkinter import *
from tkinter import scrolledtext

from modules.capture import Capture
from modules.engine import Engine
from modules.log import log
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

# --------Log Frame----------------

left_top_log = Frame(left_frame, bg=colors.WHITE)
left_top_log.pack(side=TOP, fill=BOTH, expand=True)
left_top_log.pack_propagate(False)

log_top = Frame(left_top_log, bg=colors.LIGHT, height=60)
log_top.pack(side=TOP, fill=X)

log_label = Label(log_top, text="Log", bg=colors.LIGHT)
log_label.pack()

hscrollbar = Scrollbar(left_top_log, orient=HORIZONTAL)
vscrollbar = Scrollbar(left_top_log, orient=VERTICAL)

log_content = Listbox(
    left_top_log,
    xscrollcommand=hscrollbar.set,
    yscrollcommand=vscrollbar.set
)
hscrollbar.config(command=log_content.xview)
hscrollbar.pack(side=BOTTOM, fill=X)
vscrollbar.config(command=log_content.yview)
vscrollbar.pack(side=RIGHT, fill=Y)
log_content.pack(side=LEFT, fill=BOTH, expand=True)

log.setContent(log_content)
log.write("Creado por:")
log.write("Ezequiel Alejandro Nava Alonso (TochtliNava)!")
log.write("(●'◡'●)")

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

# -------------------Cromosomas frame con scroll---------------

hscrollbar = Scrollbar(lower_frame, orient=HORIZONTAL)
vscrollbar = Scrollbar(lower_frame, orient=VERTICAL)

cromosoma = Listbox(
    lower_frame,
    xscrollcommand=hscrollbar.set,
    yscrollcommand=vscrollbar.set
)
hscrollbar.config(command=cromosoma.xview)
hscrollbar.pack(side=BOTTOM, fill=X)
vscrollbar.config(command=cromosoma.yview)
vscrollbar.pack(side=RIGHT, fill=Y)
cromosoma.pack(side=LEFT, fill=BOTH, expand=True)

engine = Engine(buttons_frame)
engine.setRenderFrame(cromosoma)
engine.setCapture(capture)

root.mainloop()