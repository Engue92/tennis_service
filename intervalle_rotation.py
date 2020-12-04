# programme permettant de trouver un interval de vitesse de rotation de la balle pour lequel le service est bon 
# les position et vitesse initial son fixe

import position_vitesse_magnus as pvm
import numpy as np

def intervalle_rotation (PX,PY,PZ,VX,VY,VZ,h=1,n=60,VRD0=-20) :
    
    h = h  # pas d'iteration
    n = n  # nb d'iteration
    
    VRD = np.zeros(n)   # declaration du tableau de vitesse de rotation
    VRD[0] = VRD0       # vitesse de rotation initial
    i = 0               # compteur initialise
    
    (VRinf,VRsup) = (0,0)   # rotation min et max qui valide le service 
    
    service = pvm.calcule_position_vitesse_magnus(PX,PY,PZ,VX,VY,VZ,teste=True,VRD=VRD0)     
    # variable de teste de validite du service
    
    while service == False and i < n-1 :
    # premiere partie ou on cherche a savoir la premiere valeur pour avoir un service valide
        service = pvm.calcule_position_vitesse_magnus(PX,PY,PZ,VX,VY,VZ,teste=True,VRD=VRD[i])  
        # on fait tourner le programme pour savoir si le service est bon a la vitesse VRD[i]
        VRD[i+1] = VRD[i]+h      # on fais augmenter la vitesse de rotation de la valeur du pas
        i += 1                   # incrementation du compteur
    
    if service == True :  # teste au cas ou le service est vrai des la premiere iteration
        VRinf = VRD[i]    # on donne la premiere valeur qui donne un service valide
    
    while service == True and i < n-1 :
    # deuxieme partie ou on cherche a savoir jusqu'a quand le service est valide
        service = pvm.calcule_position_vitesse_magnus(PX,PY,PZ,VX,VY,VZ,teste=True,VRD=VRD[i])
        # on fait tourner le programme pour savoir si le service est bon a la vitesse VRD[i]
        VRD[i+1] = VRD[i]+h      # on fais augmenter la vitesse de rotation de la valeur du pas
        i += 1                   # incrementation du compteur
        
    VRsup = VRD[i]  # on donne la derniere valeur qui donne un service valide
    
    # affichage du resultat
    if VRinf != 0 and VRsup != 0 :  # on affiche uniquement si on truve des valeur validant le service
        print("\nl'intervale de rotation pour que le service soit bon avec les paramètre rentré est :")
        print("\nDe ", VRinf, " à ", VRsup, " tour/min")
    else :  # on affiche si dans le cas ou on ne trouve pas de valeur validant le service
        print("le service n'est valable à aucune hauteur convenable")
    
