#Programme servant a calculer la position et la vitesse en prenant en compte la gravité et l'effet Magnus

import numpy as np
# importation des bibliotheque nécéssaire

import euler as eu
import adams_moulton as am
import teste_filet as tf
import teste_zone as tz
import fonctions_magnus as f
#liens vers les autres fichiers

def calcule_position_vitesse_magnus(PXD, PYD, PZD, VXD, VYD, VZD, cote="gauche", croise="bas"):
    
    n = 1000  # nombre d'itération
    h = 0.0005  # le pas dintegration

    faute = False  # testeur de faute
    filet = False  # testeur de passage de filet
    zone = False  # testeur de zone de service

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
    PX1 = 0
    PY1 = 0
    PZ1 = 0
    VX1 = 0
    VY1 = 0
    VZ1 = 0
    
    for i in range(n-1):
        T[i+1] = T[i]+h

        if zone != True and faute != True:
            # calcule de la trajectoir avant de toucher le sol

            # approxition des positions à t+1 avec Euler
            PX1 = eu.euler_methode(f.f1, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 1)
            PY1 = eu.euler_methode(f.f2, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 2)
            PZ1 = eu.euler_methode(f.f3, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 3)
            VX1 = eu.euler_methode(f.f4, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 4)
            VY1 = eu.euler_methode(f.f5, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 5)
            VZ1 = eu.euler_methode(f.f6, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 6)

            # Calcule des position avec Adams-Moulton
            PX[i+1] = am.adams_moulton_methode(f.f1, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], PX1, 1)
            PY[i+1] = am.adams_moulton_methode(f.f2, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], PY1, 2)
            PZ[i+1] = am.adams_moulton_methode(f.f3, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], PZ1, 3)
            VX[i+1] = am.adams_moulton_methode(f.f4, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], VX1, 4)
            VY[i+1] = am.adams_moulton_methode(f.f5, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], VY1, 5)
            VZ[i+1] = am.adams_moulton_methode(f.f6, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], VZ1, 6)

            # Partie de teste de validité du service
            (filet, faute) = tf.teste_filet(PX[i], PY[i], PZ[i])
            # teste du fillet

            (zone, faute) = tz.teste_zone(PX[i], PY[i], PZ[i], cote, croise)
            # teste de la zone de service
            
            if zone:
                VY[i]=-VY[i]
                #inversion de la vitesse au moment du rebond

        if zone == True and faute != True:
        # calcule de la trajectoir après le rebond

            # approxition des positions à t+1 avec Euler
            PX1 = eu.euler_methode(f.f1, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 1)
            PY1 = eu.euler_methode(f.f2, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 2)
            PZ1 = eu.euler_methode(f.f3, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 3)
            VX1 = eu.euler_methode(f.f4, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 4)
            VY1 = eu.euler_methode(f.f5, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 5)
            VZ1 = eu.euler_methode(f.f6, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], 6)

            # Calcule des position avec Adams-Moulton
            PX[i+1] = am.adams_moulton_methode(f.f1, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], PX1, 1)
            PY[i+1] = am.adams_moulton_methode(f.f2, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], PY1, 2)
            PZ[i+1] = am.adams_moulton_methode(f.f3, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], PZ1, 3)
            VX[i+1] = am.adams_moulton_methode(f.f4, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], VX1, 4)
            VY[i+1] = am.adams_moulton_methode(f.f5, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], VY1, 5)
            VZ[i+1] = am.adams_moulton_methode(f.f6, T[i], PX[i], PY[i], PZ[i], VX[i], VY[i], VZ[i], VZ1, 6)
            
            
            
