#Programme servant a calculer la position et la vitesse en prenant en compte la gravite et l'effet Magnus

import numpy as np
# importation des bibliotheque nécéssaire

import euler as eu
import adams_moulton as am
import teste_filet as tf
import teste_zone as tz
import trajectoir as tr
#liens vers les autres fichiers

def calcule_position_vitesse_magnus(PXD, PYD, PZD, VXD, VYD, VZD, cote="gauche", croise="bas"):
    
    n = 1200    # nombre d'iteration
    h = 0.0005  # le pas dintegration

    faute = False  # testeur de faute
    filet = False  # testeur de passage de filet
    zone = False   # testeur de zone de service

    # on declare les tableaux
    PX = np.zeros(n)
    PY = np.zeros(n)
    PZ = np.zeros(n)
    VX = np.zeros(n)
    VY = np.zeros(n)
    VZ = np.zeros(n)
    T = np.zeros(n)
    
    # les positions initiales
    PX[0] = PXD
    PY[0] = PYD
    PZ[0] = PZD

    # les vitesses initiales
    VX[0] = VXD
    VY[0] = VYD
    VZ[0] = VZD

    # les approximation initiales
    PX1 = 1
    PY1 = 1
    PZ1 = 1
    VX1 = 1
    VY1 = 1
    VZ1 = 1
    
    for i in range(n-1):
        
        T[i+1] = T[i]+h  # incrementation du temps

        if zone != True and faute != True :  # calcule de la trajectoir avant de toucher le sol
            
            # approxition des positions a t+1 avec Euler
            (PX1,PY1,PZ1,VX1,VY1,VZ1) = eu.euler_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],fct="m")

            # Calcule des position avec Adams-Moulton
            (PX[i+1],PY[i+1],PZ[i+1],VX[i+1],VY[i+1],VZ[i+1]) = am.adams_moulton_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],PX1,PY1,PZ1,VX1,VY1,VZ1,fct="m")

            # Partie de teste de validite du service
            (filet, faute, let) = tf.teste_filet(PX[i], PY[i], PZ[i])                 # teste de la hauteur au filet
            (zone, faute) = tz.teste_zone(PX[i], PY[i], PZ[i], let, cote, croise)     # teste de la zone de service
               
            if zone:            # si la balle atterit dans la bonne zone du terrain
                VY[i]=-VY[i]    # inversion de la vitesse au moment du rebond    

        if zone == True and faute != True :  # calcule de la trajectoir apres le rebond
        
            # approxition des positions a t+1 avec Euler
            (PX1,PY1,PZ1,VX1,VY1,VZ1) = eu.euler_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],fct="m")

            # Calcule des position avec Adams-Moulton
            (PX[i+1],PY[i+1],PZ[i+1],VX[i+1],VY[i+1],VZ[i+1]) = am.adams_moulton_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],PX1,PY1,PZ1,VX1,VY1,VZ1,fct="m")
            
    tr.trajectoir(PX,PY,PZ) # affichage de la trajectoire

    return (zone)  
            
