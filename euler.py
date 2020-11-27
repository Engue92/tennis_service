#Programme permettant d'utiliser la fonction d'Euler

import fonctions_gravite as fg
import fonctions_magnus as fm

def euler_methode(T,PX,PY,PZ,VX,VY,VZ,fct):
#initialisation de la fonction
#PN : paramètre n°N peut-être PX ou PY ou VX...

    h = 0.0005
      
    if fct == "g" :
        PX1 = PX + h*fg.f1(T,PX,PY,PZ,VX,VY,VZ)            
        PY1 = PY + h*fg.f2(T,PX,PY,PZ,VX,VY,VZ)        
        PZ1 = PZ + h*fg.f3(T,PX,PY,PZ,VX,VY,VZ)        
        VX1 = VX + h*fg.f4(T,PX,PY,PZ,VX,VY,VZ)        
        VY1 = VY + h*fg.f5(T,PX,PY,PZ,VX,VY,VZ)    
        VZ1 = VZ + h*fg.f6(T,PX,PY,PZ,VX,VY,VZ)
        
    elif fct == "m" :
        PX1 = PX + h*fm.f1(T,PX,PY,PZ,VX,VY,VZ)            
        PY1 = PY + h*fm.f2(T,PX,PY,PZ,VX,VY,VZ)        
        PZ1 = PZ + h*fm.f3(T,PX,PY,PZ,VX,VY,VZ)        
        VX1 = VX + h*fm.f4(T,PX,PY,PZ,VX,VY,VZ)        
        VY1 = VY + h*fm.f5(T,PX,PY,PZ,VX,VY,VZ)    
        VZ1 = VZ + h*fm.f6(T,PX,PY,PZ,VX,VY,VZ)
    
    
    return (PX1,PY1,PZ1,VX1,VY1,VZ1)
    #renvoie position à t+1 approximé avec euler """


