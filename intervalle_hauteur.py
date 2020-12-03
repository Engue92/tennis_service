# programme permettant de trouver un interval de hauteur pour lequel le service est bon 
# les position et vitesse initial son fixe

import position_vitesse_gravite as pvg
import numpy as np

def intervalle_hauteur (PX,PZ,VX,VY,VZ,h=0.005,n=400,PY0=2) :
    
    h = h  # pas d'iteration
    n = n  # nb d'iteration
    
    PY = np.zeros(n)   # declaration du tableau de vitesse de rotation
    PY[0] = PY0        # vitesse de rotation initial
    i = 0              # compteur initialise
    
    (PYinf,PYsup) = (0,0)   # rotation min et max qui valide le service 
    
    service = False     # variable pour savoir si le service est bon ou non
    
    while service == False :
    # premiere partie ou on cherche a savoir la premiere valeur pour avoir un service valide
        service = pvg.calcule_position_vitesse_gravite(PX,PY[i],PZ,VX,VY,VZ,teste=True)
        # on fait tourner le programme pour savoir si le service est bon a la vitesse hauteur PY[i]
        PY[i+1] = PY[i]+h  # on fais augmenter la hauteur de la valeur du pas
        i += 1             # incrementation du compteur
    
    PYinf = PY[i]  # on donne la premiere valeur qui donne un service valide
    
    while service == True:
    # deuxieme partie ou on cherche a savoir jusqu'a quand le service est valide
        service = pvg.calcule_position_vitesse_gravite(PX,PY[i],PZ,VX,VY,VZ,teste=True)
        # on fait tourner le programme pour savoir si le service est bon a la vitesse hauteur PY[i]
        PY[i+1] = PY[i]+h  # on fais augmenter la hauteur de la valeur du pas
        i += 1             # incrementation du compteur
        
    PYsup = PY[i]  # on donne la derniere valeur qui donne un service valide

    if PYinf != 0 and PYsup != 0 :  # on affiche uniquement si on truve des valeur validant le service
        print("\nl'intervale de hauteur pour que le service soit bon avec les paramètre rentré est :")
        print("\nDe ", PYinf, "m à ", PYsup, "m")
    else :  # on affiche si dans le cas ou on ne trouve pas de valeur validant le service
        print("le service n'est valable à aucune hauteur convenable")
