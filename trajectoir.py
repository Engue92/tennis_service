#programme pour afficher la trajectoire de la balle

import matplotlib.pyplot as plt
# importation des bibliotheque necessaire


def trajectoir(X,Y,Z):

    fig = plt.figure()
    ax = fig.gca(projection='3d')   # Affichage en 3D
    
    # coordonne du terrain
    TX = [0, 23.78, 23.78, 0, 0]
    TY= [-1.37, -1.37, 9.6, 9.6, -1.37]
    TZ = [0, 0, 0, 0, 0]
  
    CX1 = [0, 23.78, 23.78, 0, 0]
    CY1 = [0, 0, 8.23, 8.23, 0]
    CZ1 = [0, 0, 0, 0, 0]
    
    CX2 = [5.49, 18.29, 18.29, 5.49, 5.49]
    CY2 = [0, 0, 8.23, 8.23, 0]
    CZ2 = [0, 0, 0, 0, 0]
    
    CX3 = [5.49, 18.29, 18.29, 5.49, 5.49]
    CY3 = [0, 0, 4.115, 4.115, 0]
    CZ3 = [0, 0, 0, 0, 0]
    
    # coordonne du filet
    FX = [11.89, 11.89, 11.89, 11.89, 11.89]
    FY = [-1.37, -1.37, 9.6, 9.6, -1.37]
    FZ = [0, 1.07, 1.07, 0, 0]
    
    ax.plot(CX1,CY1,CZ1, color='darkgoldenrod')   # affichage du terrain
    ax.plot(CX2,CY2,CZ2, color='darkgoldenrod')   # affichage du terrain
    ax.plot(CX3,CY3,CZ3, color='darkgoldenrod')   # affichage du terrain
    ax.plot(TX,TY,TZ, color='darkgoldenrod')      # affichage du terrain
    ax.plot(FX,FY,FZ, color='black')              # affichage du filet
      
    ax.plot(X, Z, Y, label='Courbe')   # Tracé de la trajectoire de la balle



    plt.show()
    
    
    
    
    
    