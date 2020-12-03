# programme permettant d'utiliser la fonction d'Euler

import fonctions_gravite as fg
import fonctions_magnus as fm

def euler_methode(T,PX,PY,PZ,VX,VY,VZ,h,fct,VR=0.4):
# initialisation de la fonction
      
    if fct == "g" :  # dans le cas ou on prend en compte la gravite
        PX1 = PX + h*fg.f1(T,PX,PY,PZ,VX,VY,VZ)        # pour la position en X            
        PY1 = PY + h*fg.f2(T,PX,PY,PZ,VX,VY,VZ)        # pour la position en Y    
        PZ1 = PZ + h*fg.f3(T,PX,PY,PZ,VX,VY,VZ)        # pour la position en Z        
        VX1 = VX + h*fg.f4(T,PX,PY,PZ,VX,VY,VZ)        # pour la vitesse en X      
        VY1 = VY + h*fg.f5(T,PX,PY,PZ,VX,VY,VZ)        # pour la vitesse en Y   
        VZ1 = VZ + h*fg.f6(T,PX,PY,PZ,VX,VY,VZ)        # pour la vitesse en Z
        
    elif fct == "m" :  # dans le cas ou on prend en compte toutes les forces
        PX1 = PX + h*fm.f1(T,PX,PY,PZ,VX,VY,VZ)        # pour la position en X            
        PY1 = PY + h*fm.f2(T,PX,PY,PZ,VX,VY,VZ)        # pour la position en Y        
        PZ1 = PZ + h*fm.f3(T,PX,PY,PZ,VX,VY,VZ)        # pour la position en Z        
        VX1 = VX + h*fm.f4(T,PX,PY,PZ,VX,VY,VZ,VR)     # pour la vitesse en X  
        VY1 = VY + h*fm.f5(T,PX,PY,PZ,VX,VY,VZ,VR)     # pour la vitesse en Y
        VZ1 = VZ + h*fm.f6(T,PX,PY,PZ,VX,VY,VZ,VR)     # pour la vitesse en Z
    
    
    return (PX1,PY1,PZ1,VX1,VY1,VZ1)
    # renvoie position à t+1 approximé avec euler 


