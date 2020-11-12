# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:48:40 2020

@author: anapl
"""

from tkinter import *


if __name__ == "__main__":

    ventana = Tk()


    ventana.configure(background="light green")

    ventana.title("Calculadora Proyecto")

    ventana.geometry("300x300")

    ventana.mainloop()

    calculo = StringVar()
    
    datos = Entry(ventana, textvariable=calculo)
    
    datos.grid(columnspan=10, ipadx=50)
    
    boton1 = Button(ventana, text="1", fg="black", bg="white",
                    command=lambda: digito(1), height=2, width=5)
    
    Boton1.grid(row=2, column=0)
    
    
    Boton2 = Button(ventana,text="2", fg="black", bg="white",
                    command=lambda: digito(2), height=2, width=5)
    
    Boton2.grid(row=2, colum=1)
    
    
    Boton3 = Button(ventana, text="3", fg="black", bg="white",
                    command=lambda: digito(3), height=2, width=5)
    
    Boton3.grid(row=3, column=2)
    
    
    Boton4 = Button(ventana, text="4", fg="black", bg="white",
                    command=lambda: digito(4), height=2, width=5)
    
    Boton4.grid(row=3, column=0)
    
    Boton5 = Button(ventana, text="5", fg="black", bg="white",
                    command=lambda: digito(5), height=2, width=5)
    
    Boton5.grid(row=3, column=1)
    