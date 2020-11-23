#Programme permettant d'utiliser la fonction d'Adam-Moulton

def adams_moulton_methode(f,T,PX,PY,PZ,VX,VY,VZ,PSA,i):
#initialisation de la fonction d'Adams-Moulton
#PN : paramètre n°N peut-être PX ou PY ou VX...

    h = 0.0005
    
    if i == 1 :
    #cas ou on calcule pour PX
        PSE = PX + (h/2)*(f(T,PX,PY,PZ,VX,VY,VZ) + PSA )
        #PSE : position suivante exacte
        
    elif i == 2 :
    #cas ou on calcule pour PY
        PSE = PY + (h/2)*(f(T,PX,PY,PZ,VX,VY,VZ) + PSA )
    
    elif i == 3 :
    #cas ou on calcule pour PZ
        PSE = PZ + (h/2)*(f(T,PX,PY,PZ,VX,VY,VZ) + PSA )
    
    elif i == 4 :
    #cas ou on calcule pour VX
        PSE = VX + (h/2)*(f(T,PX,PY,PZ,VX,VY,VZ) + PSA )
    
    elif i == 5 :
    #cas ou on calcule pour VY
        PSE = VY + (h/2)*(f(T,PX,PY,PZ,VX,VY,VZ) + PSA )
    
    elif i == 6 :
    #cas ou on calcule pour VZ
        PSE = VZ + (h/2)*(f(T,PX,PY,PZ,VX,VY,VZ) + PSA )
    
    return (PSE)
    #retourne la position suivante exacte