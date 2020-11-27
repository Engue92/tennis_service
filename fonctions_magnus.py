# programme pour encoder les fonctions en prennant en compte la gravité et l'effet Magnus

import numpy as np

g = 9.81  # force de pesenteur
m = 0.058 # poid de la balle
Cd = 0.65 # coef de la force de frotment
alpha = 1.2*np.pi*(0.065**2)/8      # coef de resistance a l'air
r = [np.sqrt(2)/2,np.sqrt(2)/2,0]   # vecteur de l'axe de rotation de la balle

def f1(T, PX, PY, PZ, VX, VY, VZ) :
    return (VX)

def f2(T, PX, PY, PZ, VX, VY, VZ) :
    return (VY)

def f3(T, PX, PY, PZ, VX, VY, VZ) :
   return (VZ)


def f4(T, PX, PY, PZ, VX, VY, VZ, VR=0.4) :
    
    v = [VX,VY,VZ]      # vecteur vitesse
    n = np.cross(r,v)   # produit vectorielle entre la vitesse et l'axe de rotation de la balle
    norme_v = np.sqrt(VX**2 + VY**2 + VZ**2)      # norme de la vitesse
    norme_n = np.sqrt(n[0]**2 +n[1]**2 +n[2]**2)  # norme du produit vectoriel
    
    return ( - (Cd*alpha*VX*norme_v/m) + ( (alpha/(2 + norme_v*0.98/(np.pi*0.065*VR))) * (norme_v**2/m) * (n[0]/norme_n) ) )


def f5(T, PX, PY, PZ, VX, VY, VZ, VR=0.4) :
    
    v = [VX,VY,VZ]      # vecteur vitesse
    n = np.cross(r,v)   # produit vectorielle entre la vitesse et l'axe de rotation de la balle
    norme_v = np.sqrt(VX**2 + VY**2 + VZ**2)      # norme de la vitesse
    norme_n = np.sqrt(n[0]**2 +n[1]**2 +n[2]**2)  # norme du produit vectoriel
    
    return ( - g - (Cd*alpha*VY*norme_v/m) + ( (alpha/(2 + norme_v*0.98/(np.pi*0.065*VR))) * (norme_v**2/m) * (n[1]/norme_n) ) )  


def f6(T, PX, PY, PZ, VX, VY, VZ, VR=0.4) :
    
    v = [VX,VY,VZ]      # vecteur vitesse
    n = np.cross(r,v)   # produit vectorielle entre la vitesse et l'axe de rotation de la balle
    norme_v = np.sqrt(VX**2 + VY**2 + VZ**2)      # norme de la vitesse
    norme_n = np.sqrt(n[0]**2 +n[1]**2 +n[2]**2)  # norme du produit vectoriel
    
    return ( - (Cd*alpha*VZ*norme_v/m) + ( (alpha/(2 + norme_v*0.98/(np.pi*0.065*VR))) * (norme_v**2/m) * (n[2]/norme_n) ) )



