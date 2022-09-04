import tkinter
from tkinter import *
import os


class MainWindow:

    def __init__(self, **kwargs):
        self.graph_img = kwargs.pop("graph_img")
        self.master = kwargs.pop("master")
        self.canvas = Canvas(self.master, width=kwargs.pop("width"),
                             height=kwargs.pop("height"))
        self.canvas.place(x=0, y=0)
        self.graph_range = [500, 580,3]

        self.number_text_var = StringVar()

        self.canvas.create_image(0, 0, image=kwargs.pop("background"), anchor="nw")
        self.canvas.create_text(400, 100, text="Poryecto 1\nDiseño Lógico")

        self.start_button = Button(self.canvas, text="Prueba", command=self.start_button_fun)
        self.start_button.place(x=500, y=200)

        self.text_entry = Entry(self.canvas, textvariable=self.number_text_var)
        self.text_entry.place(x=600, y=200)

    def start_button_fun(self):
        temp_var = self.number_text_var.get()
        self.text_entry.delete(0, tkinter.END)
        self.canvas.create_image(20,500-10,image=self.graph_img,anchor="nw")
        self.create_graphics(temp_var)

    def create_graphics(self, numbers_list):
        counter = 1

        cambio = True
        for i in numbers_list:
            if i == "1":
                cambio = not cambio
            if cambio:
                self.canvas.create_line((80*(counter-1))+20, self.graph_range[0],
                                    80*counter+20, self.graph_range[0], width=5)
            else:
                self.canvas.create_line((80 * (counter - 1))+20, self.graph_range[1],
                                        80 * counter+20, self.graph_range[1], width=5)
       #     self.canvas.create_line(80, 500, 80, 580, width=5)
            counter += 1

