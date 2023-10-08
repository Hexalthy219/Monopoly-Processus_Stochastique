import sys
import getopt
import random
import numpy as np
from numpy import genfromtxt


nombre_individus = 1

matrice1 = [[0,1/2,1/2],[1/3,1/3,1/3],[1/2,1/2,0]]
matrice2 = [[1/3,1/2,1/6],[1/3,1/3,1/3],[0,0,1]]
matrice3 = [[0,0,1,0],[0,0,1,0],[1,0,0,0],[1/2,1/2,0,0]]

nombre_dans_chaque_etat = [0,0,0,0]
proportion = [0,0,0,0]
proportion_prec = [0,0,0,0]

def creation_vecteur(distribution_initiale):
    
    vecteur = []
    for i in range(1, nombre_individus+1):
        valeur = random.uniform(0,1)
        if(valeur<=distribution_initiale[0]):
            vecteur.append(1)
        elif(valeur<=distribution_initiale[0]+distribution_initiale[1]):
            vecteur.append(2)
        elif(len(distribution_initiale)==4 and valeur<=distribution_initiale[0]+distribution_initiale[1]+distribution_initiale[2]):
                vecteur.append(3)
        elif(len(distribution_initiale)==4):
            vecteur.append(4)
        else:
            vecteur.append(3)

    return vecteur
        
def nouvelle_prochaine_etape(matrice, vecteur):
    i = 0
    global nombre_dans_chaque_etat
    nombre_dans_chaque_etat = [0,0,0,0]
    for i in range(len(vecteur)):
        valeur = random.uniform(0,1)
        if(valeur<=matrice[vecteur[i]-1][0]):
            vecteur[i]=1
            nombre_dans_chaque_etat[0]+=1
            continue
        elif(valeur<=matrice[vecteur[i]-1][0]+matrice[vecteur[i]-1][1]):
            vecteur[i]=2
            nombre_dans_chaque_etat[1]+=1
            continue
        elif(len(matrice)==3):
            vecteur[i]=3
            nombre_dans_chaque_etat[2]+=1
            continue
        elif(valeur<=matrice[vecteur[i]-1][0]+matrice[vecteur[i]-1][1]+matrice[vecteur[i]-1][2]):
            vecteur[i]=3
            nombre_dans_chaque_etat[2]+=1
            continue
        else:
            vecteur[i]=4
            nombre_dans_chaque_etat[3]+=1
            

def moyenne_individu():
    global proportion
    for i in range(4):
        proportion[i] = nombre_dans_chaque_etat[i]/nombre_individus

def check_stagnation():
    stable = True
    for i in range(len(proportion)):
        if(proportion[i]!=proportion_prec[i]):
            stable = False
        proportion_prec[i]=proportion[i]
    if(stable==True):
        return True
    return False
    
    

random.seed()

distribution = [1,0,0]
# somme = 2.
# while(somme>1):
#     somme = 0
#     distribution[3] = 1
#     for i in range(3):
#         distribution[i] = random.random()/3
#         distribution[3] -= distribution[i]
#         somme += distribution[i]
#     somme += distribution[3]
    

vecteur_test = creation_vecteur(distribution)

F = open("distribution{1,0,0}.csv", "w")

string_test = "{},{},{}\n".format(distribution[0],distribution[1], distribution[2])
F.write(string_test)

for i in range(30):
    nouvelle_prochaine_etape(matrice1 , vecteur_test)
    moyenne_individu()
    string_test = "{},{},{}\n".format(proportion[0],proportion[1], proportion[2])
    F.write(string_test)
    if(check_stagnation()):
        break

F.close()