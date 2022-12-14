import GUI.MainWindow as MainWindow
from tkinter import *

width = 1000
height = 600

if __name__ == '__main__':
    master = Tk()
    master.title("Proyecto Diseño Lógico")
    master.geometry(str(width) + "x" + str(height))
    master.resizable(False,False)

    background = PhotoImage(file="Images/Background.gif")
    graph_img = PhotoImage(file="Images/graph.gif")

    mainWindow = MainWindow.MainWindow(master=master, width=width,
                                       height=height,background=background,
                                       graph_img=graph_img)
    master.mainloop()
