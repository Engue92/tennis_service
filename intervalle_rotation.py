# programme permettant de trouver un interval de vitesse de rotation de la balle pour lequel le service est bon 
# les position et vitesse initial son fixe

import position_vitesse_gravite as pvg
import numpy as np

def intervalle_rotation (PX,PZ,VX,VY,VZ,cote,croise,force) :
    
    h = 0.0005  # pas d'iteration
    n = 1200    # nb d'iteration
    
    PY = np.zeros(n)
    PY[0] = 1
    i = 0
    
    PYinf = 0
    PYsup = 0
    
    service = False
    
    while service == False :
        service = pvg.calcule_position_vitesse_gravite(PX,PY[i],PZ,VX,VY,VZ,cote,croise)
        PY[i+1] = PY[i]+h
        i += 1
    
    PY[i] = PYinf
    
    while service == True:
        service = pvg.calcule_position_vitesse_gravite(PX,PY[i],PZ,VX,VY,VZ,cote,croise)
        PY[i+1] = PY[i]+h
        i += 1
        
    PY[i] = PYsup
    
    print("l'intervale de hauteur pour que le service soit bon avec les paramètre rentré est :")
    print("De ", PYinf, " à ", PYsup)
