import time
import os
from random import randint
import tkinter as tk

#create the cube in a class

class Cube:
    def __init__(self):   
        self.B = [1 for x in range(9)]
        self.j = [2 for x in range(9)]
        self.v = [3 for x in range(9)]
        self.o = [4 for x in range(9)]
        self.b = [5 for x in range(9)]
        self.r = [6 for x in range(9)]
        self.melange = []
        self.mouvements = []
    

    def rotateBlanc(self):
        self.B[0], self.B[1], self.B[2], self.B[3], self.B[5], self.B[6], self.B[7], self.B[8] = self.B[6], self.B[3], self.B[0], self.B[7], self.B[1], self.B[8], self.B[5], self.B[2]
        
        #je veux que tu faire tourner les coté des faces v o b r collés à la face B de la même manière que la face B

        self.v[6], self.v[7], self.v[8], self.o[0], self.o[3], self.o[6], self.b[0], self.b[1], self.b[2], self.r[2], self.r[5], self.r[8] = self.r[8], self.r[5], self.r[2], self.v[6], self.v[7], self.v[8], self.o[6], self.o[3], self.o[0], self.b[0], self.b[1], self.b[2]

        self.mouvements.append(1)


    def rotateJaune(self):
        self.j[0], self.j[1], self.j[2], self.j[3], self.j[5], self.j[6], self.j[7], self.j[8] = self.j[6], self.j[3], self.j[0], self.j[7], self.j[1], self.j[8], self.j[5], self.j[2]

        self.v[0], self.v[1], self.v[2], self.o[2], self.o[5], self.o[8], self.b[6], self.b[7], self.b[8], self.r[0], self.r[3], self.r[6] = self.o[2], self.o[5], self.o[8], self.b[8], self.b[7], self.b[6], self.r[0], self.r[3], self.r[6], self.v[2], self.v[1], self.v[0]

        self.mouvements.append(2)


    def rotateVert(self):
        self.v[0], self.v[1], self.v[2], self.v[3], self.v[5], self.v[6], self.v[7], self.v[8] = self.v[6], self.v[3], self.v[0], self.v[7], self.v[1], self.v[8], self.v[5], self.v[2]

        self.B[0], self.B[1], self.B[2], self.o[0], self.o[1], self.o[2], self.j[6], self.j[7], self.j[8], self.r[0], self.r[1], self.r[2] = self.o[0], self.o[1], self.o[2], self.j[8], self.j[7], self.j[6], self.r[2], self.r[1], self.r[0], self.B[0], self.B[1], self.B[2]

        self.mouvements.append(3)

    def rotateOrange(self):
        self.o[0], self.o[1], self.o[2], self.o[3], self.o[5], self.o[6], self.o[7], self.o[8] = self.o[6], self.o[3], self.o[0], self.o[7], self.o[1], self.o[8], self.o[5], self.o[2]

        self.B[2], self.B[5], self.B[8], self.b[2], self.b[5], self.b[8], self.j[2], self.j[5], self.j[8], self.v[2], self.v[5], self.v[8] = self.b[2], self.b[5], self.b[8], self.j[2], self.j[5], self.j[8], self.v[2], self.v[5], self.v[8], self.B[2], self.B[5], self.B[8]

        self.mouvements.append(4)


    def rotateBleu(self):
        self.b[0], self.b[1], self.b[2], self.b[3], self.b[5], self.b[6], self.b[7], self.b[8] = self.b[6], self.b[3], self.b[0], self.b[7], self.b[1], self.b[8], self.b[5], self.b[2]
        
        self.B[6], self.B[7], self.B[8], self.o[6], self.o[7], self.o[8], self.j[0], self.j[1], self.j[2], self.r[6], self.r[7], self.r[8] = self.r[6], self.r[7], self.r[8], self.B[6], self.B[7], self.B[8], self.o[8], self.o[7], self.o[6], self.j[2], self.j[1], self.j[0]

        self.mouvements.append(5)


    def rotateRouge(self):
        self.r[0], self.r[1], self.r[2], self.r[3], self.r[5], self.r[6], self.r[7], self.r[8] = self.r[6], self.r[3], self.r[0], self.r[7], self.r[1], self.r[8], self.r[5], self.r[2]
        
        self.B[0], self.B[3], self.B[6], self.b[0], self.b[3], self.b[6], self.j[0], self.j[3], self.j[6], self.v[0], self.v[3], self.v[6] = self.v[0], self.v[3], self.v[6], self.B[0], self.B[3], self.B[6], self.b[0], self.b[3], self.b[6], self.j[0], self.j[3], self.j[6]

        self.mouvements.append(6)

    def melangerCube(self):
        for i in range(3):
            temp = randint(1,6)
            self.melange.append(temp)
            if temp == 1:
                self.rotateBlanc()
            elif temp == 2:
                self.rotateJaune()
            elif temp == 3:
                self.rotateVert()
            elif temp == 4:
                self.rotateOrange()
            elif temp == 5:
                self.rotateBleu()
            elif temp == 6:
                self.rotateRouge()
            print(self.melange)


    def remettreCubeZero(self):
        self.B = [1 for x in range(9)]
        self.j = [2 for x in range(9)]
        self.v = [3 for x in range(9)]
        self.o = [4 for x in range(9)]
        self.b = [5 for x in range(9)]
        self.r = [6 for x in range(9)]
        self.melange = []
        self.mouvements = []

    def afficherCube(self):
        print("         ",self.v[0:3])
        print("         ",self.v[3:6])
        print("         ",self.v[6:9])
        print(self.r[0:3],self.B[0:3],self.o[0:3])
        print(self.r[3:6],self.B[3:6],self.o[3:6])
        print(self.r[6:9],self.B[6:9],self.o[6:9])
        print("         ",self.b[0:3])
        print("         ",self.b[3:6])
        print("         ",self.b[6:9])
        print("         ",self.j[0:3])
        print("         ",self.j[3:6])
        print("         ",self.j[6:9])



