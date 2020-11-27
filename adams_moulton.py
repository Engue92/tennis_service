#Programme permettant d'utiliser la fonction d'Adam-Moulton

import fonctions_gravite as fg
import fonctions_magnus as fm

def adams_moulton_methode(T,PX,PY,PZ,VX,VY,VZ,PAX,PAY,PAZ,VAX,VAY,VAZ,fct):
#initialisation de la fonction d'Adams-Moulton
#PN : paramètre n°N peut-être PX ou PY ou VX...

    h = 0.0005
    
    if fct == "g" :
        PX1 = PX + (h/2)*(fg.f1(T,PX,PY,PZ,VX,VY,VZ) + PAX )
        PY1 = PY + (h/2)*(fg.f2(T,PX,PY,PZ,VX,VY,VZ) + PAY )
        PZ1 = PZ + (h/2)*(fg.f3(T,PX,PY,PZ,VX,VY,VZ) + PAZ )
        VX1 = VX + (h/2)*(fg.f4(T,PX,PY,PZ,VX,VY,VZ) + VAX )
        VY1 = VY + (h/2)*(fg.f5(T,PX,PY,PZ,VX,VY,VZ) + VAY )
        VZ1 = VZ + (h/2)*(fg.f6(T,PX,PY,PZ,VX,VY,VZ) + VAZ )
        
    elif fct == "m" :
        PX1 = PX + (h/2)*(fm.f1(T,PX,PY,PZ,VX,VY,VZ) + PAX )
        PY1 = PY + (h/2)*(fm.f2(T,PX,PY,PZ,VX,VY,VZ) + PAY )
        PZ1 = PZ + (h/2)*(fm.f3(T,PX,PY,PZ,VX,VY,VZ) + PAZ )
        VX1 = VX + (h/2)*(fm.f4(T,PX,PY,PZ,VX,VY,VZ) + VAX )
        VY1 = VY + (h/2)*(fm.f5(T,PX,PY,PZ,VX,VY,VZ) + VAY )
        VZ1 = VZ + (h/2)*(fm.f6(T,PX,PY,PZ,VX,VY,VZ) + VAZ )
        
    return (PX1,PY1,PZ1,VX1,VY1,VZ1)
    #retourne la position suivante exacte