import  numpy as np


#crée une fonction qui crée une matrice
def Matrix(a,b,nature):
    list = []

    for i in range(a*b):
        elts = int(input(f"nombre n°{i} de la matrice : "))
        list.append(elts)
    array0 = np.array(list,dtype=nature)
    array1 = array0.reshape(a,b)
    return array1

def MatrixSum(Matrix):
    sum = 0
    try:
        for i in range(len(Matrix)):
            sum += Matrix[i]
        print(f"la somme des matrices est : {sum}")
    except:
        print("Vos matrices doivent avoir la même taille")

def MatrixProduit(Matrix):
    try:
        pro = Matrix[0]
        for i in range(1,len(Matrix)):
            pro = pro.dot(Matrix[i])
        print(f"le produit des matrices est : {pro}")
    except:
        print("la taille de vos matrices doivent être sous la forme (x,b)&(b,y)&(y,z)....")

def MatrixRapport(Matrix):
    try:
        if((len(Matrix) == 2)):
            rap = Matrix[0]/Matrix[1]
            print(f"le rapport des matrices est : {rap}")
    except:
        print("ERROR nous devons avoir obligatoirement 2 matrices de même taille")