# create clear console function

clear = lambda: os.system('cls')



"""
        o o o
        o o o
        o o o
j j j   v v v   B B B
j j j   v v v   B B B
j j j   v v v   B B B
        r r r
        r r r
        r r r
        b b b
        b b b
        b b b



corélation de chaque face avec les couleurs par rapport aux matrices initiées au début du code:


         j j j
        rv v vo
        rv v vo
        rv v vo
         B B B

         v v v
        rB B Bo
        rB B Bo
        rB B Bo
         b b b


         v v v
        Bo o oj
        Bo o oj
        Bo o oj
         b b b


         B B B
        rb b bo
        rb b bo
        rb b bo
         j j j


         v v v
        jr r rB
        jr r rB
        jr r rB
         b b b


         b b b
        rj j jo
        rj j jo
        rj j jo
         v v v

"""



# Créer l'application tkinter

class Application(tk.Tk):

    def __init__(self):
        self.cube = Cube()
        tk.Tk.__init__(self)
        self.size = 500
        self.creer_widgets()
        self.cube.mouvements.clear()
        self.cube.melange.clear()

    def creer_widgets(self):
        # création canevas
        self.canv = tk.Canvas(self, bg="light gray", height=self.size+self.size/3, width=self.size)
        self.canv.pack(side=tk.LEFT)
        # boutons
        self.faceBlanche = tk.Button(self, text="Blanc", command=self.cube.rotateBlanc)
        self.faceBlanche.pack(side=tk.TOP)

        self.faceJaune = tk.Button(self, text="Jaune", command=self.cube.rotateJaune)
        self.faceJaune.pack(side=tk.TOP)

        self.faceVerte = tk.Button(self, text="Vert", command=self.cube.rotateVert)
        self.faceVerte.pack(side=tk.TOP)

        self.faceOrange = tk.Button(self, text="Orange", command=self.cube.rotateOrange)
        self.faceOrange.pack(side=tk.TOP)

        self.faceBleue = tk.Button(self, text="Bleu", command=self.cube.rotateBleu)
        self.faceBleue.pack(side=tk.TOP)

        self.faceRouge = tk.Button(self, text="Rouge", command=self.cube.rotateRouge)
        self.faceRouge.pack(side=tk.TOP)

        
        self.bouton_quitter = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side=tk.BOTTOM)

        self.bouton_melanger = tk.Button(self, text="Melanger", command=self.cube.melangerCube)
        self.bouton_melanger.pack(side=tk.BOTTOM)

        self.bouton_actualiser = tk.Button(self, text="Actualiser", command=self.afficherCube)
        self.bouton_actualiser.pack(side=tk.BOTTOM)

        self.bouton_remettre = tk.Button(self, text="Remettre à zéro", command=self.cube.remettreCubeZero)
        self.bouton_remettre.pack(side=tk.BOTTOM)
    
    def quit(self):
        self.destroy()

    def numtocolor(self, num):
        if num == 1:
            return "white"
        elif num == 2:
            return "yellow"
        elif num == 3:
            return "green"
        elif num == 4:
            return "orange"
        elif num == 5:
            return "blue"
        elif num == 6:
            return "red"

    
    def afficherCube(self):
        # afficher tout le cube en allant chercher les couleurs dans la matrice, la face blache est au milieu, la verte et au dessus de la blanche, la orange est à droite, la bleue en bas, la rouge à gauche et la jaune en dessous de la bleue

        #face verte

        self.canv.create_rectangle(self.size/3, 0, self.size/3+self.size/9, self.size/9, fill=self.numtocolor(self.cube.v[0]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, 0, self.size/3+2*self.size/9, self.size/9, fill=self.numtocolor(self.cube.v[1]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, 0, self.size/3+3*self.size/9, self.size/9, fill=self.numtocolor(self.cube.v[2]), outline="light gray")
        self.canv.create_rectangle(self.size/3, self.size/9, self.size/3+self.size/9, 2*self.size/9, fill=self.numtocolor(self.cube.v[3]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size/9, self.size/3+2*self.size/9, 2*self.size/9, fill=self.numtocolor(self.cube.v[4]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size/9, self.size/3+3*self.size/9, 2*self.size/9, fill=self.numtocolor(self.cube.v[5]), outline="light gray")
        self.canv.create_rectangle(self.size/3, 2*self.size/9, self.size/3+self.size/9, 3*self.size/9, fill=self.numtocolor(self.cube.v[6]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, 2*self.size/9, self.size/3+2*self.size/9, 3*self.size/9, fill=self.numtocolor(self.cube.v[7]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, 2*self.size/9, self.size/3+3*self.size/9, 3*self.size/9, fill=self.numtocolor(self.cube.v[8]), outline="light gray")


        # face rouge
        self.canv.create_rectangle(0, self.size/3, self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.r[0]), outline="light gray")
        self.canv.create_rectangle(self.size/9, self.size/3, 2*self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.r[1]), outline="light gray")
        self.canv.create_rectangle(2*self.size/9, self.size/3, 3*self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.r[2]), outline="light gray")
        self.canv.create_rectangle(0, self.size/3+self.size/9, self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.r[3]), outline="light gray")
        self.canv.create_rectangle(self.size/9, self.size/3+self.size/9, 2*self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.r[4]), outline="light gray")
        self.canv.create_rectangle(2*self.size/9, self.size/3+self.size/9, 3*self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.r[5]), outline="light gray")
        self.canv.create_rectangle(0, self.size/3+2*self.size/9, self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.r[6]), outline="light gray")
        self.canv.create_rectangle(self.size/9, self.size/3+2*self.size/9, 2*self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.r[7]), outline="light gray")
        self.canv.create_rectangle(2*self.size/9, self.size/3+2*self.size/9, 3*self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.r[8]), outline="light gray")

        # face blanche
        self.canv.create_rectangle(self.size/3, self.size/3, self.size/3+self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.B[0]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size/3, self.size/3+2*self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.B[1]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size/3, self.size/3+3*self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.B[2]), outline="light gray")
        self.canv.create_rectangle(self.size/3, self.size/3+self.size/9, self.size/3+self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.B[3]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size/3+self.size/9, self.size/3+2*self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.B[4]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size/3+self.size/9, self.size/3+3*self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.B[5]), outline="light gray")
        self.canv.create_rectangle(self.size/3, self.size/3+2*self.size/9, self.size/3+self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.B[6]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size/3+2*self.size/9, self.size/3+2*self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.B[7]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size/3+2*self.size/9, self.size/3+3*self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.B[8]), outline="light gray")

        # face orange
        self.canv.create_rectangle(2*self.size/3, self.size/3, 2*self.size/3+self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.o[0]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3+self.size/9, self.size/3, 2*self.size/3+2*self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.o[1]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3+2*self.size/9, self.size/3, 2*self.size/3+3*self.size/9, self.size/3+self.size/9, fill=self.numtocolor(self.cube.o[2]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3, self.size/3+self.size/9, 2*self.size/3+self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.o[3]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3+self.size/9, self.size/3+self.size/9, 2*self.size/3+2*self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.o[4]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3+2*self.size/9, self.size/3+self.size/9, 2*self.size/3+3*self.size/9, self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.o[5]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3, self.size/3+2*self.size/9, 2*self.size/3+self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.o[6]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3+self.size/9, self.size/3+2*self.size/9, 2*self.size/3+2*self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.o[7]), outline="light gray")
        self.canv.create_rectangle(2*self.size/3+2*self.size/9, self.size/3+2*self.size/9, 2*self.size/3+3*self.size/9, self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.o[8]), outline="light gray")

        # face bleue
        self.canv.create_rectangle(self.size/3, 2*self.size/3, self.size/3+self.size/9, 2*self.size/3+self.size/9, fill=self.numtocolor(self.cube.b[0]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, 2*self.size/3, self.size/3+2*self.size/9, 2*self.size/3+self.size/9, fill=self.numtocolor(self.cube.b[1]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, 2*self.size/3, self.size/3+3*self.size/9, 2*self.size/3+self.size/9, fill=self.numtocolor(self.cube.b[2]), outline="light gray")
        self.canv.create_rectangle(self.size/3, 2*self.size/3+self.size/9, self.size/3+self.size/9, 2*self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.b[3]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, 2*self.size/3+self.size/9, self.size/3+2*self.size/9, 2*self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.b[4]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, 2*self.size/3+self.size/9, self.size/3+3*self.size/9, 2*self.size/3+2*self.size/9, fill=self.numtocolor(self.cube.b[5]), outline="light gray")
        self.canv.create_rectangle(self.size/3, 2*self.size/3+2*self.size/9, self.size/3+self.size/9, 2*self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.b[6]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, 2*self.size/3+2*self.size/9, self.size/3+2*self.size/9, 2*self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.b[7]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, 2*self.size/3+2*self.size/9, self.size/3+3*self.size/9, 2*self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.b[8]), outline="light gray")

        # face jaune
        self.canv.create_rectangle(self.size/3, self.size+2*self.size/9, self.size/3+self.size/9, 2*self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.j[0]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size+2*self.size/9, self.size/3+2*self.size/9, 2*self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.j[1]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size+2*self.size/9, self.size/3+3*self.size/9, 2*self.size/3+3*self.size/9, fill=self.numtocolor(self.cube.j[2]), outline="light gray")
        self.canv.create_rectangle(self.size/3, self.size+3*self.size/9, self.size/3+self.size/9, 2*self.size/3+4*self.size/9, fill=self.numtocolor(self.cube.j[3]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size+3*self.size/9, self.size/3+2*self.size/9, 2*self.size/3+4*self.size/9, fill=self.numtocolor(self.cube.j[4]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size+3*self.size/9, self.size/3+3*self.size/9, 2*self.size/3+4*self.size/9, fill=self.numtocolor(self.cube.j[5]), outline="light gray")
        self.canv.create_rectangle(self.size/3, self.size+4*self.size/9, self.size/3+self.size/9, 2*self.size/3+5*self.size/9, fill=self.numtocolor(self.cube.j[6]), outline="light gray")
        self.canv.create_rectangle(self.size/3+self.size/9, self.size+4*self.size/9, self.size/3+2*self.size/9, 2*self.size/3+5*self.size/9, fill=self.numtocolor(self.cube.j[7]), outline="light gray")
        self.canv.create_rectangle(self.size/3+2*self.size/9, self.size+4*self.size/9, self.size/3+3*self.size/9, 2*self.size/3+5*self.size/9, fill=self.numtocolor(self.cube.j[8]), outline="light gray")









# Lancer le jeu

if __name__ == "__main__":
    app = Application()
    while True:
        app.update()
        app.afficherCube()
        time.sleep(0.1)