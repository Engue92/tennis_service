# programme permettant d'utiliser la fonction d'Adam-Moulton

import fonctions_gravite as fg
import fonctions_magnus as fm

def adams_moulton_methode(T,PX,PY,PZ,VX,VY,VZ,PAX,PAY,PAZ,VAX,VAY,VAZ,h,fct,VR=0.4):
# initialisation de la fonction d'Adams-Moulton
    
    if fct == "g" :  # dans le cas ou on prend en compte la gravite
        PX1 = PX + (h/2)*(fg.f1(T,PX,PY,PZ,VX,VY,VZ) + PAX )        # pour la position en X
        PY1 = PY + (h/2)*(fg.f2(T,PX,PY,PZ,VX,VY,VZ) + PAY )        # pour la position en Y
        PZ1 = PZ + (h/2)*(fg.f3(T,PX,PY,PZ,VX,VY,VZ) + PAZ )        # pour la position en Z
        VX1 = VX + (h/2)*(fg.f4(T,PX,PY,PZ,VX,VY,VZ) + VAX )        # pour la vitesse en X        
        VY1 = VY + (h/2)*(fg.f5(T,PX,PY,PZ,VX,VY,VZ) + VAY )        # pour la vitesse en Y
        VZ1 = VZ + (h/2)*(fg.f6(T,PX,PY,PZ,VX,VY,VZ) + VAZ )        # pour la vitesse en Z
        
    elif fct == "m" :  # dans le cas ou on prend en compte toutes les forces
        PX1 = PX + (h/2)*(fm.f1(T,PX,PY,PZ,VX,VY,VZ) + PAX )        # pour la position en X
        PY1 = PY + (h/2)*(fm.f2(T,PX,PY,PZ,VX,VY,VZ) + PAY )        # pour la position en Y
        PZ1 = PZ + (h/2)*(fm.f3(T,PX,PY,PZ,VX,VY,VZ) + PAZ )        # pour la position en Z
        VX1 = VX + (h/2)*(fm.f4(T,PX,PY,PZ,VX,VY,VZ,VR) + VAX )     # pour la vitesse en X 
        VY1 = VY + (h/2)*(fm.f5(T,PX,PY,PZ,VX,VY,VZ,VR) + VAY )     # pour la vitesse en Y
        VZ1 = VZ + (h/2)*(fm.f6(T,PX,PY,PZ,VX,VY,VZ,VR) + VAZ )     # pour la vitesse en Z 
        
    return (PX1,PY1,PZ1,VX1,VY1,VZ1)
    # retourne la position suivante exacte