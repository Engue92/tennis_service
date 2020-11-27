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

    # variable de teste
    (filet,sol,let,service) = (False,False,False,False)  # testeur de faute

    # on declare les tableaux
    (PX,PY,PZ,VX,VY,VZ,T) = (np.zeros(n),np.zeros(n),np.zeros(n),np.zeros(n),np.zeros(n),np.zeros(n),np.zeros(n))

    # les positions initiales
    (PX[0],PY[0],PZ[0]) = (PXD,PYD,PZD)

    # les vitesses initiales
    (VX[0],VY[0],VZ[0]) = (VXD,VYD,VZD)

    # les approximation initiales
    (PX1,PY1,PZ1,VX1,VY1,VZ1) = (1,1,1,1,1,1)
    
    # variable de teste des approximation
    (TAPX,TAPY,TAPZ,TAVX,TAVY,TAVZ) = (1,1,1,1,1,1)
    
    for i in range(n-1):
        
        T[i+1] = T[i]+h  # incrementation du temps

        if sol != True :  # calcule de la trajectoir avant de toucher le sol
        
            # Calcule des approximation avec Euler
            (PX1,PY1,PZ1,VX1,VY1,VZ1) = eu.euler_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],fct="m")
            
            # tant que l'approximation n'est pas assez precise
            while abs(PX[i+1] - TAPX) > 0.000001 and abs(PY[i+1] - TAPY) > 0.000001 and abs(PZ[i+1] - TAPZ) > 0.000001 and abs(VX[i+1] - TAVX) > 0.000001 and abs(VY[i+1] - TAVY) > 0.000001 and abs(VZ[i+1] - TAVZ) > 0.000001 :
               
                # on donne la valeur approxime a la variable de teste de l'approximation
                (TAPX,TAPY,TAPZ,TAVX,TAVY,TAVZ) = (PX1,PY1,PZ1,VX1,VY1,VZ1)
               
                # Calcule des position avec Adams-Moulton
                (PX[i+1],PY[i+1],PZ[i+1],VX[i+1],VY[i+1],VZ[i+1]) = am.adams_moulton_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],PX1,PY1,PZ1,VX1,VY1,VZ1,fct="m")
              
                # on donne la valeur a i+1 a l'approximation 
                (PX1,PY1,PZ1,VX1,VY1,VZ1) = (PX[i+1],PY[i+1],PZ[i+1],VX[i+1],VY[i+1],VZ[i+1])
                
            # Teste de validite du service
            if filet != True or let != True :
                (filet, let) = tf.teste_filet(PX[i], PY[i], PZ[i])                          # teste de la hauteur au filet
            (sol,service) = tz.teste_zone(PX[i], PY[i], PZ[i], let, filet, cote, croise)    # teste de la zone de service
          
        if sol == True :  # calcule de la trajectoir apres le rebond
           
            # approxition des positions a i+1 avec Euler
            (PX1,PY1,PZ1,VX1,VY1,VZ1) = eu.euler_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],fct="m")
            VY[i]=abs(VY[i])  # on donne a la vitesse en Y sa valeur absolue
            
            # tant que l'approximation n'est pas assez precise
            while abs(PX[i+1] - TAPX) > 0.000001 and abs(PY[i+1] - TAPY) > 0.000001 and abs(PZ[i+1] - TAPZ) > 0.000001 and abs(VX[i+1] - TAVX) > 0.000001 and abs(VY[i+1] - TAVY) > 0.000001 and abs(VZ[i+1] - TAVZ) > 0.000001 :
             
                # on donne la valeur approxime a la variable de teste de l'approximation
                (TAPX,TAPY,TAPZ,TAVX,TAVY,TAVZ) = (PX1,PY1,PZ1,VX1,VY1,VZ1)
             
                # Calcule des position avec Adams-Moulton
                (PX[i+1],PY[i+1],PZ[i+1],VX[i+1],VY[i+1],VZ[i+1]) = am.adams_moulton_methode(T[i],PX[i],PY[i],PZ[i],VX[i],VY[i],VZ[i],PX1,PY1,PZ1,VX1,VY1,VZ1,fct="m")
              
                # on donne la valeur a i+1 a l'approximation
                (PX1,PY1,PZ1,VX1,VY1,VZ1) = (PX[i+1],PY[i+1],PZ[i+1],VX[i+1],VY[i+1],VZ[i+1])  

    tr.trajectoir(PX,PY,PZ)  # affichage de la trajectoire
            
    return(service)






