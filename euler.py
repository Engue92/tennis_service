#Programme permettant d'utiliser la fonction d'Euler

def euler_methode(f,T,PX,PY,PZ,VX,VY,VZ,i):
#initialisation de la fonction
#PN : paramètre n°N peut-être PX ou PY ou VX...

    h = 0.0005

    if i == 1 :
    #cas ou on calcule pour PX
        PSA = PX + h*f(T,PX,PY,PZ,VX,VY,VZ)
        #PSA : position suivante approximé
        
    elif i == 2 :
    #cas ou on calcule pour PY
        PSA = PY + h*f(T,PX,PY,PZ,VX,VY,VZ)
    
    elif i == 3 :
    #cas ou on calcule pour PZ
        PSA = PZ + h*f(T,PX,PY,PZ,VX,VY,VZ)
    
    elif i == 4 :
    #cas ou on calcule pour VX
        PSA = VX + h*f(T,PX,PY,PZ,VX,VY,VZ)
    
    elif i == 5 :
    #cas ou on calcule pour VY
        PSA = VY + h*f(T,PX,PY,PZ,VX,VY,VZ)
    
    elif i == 6 :
    #cas ou on calcule pour VZ
        PSA = VZ + h*f(T,PX,PY,PZ,VX,VY,VZ)
    
    return (PSA)
    #renvoie position à t+1 approximé avec euler 

