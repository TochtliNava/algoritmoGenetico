from tkinter import *

class Log:

    def __init__(self) -> None:
        pass

    def setContent(self, content):
        self.content = content
    
    def write(self, content):
        self.content.insert(END, content)
        self.content.insert(END, "\n")

    def clear(self):
        self.content.delete(0, END)

log = Log()