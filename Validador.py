import abc
from tkinter import *
from tkinter import messagebox
import re

class Validar(metaclass=abc.ABCMeta): #comando
    @abc.abstractmethod
    def execute(self):
        pass


class Validador(Validar):   #comando concreto
    def __init__(self,orden,expresion,frase):
        self.val = orden
        self.expresion = expresion
        self.frase = frase

    def execute(self):
        self.val.validarexpresion(self.expresion,self.frase)


class FuncionValidar:   #Receiver
    def validarexpresion(self,expresion,frase):
        patron = re.compile(expresion)
        print(patron.search(frase).group(0))
        if(expresion=="" or frase==""):
            if expresion=="":
                messagebox.showwarning("Advertencia", "Ingrese una Expresion Regular")
            else:
                messagebox.showwarning("Advertencia", "Ingrese una frase para validar")
        else:
            if patron.match(frase):
                messagebox.showinfo("Felicidades", "Frase Valida")
            else:
                messagebox.showerror("Error", "Frase No Valida")

class Broker: #invoker
    def __init__(self):
        self.__coladecomandos = []

    def respuesta(self,orden):
        self.__coladecomandos.append(orden)
        orden.execute()

