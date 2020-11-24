#programme pour tester le service

def teste_zone(PX,PY,PZ,let,cote="gauche",croise="bas"):
    
    zone = False    #testeur de zone de service     
    faute = False   #testeur de faute
    
    #position a la chute de la balle
    if PY<=0.0325 : #si on prend en compte le rayon de la balle, elle touche le sol a 0.0325
        
        if cote == "gauche" or "Gauche" or "g" or "G" :
            if croise == "haut" or "Haut" or "h" or "H" :
                if PX>= 11.9 and PX<=18.29 and PZ>=0 and PZ<=4.115:
                #condition dans laquel le service est dans la zone
                    if let == False :
                        #le service n'est pas let tout est valide le service est bon
                        print("service bon")
                        zone = True
                    elif let == True :
                    #condition dans laquel le service est un let
                        print("Let") 
                else :
                    #dans les autres cas le service est en dehors de la zone donc en faute
                    print("faute")
                    faute = True
                    
            elif croise == "bas" or "Bas" or "b" or "B" :
                if PX>= 11.9 and PX<=18.29 and PZ>=4.115 and PZ<=8.23:
                #condition dans laquel le service est dans la zone
                    if let == False :
                        #le service n'est pas let tout est valide le service est bon
                        print("service bon")
                        zone = True
                    elif let == True :
                    #condition dans laquel le service est un let
                        print("Let") 
                else :
                    #dans les autres cas le service est en dehors de la zone donc en faute
                    print("faute")
                    faute = True
            
        elif cote == "droite" or "Droite" or "d" or "D" :
            if croise == "haut" or "Haut" or "h" or "H" :
                if PX>= 5.49 and PX<=11.89 and PZ>=0 and PZ<=4.115:
                #condition dans laquel le service est dans la zone
                    if let == False :
                        #le service n'est pas let tout est valide le service est bon
                        print("service bon")
                        zone = True
                    elif let == True :
                    #condition dans laquel le service est un let
                        print("Let") 
                else :
                    #dans les autres cas le service est en dehors de la zone donc en faute
                    print("faute")
                    faute = True
                    
            elif croise == "bas" or "Bas" or "b" or "B" :
                if PX>= 5.49 and PX<=11.89 and PZ>=4.115 and PZ<=8.23:
                #condition dans laquel le service est dans la zone
                    if let == False :
                        #le service n'est pas let tout est valide le service est bon
                        print("service bon")
                        zone = True
                    elif let == True :
                    #condition dans laquel le service est un let
                        print("Let") 
                else :
                    #dans les autres cas le service est en dehors de la zone donc en faute
                    print("faute")
                    faute = True
                
        
                
    return(zone,faute)
            
