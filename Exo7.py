import sys
import getopt
import random
import numpy as np
from numpy import genfromtxt


nombre_individus = 1

matrice1 = [[0,1/2,1/2],[1/3,1/3,1/3],[1/2,1/2,0]]
matrice2 = [[1/3,1/2,1/6],[1/3,1/3,1/3],[0,0,1]]
matrice3 = [[0,0,1,0],[0,0,1,0],[1,0,0,0],[1/2,1/2,0,0]]

nombre_dans_chaque_etat = [0,0,0]
proportion = [0,0,0]
proportion_prec = [0,0,0]

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
    global nombre_dans_chaque_etat
    i = 0    
    nombre_dans_chaque_etat = [0,0,0]
    for i in range(len(vecteur)):
        valeur = random.uniform(0,1)
        if(valeur<=matrice[vecteur[i]-1][0]):
            vecteur[i]=1
            nombre_dans_chaque_etat[0]+=1
            nombre_passage[0]+=1
            continue
        elif(valeur<=matrice[vecteur[i]-1][0]+matrice[vecteur[i]-1][1]):
            vecteur[i]=2
            nombre_dans_chaque_etat[1]+=1
            nombre_passage[1]+=1
            continue
        elif(len(matrice)==3):
            vecteur[i]=3
            nombre_dans_chaque_etat[2]+=1
            nombre_passage[2]+=1
            continue
        elif(valeur<=matrice[vecteur[i]-1][0]+matrice[vecteur[i]-1][1]+matrice[vecteur[i]-1][2]):
            vecteur[i]=3
            nombre_dans_chaque_etat[2]+=1
            nombre_passage[2]+=1
            continue
        else:
            vecteur[i]=4
            nombre_dans_chaque_etat[3]+=1
            nombre_passage[3]+=1
            

def moyenne_individu():
    global proportion
    for i in range(3):
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
    
    
#Main

random.seed()

distribution = [1,0,0]
nombre_passage = [0,0,0]
temps_moyen = 0

for t in range(5000000):
    vecteur_test = creation_vecteur(distribution)
    nombre_passage = [0,0,0]
    i = 0
    while True:
        nouvelle_prochaine_etape(matrice2 , vecteur_test)
        moyenne_individu()
        i+=1
        if(nombre_passage[2] == 1):
            break
    temps_moyen += i
temps_moyen = temps_moyen/5000000
print(temps_moyen)
