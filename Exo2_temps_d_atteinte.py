from dis import dis
import sys
import getopt
import random
import numpy as np
from numpy import genfromtxt


nombre_individus = 1
#Etat initiale depuis lequel calculer le temps moyen d'atteinte
#vers l'état voulu
etat = 0


def nouvelle_prochaine_etape(matrice):
    global etat
    valeur = random.uniform(0,1)
    sum_proba = 0
    for i in range(len(matrice)):
        sum_proba += matrice[etat][i]
        if(valeur<=sum_proba):
            etat = i
            break
    
    
#Main

random.seed()

matrice = np.genfromtxt('matriceQ2_1.csv', delimiter=',')

temps_moyen = 0

for t in range(100000):
    i = 0
    etat = 9
    while True:
        nouvelle_prochaine_etape(matrice)
        i+=1
        #Introduide la valeur de l'état-1 ici 
        # pour calculer le temps moyen pour l'atteindre
        if(etat == 8):
            break
    temps_moyen += i
temps_moyen = temps_moyen/100000
print(temps_moyen)
