import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import Bases.Bases as b
import Hamming.Hamming as h


class MainWindow:

    def __init__(self, **kwargs):
        self.graph_img = kwargs.pop("graph_img")
        self.master = kwargs.pop("master")
        self.canvas = Canvas(self.master, width=kwargs.pop("width"),
                             height=kwargs.pop("height"))
        self.canvas.place(x=0, y=0)
        self.graph_range = [500, 580, 3]
        self.ps = ["p1", "p2", "p3", "p4", "p5"]

        self.number_text_var = StringVar()

        self.bases = b.Bases()
        self.hamming = h.Hamming()

        self.canvas.create_image(0, 0, image=kwargs.pop("background"), anchor="nw")
        self.canvas.create_text(160, 80, text="Proyecto 1\nDiseño Lógico", font="Century 30", fill="white")

        self.start_button = Button(self.canvas, text="Convertir", command=self.start_button_fun)
        self.start_button.place(x=500, y=100)

        self.text_entry = Entry(self.canvas, textvariable=self.number_text_var)
        self.text_entry.place(x=600, y=100)

        self.results = ()

        self.comprobar_var = StringVar()
        self.text_entry_comrpobar = Entry(self.canvas, textvariable=self.comprobar_var)
        self.text_entry_comrpobar.place(x=600, y=450)

        self.comprobar_button = Button(self.canvas, text="Comprobar", command=self.comprobar)
        self.comprobar_button.place(x=500, y=450)

        self.cambiar_paridad_button = Button(self.canvas,text="Cambiar Paridad",command=self.cambiar_paridad)
        self.cambiar_paridad_label = Label(self.canvas,text="Paridad Par")
        self.cambiar_paridad_button.place(x=200,y=450)
        self.cambiar_paridad_label.place(x=300,y=450)



    def cambiar_paridad(self):
        self.hamming.paridadPar = not self.hamming.paridadPar
        if self.hamming.paridadPar:
            self.cambiar_paridad_label['text']= "Paridad Par"
        else:
            self.cambiar_paridad_label['text'] = "Paridad Impar"

    def comprobar(self):
        self.text_entry_comrpobar.delete(0, tkinter.END)
        # print("ff"+self.comprobar_var.get())
        # self.hamming.calcParityBitsForError(self.comprobar_var.get())

    def start_button_fun(self):
        temp_var = self.number_text_var.get()
        self.text_entry.delete(0, tkinter.END)

        if self.bases.is_valid(str(temp_var)):
            self.results = self.bases.conversion(str(temp_var))
            self.canvas.create_image(20 - 2, 500 - 10, image=self.graph_img, anchor="nw")
            self.create_graphics(self.results[1])
            print(self.results)

            self.canvas.create_rectangle(750, 100, 980, 300, fill="white")

            self.canvas.create_text(867, 130, text="Octal = " + str(temp_var), font="Arial 15")
            self.canvas.create_text(867, 170, text="Decimal = " + str(self.results[0]), font="Arial 15")
            self.canvas.create_text(867, 210, text="Hexadecimal = " + str(self.results[2]), font="Arial 15")
            self.canvas.create_text(867, 250, text="Binario = " + str(self.results[1]), font="Arial 15")

            self.text_entry_comrpobar.insert(0,str(self.results[1]))

            temp_result_hamming = self.hamming.start(str(self.results[1]))

            self.canvas.create_rectangle(20, 150, 700, 400, fill="white")
            temp_counter = 0
            for i in temp_result_hamming:
                text = Label(self.canvas, text=i, bg="white", font="Arial")
                text.place(x=50, y=160 + (20 * temp_counter))
                # self.canvas.create_text(80,160+(10*temp_counter),text=i,font="Arial 12",justify=RIGHT)
                temp_counter += 1


        else:
            messagebox.showerror(message="El texto insertado no corresponde a un "
                                         "número octal o está fuera del rango, debe"
                                         " ser menor o igual a 777",
                                 title="Error al insertar el número")

    def create_graphics(self, numbers_list):
        counter = 1
        tempX = 20
        tempY = self.graph_range[0]
        cambio = True
        for i in numbers_list:
            if i == "1":
                cambio = not cambio
            if cambio:
                if counter != 1:
                    self.canvas.create_line(tempX, tempY, (80 * (counter - 1)) + 20,
                                            self.graph_range[0], width=5)
                self.canvas.create_line((80 * (counter - 1)) + 20, self.graph_range[0],
                                        80 * counter + 20, self.graph_range[0], width=5)
                tempX = 80 * counter + 20
                tempY = self.graph_range[0]
            else:
                self.canvas.create_line(tempX, tempY, (80 * (counter - 1)) + 20,
                                        self.graph_range[1], width=5)
                self.canvas.create_line((80 * (counter - 1)) + 20, self.graph_range[1],
                                        80 * counter + 20, self.graph_range[1], width=5)
                tempX = 80 * counter + 20
                tempY = self.graph_range[1]
            counter += 1
