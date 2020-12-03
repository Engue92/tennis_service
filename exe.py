#programme d'execution

import position_vitesse_gravite as pvg
import position_vitesse_magnus as pvm
import intervalle_hauteur as ih
import intervalle_rotation as ir

print("\nBonjour, bienvenue dans le calculateur de service !")
print("Voulez vous tester un service ou trouver un intervale ?")
choix1 = input("service ou intervale (S / I) :")
choix1 = str(choix1)

if choix1 == "I" or "i" or "intervale" or "Interval" :
    print("\nQuel type t'interval voulez vous chercher ?")
    choix2 = input("hauteur ou vitesse de rotation (H / VR) :")
    choix2 = str(choix2)
    
    if choix2 == "h" or choix2 == "H" or choix2 == "hauteur" or choix2 == "Hauteur" :
        print("\non recherche un interval de hauteur qui valide un service")
        
        print("\nrentrer une position initial")
        PX = input("En X (entre -0.2 et 0) :")
        PX = float(PX)
        PZ = input("En Z (entre 4.115 et 8.23) :")
        PZ = float(PZ)
        
        print("\nrentrer une vitesse initial") 
        VX = input("En X (positive) :")
        VX = float(VX)
        VY = input("En Y (negative) :")
        VY = float(VY)
        VZ = input("En Z (negative) :")
        VZ = float(VZ)
        
        print("\nCalcule en cours...")
                        
        ih.intervalle_hauteur (PX,PZ,VX,VY,VZ)
    
    elif choix2 == "VR" or choix2 == "vr" or choix2 == "Vr" :
        print("\non recherche un interval de vitesse de rotation qui valide un service")
        
        print("\nrentrer une position initial")
        PX = input("En X (entre -0.2 et 0) :")
        PX = float(PX)
        PY = input("En Y (entre 2 et 3.5) :")
        PY = float(PY)
        PZ = input("En Z (entre 4.115 et 8.23) :")
        PZ = float(PZ)
        
        print("\nrentrer une vitesse initial") 
        VX = input("En X (positive) :")
        VX = float(VX)
        VY = input("En Y (negative) :")
        VY = float(VY)
        VZ = input("En Z (negative) :")
        VZ = float(VZ)
                        
        print("\nCalcule en cours...")
        
        ir.intervalle_rotation(PX,PY,PZ,VX,VY,VZ)

elif choix1 == "S" or "s" or "service" or "Service" :
    print("\non va tester la validité d'un service")
    print("\nQuel force voulez vous prendre en compte ?")

    force = input("(gravité / toutes) :")
    force = str(force)

    if force == "gravité" or "gravite" or "Gravité" or "Gravite" or "g" or "G" :
        print("\nVous avez choisit  de prendre en compte la gravité")
        
        print("\nrentrer une position initial")
        PX = input("En X (entre -0.2 et 0) :")
        PX = float(PX)
        PY = input("En Y (entre 2 et 3.5) :")
        PY = float(PY)
        PZ = input("En Z (entre 4.115 et 8.23) :")
        PZ = float(PZ)
        
        print("\nrentrer une vitesse initial") 
        VX = input("En X (positive) :")
        VX = float(VX)
        VY = input("En Y (negative) :")
        VY = float(VY)
        VZ = input("En Z (negative) :")
        VZ = float(VZ)
            
        pvg.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ)
        
    if force == "toutes" or "toute" or "tout" or "Toutes" or "Touts" or "Tout":
        print("\nVous avez choisit de prendre en compte toutes les forces")
    
        print("\nrentrer une position initial")
        PX = input("En X (entre -0.2 et 0) :")
        PX = float(PX)
        PY = input("En Y (entre 2 et 3.5) :")
        PY = float(PY)
        PZ = input("En Z (entre 4.115 et 8.23) :")
        PZ = float(PZ)
        
        print("\nrentrer une vitesse initial") 
        VX = input("En X (positive) :")
        VX = float(VX)
        VY = input("En Y (negative) :")
        VY = float(VY)
        VZ = input("En Z (negative) :")
        VZ = float(VZ)
        
        print("\nDonner une vitesse de rotation de la balle :")
        VR = input()
        VR = int(VR)
            
        pvm.calcule_position_vitesse_gravite(PX,PY,PZ,VX,VY,VZ,VRD=VR)

            

#pvg.calcule_position_vitesse_gravite(PXD=0,PYD=3,PZD=4.3,VXD=63,VYD=-12,VZD=-14,cote="gauche",croise="bas")
#pvm.calcule_position_vitesse_magnus(PXD=0,PYD=3,PZD=4.3,VXD=66.5,VYD=-12.9,VZD=-14,cote="gauche",croise="bas",VRD=15)
#pvm.calcule_position_vitesse_magnus(PXD=0,PYD=3,PZD=4.3,VXD=67,VYD=-13,VZD=-14,cote="gauche",croise="bas")
#pvm.calcule_position_vitesse_magnus(PXD=0,PYD=3,PZD=4.3,VXD=67,VYD=-14,VZD=-14,cote="gauche",croise="bas")


#ih.intervalle_hauteur (0,4.3,63,-12,-14,"gauche","bas")
#ir.intervalle_rotation(0, 3, 4.3, 66.5, -12.9, -14, "gauche", "bas")









