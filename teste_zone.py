# programme pour tester le service

def teste_zone(PX,PY,PZ,let,filet,teste=False):
    
    sol = False     # testeur de zone de service   
    service = False # donne la validite du service 
    
    if PY<=0.0325 : # si la balle touche le sol
    # prend en compte le rayon de la balle, elle touche le sol a 0.0325
    
        sol = True  # variable indicant que la balle a touche le sol
        
        if filet == True :  # si le fillet est passe
        
            if PX>= 11.9 and PX<=18.29 and PZ>=0 and PZ<=4.115:  # condition dans laquel le service est dans la zone
                if let == False : # si le service n'est pas let tout est valide le service est bon
                    if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
                        print("service bon")
                    service = True  # variable de validite de service 
                elif let == True :  # si la variable let est vrai et que la balle est passe apres avoir touche le filet
                    if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
                        print("Let, rejouer le service") 
                                
            else :  # dans les cas ou la balle tombe en dehors de la zone
                if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
                    print("faute")
                 
                    
        else :  # si on la balle n'a pas passe le fillet 
            if teste == False :  # si on n'est pas dans une situation de teste d'intervale
                print("faute")   
                
    return(sol,service)  # on renvoit les variable indiquant si la balle a touche le sol et si le service est valide ou non
            
