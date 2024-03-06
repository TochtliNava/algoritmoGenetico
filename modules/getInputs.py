from modules.inputs import getSizeWidget, getQuantityWidget, getGenWidget

def getSize():
    return int(getSizeWidget().get())

def getQuantity():
    return int(getQuantityWidget().get())

def getGen():
    return int(getGenWidget().get())