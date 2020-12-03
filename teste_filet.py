# programme pour tester le passage du filet

def teste_filet(PX,PY,PZ,teste=False):
    
    filet = False  # variable pour indiquer si le filet est passe ou non 
    let = False    # variable pour savoir si on est dans le cas d'un let
    
    if PX<11.89 and PY<=0.0325 :  # si le rebond est avant le filet
        if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
            print("Faute")    
            
    elif PX>=11.89 and PX<11.91 : # quand la balle est au niveau du filet 
    # on prend une marge de 11.89 à 11.91 pour être sur d'avoir une valeur au filet
    
        if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
            print("\nHauteur de la balle au filet : ", PY)   
                
        if PY > 1.1025 :  # si la balle passe le filet
            if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
                print("La balle passe le filet")
            filet = True  # la balle passe le filet
                    
        elif PY >= 1.1 and PY <= 1.1025 :  # si la balle touche le filet mais passe quand même
            if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
                print("la balle touche le filet et passe")
            filet = True  # on passe le fillet
            let = True    # on est dans le cas d'un potentiel let
                        
        elif PY < 1.1 :  # si la balle ne passe pas le filet
            if teste == False :  # si nous ne somme pas dans le cas d'un teste d'intervale
                print("La balle ne passe pas le filet")    
    
    return (filet,let)  # on renvoie les variable de teste de filet et de let