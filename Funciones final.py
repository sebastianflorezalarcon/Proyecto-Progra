# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:28:11 2020

@author: anapl
"""

from tkinter import *

import math



boton = ""



def digito(num):
    
    global boton
    
    boton = boton + str(num)
    
    calculo.set(boton)
    
    
def igual():
    
    try:
        global boton
        total=str(eval(boton))
        calculo.set(total)
        boton=""
        
    except:
        calculo.set(" error ")
        
        
def limpiar():
    
    calculo.set("")
    
    
def cuadrado():
    
    try:
        global boton
        
        total=str((eval(boton))**2)
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error")
        
def notacionc():

        global boton

        s='{:.2e}'.format(int(boton)).replace(".00e+", "*10^")

        calculo.set(str(s))

        boton = ""
        
def logaritmo():
    
    try:
        global boton
        
        total= str(math.log10(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error")
        
def logaritmo_natural():
    
    try:
        global boton
        
        total= str(math.log(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error")

def raiz():
    
    try:
        global boton
        
        total=str(math.sqrt(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error")
        
def seno():
    
    try:
        global boton
        
        total=str(math.sin(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
          
    except:
        calculo.set("error")
        
def seno():
    
    try:
        global boton
        
        total=str(math.sin(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error") 
        

def coseno():
    
    try:
        global boton
        
        total=str(math.cos(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error")
        
def tangente():
    
    try:
        global boton
        
        total=str(math.tan(eval(boton)))
        
        calculo.set(total)
        
        boton= ""
        
    except:
        calculo.set("error")
        
def teclado(event):
    
    digito(event.char)
    
    
        
if __name__ == "__main__":

    ventana = Tk()


    ventana.configure(background="light green")

    ventana.title("Calculadora Proyecto")

    ventana.geometry("300x300")




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


    suma = Button(ventana, text=' + ', fg='black', bg='white',

                  command=lambda: digito("+"), height=2, width=5)

    suma.grid(row=2, column=3)
    
    
    resta = Button(ventana, text=' - ', fg='black', bg='white',

                   command=lambda: digito("-"), height=2, width=5)

    resta.grid(row=2, column=5)
    
    
    multiplica = Button(ventana, text=' * ', fg='black', bg='white',

                      command=lambda: digito("*"), height=2, width=5)

    multiplica.grid(row=3, column=3)
    
    
    divide = Button(ventana, text=' / ', fg='black', bg='white',

                    command=lambda: digito("/"), height=2, width=5)

    divide.grid(row=3, column=5)
    
    
    resultado = Button(ventana, text=' = ', fg='black', bg='white',

                   command=igual, height=2, width=5)

    resultado.grid(row=5, column=5)
    
    
    limpiar = Button(ventana, text='Limpiar', fg='black', bg='white',

                   command=limpiar, height=2, width=5)

    limpiar.grid(row=4, column=5)
    
    
    punto = Button(ventana, text='.', fg='black', bg='white',

                   command=lambda: digito("."), height=2, width=5)

    punto.grid(row=4, column=3)
    
    
    expo = Button(ventana, text=' ^2 ', fg='black', bg='white',

                   command=cuadrado, height=2, width=5)

    expo.grid(row=5, column=3)
    
    parentesis1 = Button(ventana, text='(', fg='black', bg='white',

                   command=lambda: digito("("), height=2, width=5)

    parentesis1 .grid(row=5, column=1)

    parentesis2 = Button(ventana, text=')', fg='black', bg='white',

                   command=lambda: digito(")"), height=2, width=5)

    parentesis2 .grid(row=5, column=2)
    
    e = Button(ventana, text=' e ', fg='black', bg='white',

                   command= lambda:digito(math.e), height=2, width=5)

    e.grid(row=6, column=0)
    
    pi = Button(ventana, text=' π ', fg='black', bg='white',

                   command= lambda:digito(math.pi), height=2, width=5)

    pi.grid(row=6, column=1)
    
    notacion = Button(ventana, text=' E ', fg='black', bg='white',

                   command=notacionc, height=2, width=5)

    notacion.grid(row=6, column=2)
    
    log = Button(ventana, text=' log ', fg='black', bg='white',

                   command=logaritmo, height=2, width=5)

    log.grid(row=6, column=3)
    
    ln = Button(ventana, text=' ln ', fg='black', bg='white',

                   command=logaritmo_natural, height=2, width=5)

    ln.grid(row=6, column=5)
    
    raiz2 = Button(ventana, text=' √ ', fg='black', bg='white',

                   command=raiz, height=2, width=5)

    raiz2.grid(row=7, column=0)
    
    sen = Button(ventana, text=' sin ', fg='black', bg='white',

                   command=seno, height=2, width=5)

    sen.grid(row=7, column=1)
    
    cos = Button(ventana, text=' cos ', fg='black', bg='white',

                   command=coseno, height=2, width=5)

    cos.grid(row=7, column=2)
    
    tan = Button(ventana, text=' tan ', fg='black', bg='white',

                   command=tangente, height=2, width=5)

    tan.grid(row=7, column=3)
        
    ventana.bind("<Return>",(lambda event: igual()))
    
    ventana.bind("<Key>", teclado)
    
    ventana.mainloop()