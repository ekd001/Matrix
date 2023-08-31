"""
name : matrice
goal: crée des matrices et éffectuer quelques opérations sur eux
author:the numeric emperor
date: 31-08-2023
"""

import numpy as np
from matrice import *

natureList= ['int','float', 'complex']
rep = 'o'
rep1 = 'o'
stockMatrix = []

while(rep == 'o'):
    #Entrez la dimension de notre matrice
    a = int(input("Entrez la dimension de votre matrice(ligne) : "))
    b = int(input("Entrez la dimension de votre matrice(colonne) : "))

    print("Choisir la nature de votre matrice")
    print("1-entier naturel")
    print("2-entier décimal")
    print("3-complexe")

    choix = int(input("Entrez votre choix : "))
    if(choix == 1):
        nature = natureList[0]
    elif(choix == 2):
        nature = natureList[1]
    elif(choix == 3):
        nature = natureList[2]

    #crée notre matrice en fonction des paramètres ci-dessus
    matrix = Matrix(a,b,nature)

    #stocker notre matrix pour les opérations
    stockMatrix.append(matrix)

    rep = input("Voulez vous continuer(o/n):" )

for i in range(len(stockMatrix)):
    print(stockMatrix[i])

while(rep1 == 'o'):

    print("Choisir une opération que vous voudrez éffectuer sur vos matrice")
    print("1-somme matriciel")
    print("2-produit matriciel")
    print("3-rapport matriciel")

    choix1 = int(input("Entrez votre choix : "))
    if(choix1 == 1):
        MatrixSum(stockMatrix)
    elif(choix1 == 2):
        MatrixProduit(stockMatrix)
    elif(choix1 == 3):
        MatrixRapport(stockMatrix)
    rep1 = input("Voulez vous continuer(o/n): ")




