#programme pour tester le passage du filet

def teste_filet(PX,PY,PZ):
    
    filet = False
    faute = False
    let = False
    
    #rebond avant le fillet
    if PX<11.89 and PY<=0.0325 :
        print("Faute")
        faute = True            
            
    #Calcule de la hauteur au fillet
    if PX>=11.89 and PX<11.91 : 
        #On prend une marge de 11.89 à 11.91 pour être sur d'avoir une valeur au fillet
        print("Hauteur de la balle au filet : ", PY)
                
        if PY > 1.1025 :
            #condition pour que la balle passe le filet
            print("La balle passe le filet")
            filet = True
                    
        elif PY >= 1.1 and PY <= 1.1025 :
            #conditino dans laquel la balle touche le filet mais le passe tout de même
            print("la balle touche le filet et passe")
            filet = True
            let = True
                        
        elif PY < 1.1 :
            #conditino dans laquel la balle ne passe pas le filet
            print("La balle ne passe pas le filet")
            print("faute")
            faute = True
    
    
    
    return (filet,faute,let)