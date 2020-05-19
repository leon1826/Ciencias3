import pickle
import random
from distutils import command
from tkinter import *
import os.path as path
from tkinter import messagebox, ttk


class Nodo():
    predecesor=list()
    antecesor=list()
    valor=None
    identificador=None
    TIC=None
    TTC=None
    def __init__(self, valor, identificador):
        # self.predecesor=predecesor
        self.valor=valor
        self.identificador=identificador
        # self.antecesor=antecesor
    def info(self):
        return self.valor, self.TIC
    def setpredecesor(self,ante:list()):
        self.antecesor=ante

    def TIC(self):
        for i in self.predecesor:
            if self.TIC == None:
                self.TIC=i
            else:
                if self.TIC>i:
                    self.TIC=i
    def TTC(self):
        self.TTC=self.TIC+self.valor
    def TTL(self):
        pass
class Rcritica():
    rutacritica=list()
    tareas=list()
    inicio=None
    def __init__(self,inicio,tareas:list()):
        self.inicio=inicio
        self.tareas=tareas
    def rutacritica(self):
        for i in self.tareas:
            pass
def prueba(numacti,root):
    matriz = []
    for i in range(numacti):
        matriz.append([])
        for j in range(2):
            matriz[i].append(None)
    opSignos = list(range(numacti))
    for i in range(numacti):
        opSignos[i] = IntVar()
    coorX1 = 30
    coorX2 = 100
    coorY = 280

    for i in range(numacti):
        for j in range(2):
            matriz[i][j] = Entry(root, width='10')
            if j == 0:
                matriz[i][j].place(x=coorX1, y=coorY)
            if j == 1:
                matriz[i][j].place(x=coorX2, y=coorY)
        coorY += 25

    print(matriz)
    procesar = Button(root, width=10, text="confirmar", command=lambda: procesar1(matriz, root,numacti))
    procesar.pack()
    procesar.place(x=130, y=200)

def procesar1(matriz,root,numacti):
    for i in range(numacti):
        for j in range(2):
                matriz[i][j]=str(matriz[i][j].get())
    temp=list()
    for k in matriz:
        nodo=Nodo(k[1],k[0])
        temp.append(nodo)

    t = Toplevel(root)
    t.geometry("500x500")


def principal():
    root = Tk()
    root.geometry("500x550")
    root.title('INVENTARIO')
    root.config(bg="#00BFFF")
    titulo = Label(root,text="Ruta critica",relief="groove", bg="red", font=("Times", 16))
    titulo.pack()
    titulo.place(x=200,y=10)
    actividades = Label(root, text="Actividades", relief="groove", bg="blue", font=("Times 12 italic bold", 12))
    actividades.pack()
    actividades.place(x=100, y=40)
    no_actividades = Label(root, text="Actividades", relief="groove", bg="blue", font=("Times 12 italic bold", 12))
    no_actividades.pack()
    no_actividades.place(x=100, y=40)
    numactividades = Entry(root)
    numactividades.place(x=315, y=125)
    # A = Label(root, text="A", relief="groove", bg="blue", font=("Times 12 italic bold", 14))
    # A.pack()
    # A.place(x=130, y=80)

    confirmar = Button(root,width=10,text="confirmar", command=lambda:prueba(int(numactividades.get()),root))
    confirmar.pack()
    confirmar.place(x=130,y=400)

    # lienzo = Canvas(root, width=450, height=220, background="#DBE3FA")
    # lienzo.pack()
    # lienzo.place(x=20, y=300)
    # # lienzo.create_rectangle(40,10,180,50, width=5)
    # lienzo.create_rectangle(180, 10,320, 50, width=5)
    # lienzo.create_text(100,35,fill="darkblue",font="Times 12 italic bold",text="Actividades")
    # lienzo.create_text(100, 35, fill="darkblue", font="Times 12 italic bold", text="Actividades")
    root.mainloop()

principal()