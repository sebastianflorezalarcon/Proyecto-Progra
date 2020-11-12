# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:26:58 2020

@author: USER
"""

from tkinter import *



boton = ""



def digito(num):
    
    global boton
    
    boton = boton + str(num)
    
    calculo.set(boton)
    
    
    
if __name__ == "__main__":

    ventana = Tk()


    ventana.configure(background="light green")

    ventana.title("Calculadora Proyecto")

    ventana.geometry("250x250")




    calculo = StringVar()
    
    datos = Entry(ventana, textvariable=calculo)
    
    datos.grid(columnspan=10, ipadx=50)
    
    
    boton1 = Button(ventana, text=' 1 ', fg='black', bg='white',

                     command=lambda: digito(1), height=2, width=5)

    boton1.grid(row=2, column=0)



    boton2 = Button(ventana, text=' 2 ', fg='black', bg='white',

                     command=lambda: digito(2), height=2, width=5)

    boton2.grid(row=2, column=1)



    boton3 = Button(ventana, text=' 3 ', fg='black', bg='white',

                     command=lambda: digito(3), height=2, width=5)

    boton3.grid(row=2, column=2)



    boton4 = Button(ventana, text=' 4 ', fg='black', bg='white',

                     command=lambda: digito(4), height=2, width=5)

    boton4.grid(row=3, column=0)



    boton5 = Button(ventana, text=' 5 ', fg='black', bg='white',

                     command=lambda: digito(5), height=2, width=5)

    boton5.grid(row=3, column=1)
    

    boton6 = Button(ventana, text=' 6 ', fg='black', bg='white',

                     command=lambda: digito(6), height=2, width=5)

    boton6.grid(row=3, column=2)


    boton7 = Button(ventana, text=' 7 ', fg='black', bg='white',

                     command=lambda: digito(7), height=2, width=5)

    boton7.grid(row=4, column=0)


    boton8 = Button(ventana, text=' 8 ', fg='black', bg='white',

                     command=lambda: digito(8), height=2, width=5)

    boton8.grid(row=4, column=1)


    boton9 = Button(ventana, text=' 9 ', fg='black', bg='white',

                     command=lambda: digito(9), height=2, width=5)

    boton9.grid(row=4, column=2)


    boton0 = Button(ventana, text=' 0 ', fg='black', bg='white',

                     command=lambda: digito(0), height=2, width=5)

    boton0.grid(row=5, column=0)

    ventana.mainloop()