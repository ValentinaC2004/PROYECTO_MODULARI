# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:24:10 2020

@author: JuanJosé
"""

import numpy as np

# Datos_Muros=np.array([[0,46,46,54,52,82,82,54,54,46],
#                       [5,7,0,0,5,5,55,53,60,60],
#                       [48,46,54,54,82,82,52,54,46,46],
#                       [5,0,0,7,5,55,55,60,60,53]])

# Delta=np.array([[0,48,46,52,52,80,82,52,54,48],
#               [7,7,2,0,7,5,53,53,58,60],
#               [48,48,54,52,82,80,52,52,46,48],
#               [7,0,2,7,7,55,53,60,58,53]])

Datos_Muros=np.array([[1559,1559,1522,1714,1976,1924,2020,2155,2602,1949,2096,2108,2096,1949,1949,1766,1901,2411],
                      [35,135,256,256,35,256,256,210,210,376,743,474,1022,1010,1268,1504,1504,1639],
                      [1559,1501,1624,1834,1976,2020,2020,2602,2602,1949,2031,2108,2031,1949,2096,2423,1901,2411],
                      [244,135,256,256,244,256,35,210,35,743,743,1228,1022,1268,1268,1504,1667,1667]])

Delta=np.array([[1571,1559,1522,1714,1988,1924,2008,2155,2590,1961,2096,2096,2096,1961,1949,1766,1913,2423],
              [35,123,244,244,35,244,256,198,210,376,731,474,1010,1010,1256,1492,1504,1639],
              [1571,1501,1624,1834,1988,2020,2008,2602,2590,1961,2031,2096,2031,1961,2096,2423,1913,2423],
              [244,123,244,244,244,244,35,198,35,743,731,1228,1010,1268,1256,1492,1667,1667]])




for i in range(Datos_Muros.shape[1]):
    TrabaIzquierda="no"
    TrabaDerecha="no"

    print ()
    print ("Muro",i)
    x=Datos_Muros[0][i]
    y=Datos_Muros[1][i]
    
    for j in range(Datos_Muros.shape[1]):
        if i!=j:
            if x==Datos_Muros[0][j] and y==Datos_Muros[1][j] or x==Datos_Muros[2][j] and y==Datos_Muros[3][j] or x==Delta[0][j] and y==Delta[1][j] or x==Delta[2][j] and y==Delta[3][j]:
                TrabaIzquierda="si"
    
    x=Delta[0][i]
    y=Delta[1][i]
    
    for j in range(Datos_Muros.shape[1]):
        if i !=j:
            if x==Datos_Muros[0][j] and y==Datos_Muros[1][j] or x==Datos_Muros[2][j] and y==Datos_Muros[3][j] or x==Delta[0][j] and y==Delta[1][j] or x==Delta[2][j] and y==Delta[3][j]:
                TrabaIzquierda="si"
    
    
    print ("izquierda",TrabaIzquierda)
        
    x=Datos_Muros[2][i]
    y=Datos_Muros[3][i]
    
    for j in range(Datos_Muros.shape[1]):
        if i!=j:
            if x==Datos_Muros[0][j] and y==Datos_Muros[1][j] or x==Datos_Muros[2][j] and y==Datos_Muros[3][j] or x==Delta[0][j] and y==Delta[1][j] or x==Delta[2][j] and y==Delta[3][j]:
                
                TrabaDerecha="si"

    x=Delta[2][i]
    y=Delta[3][i]
    
    for j in range(Datos_Muros.shape[1]):
        if i !=j:
            if x==Datos_Muros[0][j] and y==Datos_Muros[1][j] or x==Datos_Muros[2][j] and y==Datos_Muros[3][j] or x==Delta[0][j] and y==Delta[1][j] or x==Delta[2][j] and y==Delta[3][j]:
                
                TrabaDerecha="si"

    print ("derecha",TrabaDerecha)
































# for i in range(Datos_Muros.shape[1]):
#     """la linea1 es el pedazo de linea que vamos a chequear contra todas
#     las lineas completas de los otros muros line1[xi,yi],[xf-xi/2,yf-yi/2]"""
#     TrabaIzquierda="no"
#     line1=[[Datos_Muros[0][i],Datos_Muros[1][i]],
#             [(Datos_Muros[2][i]+Datos_Muros[0][i])/2,(Datos_Muros[3][i]+Datos_Muros[1][i])/2]]
    
#     for j in range(Datos_Muros.shape[1]):
#         line2=[[Datos_Muros[0][j],Datos_Muros[1][j]],
#                 [Datos_Muros[2][j],Datos_Muros[3][j]]]
#         # print ()
#         # print ("linea 1",line1)
#         # print ("linea2",line2)
#         if line_intersection(line1,line2)!="Not intersect":
#             x,y=line_intersection(line1,line2)
            
#             if x>=min(Datos_Muros[0][i],(Datos_Muros[2][i]+Datos_Muros[0][i])/2) and x<=max(Datos_Muros[0][i],(Datos_Muros[2][i]+Datos_Muros[0][i])/2) and y>=min(Datos_Muros[1][i],(Datos_Muros[3][i]+Datos_Muros[1][i])/2) and y<=max(Datos_Muros[1][i],(Datos_Muros[3][i]+Datos_Muros[1][i])/2):
#                 if x>=min(Datos_Muros[0][j],Datos_Muros[2][j]) and x<=max(Datos_Muros[0][j],Datos_Muros[2][j]) and y>=min(Datos_Muros[1][j],Datos_Muros[3][j]) and y<=max(Datos_Muros[1][j],Datos_Muros[3][j]):
                    
#                     TrabaIzquierda='si'
#                     # print ("Muro inicial",i+1)
#                     # print ("Muro comparativo",j+1)
#                     # print ("x,y",x,y)
#                     # print (TrabaIzquierda)

    
#     print ("Muro",i+1)
#     print (TrabaIzquierda)

# print ()
# print ()

# for i in range(Datos_Muros.shape[1]):
#     """la linea1 es el pedazo de linea que vamos a chequear contra todas
#     las lineas completas de los otros muros line1[xi,yi],[xf-xi/2,yf-yi/2]"""
#     TrabaDerecha="no"
#     line1=[[(Datos_Muros[2][i]+Datos_Muros[0][i])/2,(Datos_Muros[3][i]+Datos_Muros[1][i])/2],
#             [Datos_Muros[2][i],Datos_Muros[3][i]]]
    
#     for j in range(Datos_Muros.shape[1]):
#         line2=[[Datos_Muros[0][j],Datos_Muros[1][j]],
#                 [Datos_Muros[2][j],Datos_Muros[3][j]]]


#         if line_intersection(line1,line2)!="Not intersect":
#             x,y=line_intersection(line1,line2)
            
#             if x>=min((Datos_Muros[2][i]+Datos_Muros[0][i])/2,Datos_Muros[2][i]) and x<=max((Datos_Muros[2][i]+Datos_Muros[0][i])/2,Datos_Muros[2][i]) and y>=min((Datos_Muros[3][i]+Datos_Muros[1][i])/2,Datos_Muros[3][i]) and y<=max((Datos_Muros[3][i]+Datos_Muros[1][i])/2,Datos_Muros[3][i]):
#                 if x>=min(Datos_Muros[0][j],Datos_Muros[2][j]) and x<=max(Datos_Muros[0][j],Datos_Muros[2][j]) and y>=min(Datos_Muros[1][j],Datos_Muros[3][j]) and y<=max(Datos_Muros[1][j],Datos_Muros[3][j]):
                    
#                     TrabaDerecha='si'

    
#     print ("Muro",i+1)
#     print (TrabaDerecha)








