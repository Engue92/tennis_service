#programme d'execution

import position_vitesse_gravite as pvg
import position_vitesse_magnus as pvm

"""
print("\nBonjour, bienvenue dans le calculateur de service !")
print("\nQuel force voulez vous prendre en compte ?")

force = "null"
cote = "null"
croise = "null"

force = input("(gravité / toutes) :")
force = str(force)

print("\nDe quel coté voulez vous servire ?")
cote = input("(droite / gauche) :")
cote = str(cote)
    
print("\nVoulez vous servir depuis le bas ou le haut ?")
croise = input("(haut / bas)")
croise = str(croise)

if force == "gravité" or "gravite" or "Gravité" or "Gravite" or "g" or "G" :
    print("\nVous avez choisit  de prendre en compte la gravité")
    print("Vous servez de la ", cote," vers le/la ", croise)
        
    if cote == "gauche" or "Gauche" or "g" or "G" :
        
        if croise == "haut" or "Haut" or "h" or "H" :
            print("\nrentrer une position initial")
            PX = input("En X (entre -0.2 et 0) :")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3.5) :")
            PY = int(PY)
            PZ = input("En Z (entre 4.115 et 8.23) :")
            PZ = int(PZ)
    
            print("\nrentrer une vitesse initial") 
            VX = input("En X (positive) :")
            VX = int(VX)
            VY = input("En Y (negative) :")
            VY = int(VY)
            VZ = input("En Z (negative) :")
            VZ = int(VZ)
            
            pvg.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)

            
        elif croise == "bas" or "Bas" or "b" or "B" :
            print("\nrentrer une position initial")
            PX = input("En X (entre -0.2 et 0) :")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3.5) :")
            PY = int(PY)
            PZ = input("En Z (entre 0 et 4.115) :")
            PZ = int(PZ)
    
            print("\nrentrer une vitesse initial") 
            VX = input("En X (positive) :")
            VX = int(VX)
            VY = input("En Y (negative) :")
            VY = int(VY)
            VZ = input("En Z (positive) :")
            VZ = int(VZ)
            
            pvg.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)
            
    if cote == "droite" or "Droite" or "d" or "D" :
        
        if croise == "haut" or "Haut" or "h" or "H" :
            print("\nrentrer une position initial")
            PX = input("En X (entre 23.78 et 23.9) :")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3.5) :")
            PY = int(PY)
            PZ = input("En Z (entre 4.115 et 8.23) :")
            PZ = int(PZ)
            
            print("\nrentrer une vitesse initial") 
            VX = input("En X (negative) :")
            VX = int(VX)
            VY = input("En Y (negative) :")
            VY = int(VY)
            VZ = input("En Z (negative) :")
            VZ = int(VZ)
            
            pvg.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)
            
        elif croise == "bas" or "Bas" or "b" or "B" :
            print("\nrentrer une position initial")
            PX = input("En X (entre 23.78 et 23.9) :")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3.5) :")
            PY = int(PY)
            PZ = input("En Z (entre 0 et 4.115) :")
            PZ = int(PZ)
    
            print("\nrentrer une vitesse initial") 
            VX = input("En X (negative) :")
            VX = int(VX)
            VY = input("En Y (negative) :")
            VY = int(VY)
            VZ = input("En Z (positive) :")
            VZ = int(VZ)
            
            pvg.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)
    
        
if force == "toutes" or "toute" or "tout" or "Toutes" or "Touts" or "Tout":
    print("\nVous avez choisit de prendre en compte toutes les forces")
    print("Vous servez de la ", cote," vers le/la ", croise)
    
    if cote == "droite" or "Droite" or "d" or "D" :
        
        if croise == "haut" or "Haut" or "h" or "H" :
            print("\nrentrer une position initial")
            PX = input("En X (entre -0.2 et 0):")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3):")
            PY = int(PY)
            PZ = input("En Z (entre 4.12 et 4.4):")
            PZ = int(PZ)
    
            print("\nrentrer une vitesse initial") 
            VX = input("En X :")
            VX = int(VX)
            VY = input("En Y :")
            VY = int(VY)
            VZ = input("En Z :")
            VZ = int(VZ)
            
            pvm.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)

            
        elif croise == "bas" or "Bas" or "b" or "B" :
            print("\nrentrer une position initial")
            PX = input("En X (entre -0.2 et 0):")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3):")
            PY = int(PY)
            PZ = input("En Z (entre 4.12 et 4.4):")
            PZ = int(PZ)
    
            print("\nrentrer une vitesse initial") 
            VX = input("En X :")
            VX = int(VX)
            VY = input("En Y :")
            VY = int(VY)
            VZ = input("En Z :")
            VZ = int(VZ)
            
            pvm.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)
            
    if cote == "gauche" or "Gauche" or "g" or "G" :
        
        if croise == "haut" or "Haut" or "h" or "H" :
            print("\nrentrer une position initial")
            PX = input("En X (entre -0.2 et 0):")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3):")
            PY = int(PY)
            PZ = input("En Z (entre 4.12 et 4.4):")
            PZ = int(PZ)
            
            print("\nrentrer une vitesse initial") 
            VX = input("En X :")
            VX = int(VX)
            VY = input("En Y :")
            VY = int(VY)
            VZ = input("En Z :")
            VZ = int(VZ)
            
            pvm.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)
            
        elif croise == "bas" or "Bas" or "b" or "B" :
            print("\nrentrer une position initial")
            PX = input("En X (entre -0.2 et 0):")
            PX = int(PX)
            PY = input("En Y (entre 2 et 3):")
            PY = int(PY)
            PZ = input("En Z (entre 4.12 et 4.4):")
            PZ = int(PZ)
    
            print("\nrentrer une vitesse initial") 
            VX = input("En X :")
            VX = int(VX)
            VY = input("En Y :")
            VY = int(VY)
            VZ = input("En Z :")
            VZ = int(VZ)
            
            pvm.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,cote,croise)
    """

pvg.calcule_position_vitesse_gravite(PXD=0,PYD=3,PZD=4.3,VXD=63,VYD=-12,VZD=-14,cote="gauche",croise="bas")


