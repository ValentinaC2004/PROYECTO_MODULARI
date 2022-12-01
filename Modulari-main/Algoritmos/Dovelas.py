# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.pyplot as plt
def Grafica_Muro(PuntosLadrillos):
    import numpy as np
    
    PuntosGrafica=np.zeros((len(PuntosLadrillos)*2,5))
    Contador4=0
    Contador5=1
    for i in range(len(PuntosLadrillos)): #extraer pontos "X"
        for j in range(4):
            PuntosGrafica[Contador4,j]=PuntosLadrillos[i,Contador5]
            Contador5=Contador5+2
            
        PuntosGrafica[Contador4,4]=PuntosGrafica[Contador4,0]
        Contador5=1
        Contador4=Contador4+2
            
    Contador4=1
    Contador5=2
    for i in range(len(PuntosLadrillos)): #Extraer puntos "Y"
        for j in range(4):
            PuntosGrafica[Contador4,j]=PuntosLadrillos[i,Contador5]        
            Contador5=Contador5+2
        
        PuntosGrafica[Contador4,4]=PuntosGrafica[Contador4,0]
            
        Contador5=2
        Contador4=Contador4+2  
    
       
        
    for i in range(len(PuntosGrafica)): #puntos de gráfica de los ladrillos modulados
            a=PuntosGrafica[i,2]
            PuntosGrafica[i,2]=PuntosGrafica[i,3]
            PuntosGrafica[i,3]=a
            
    #Eliminar filas con valores en cero#
    # i=0
    # while i!=len(PuntosGrafica):
        
    #     if PuntosGrafica[i,0]==0 and PuntosGrafica[i,1]==0 and PuntosGrafica[i,2]==0 and PuntosGrafica[i,3]==0 and PuntosGrafica[i,4]==0:
    #         PuntosGrafica=np.delete(PuntosGrafica,i,axis=0)
    #         i=0
    #     else:
    #         i=i+1
        
    return (PuntosGrafica)



def Punto_dentro_Poligono(x,y,poly):    
 
    n = len(poly)
    inside = False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y
         
    return(inside)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return ("Not intersect")

    d = (det(*line1), det(*line2))
    x = round(det(d, xdiff) / div,2)
    y = round(det(d, ydiff) / div,2)
    return x, y


muro=np.array([[1,	0,	0,	40,	0,	0,	20,	40,	20],
[2,	41.5,	0,	81.5,	0,	41.5,	20,	81.5,	20],
[3,	83,	0,	123,	0,	83,	20,	123,	20],
[4,	124.5,	0,	164.5,	0,	124.5,	20,	164.5,	20],
[5,	166,	0,	178,	0,	166,	20,	178,	20],
[6,	0,	22,	20,	22,	0,	42,	20,	42],
[7,	21.5,	22,	61.5,	22,	21.5,	42,	61.5,	42],
[8,	63,	22,	103,	22,	63,	42,	103,	42],
[9,	104.5,	22,	144.5,	22,	104.5,	42,	144.5,	42],
[10,	146,	22,	178,	22,	146,	42,	178,	42],
[11,	0,	44,	40,	44,	0,	64,	40,	64],
[12,	41.5,	44,	81.5,	44,	41.5,	64,	81.5,	64],
[13,	83,	44,	123,	44,	83,	64,	123,	64],
[14,	124.5,	44,	164.5,	44,	124.5,	64,	164.5,	64],
[15,	166,	44,	178,	44,	166,	64,	178,	64],
[16,	0,	66,	20,	66,	0,	86,	20,	86],
[17,	21.5,	66,	61.5,	66,	21.5,	86,	61.5,	86],
[18,	63,	66,	103,	66,	63,	86,	103,	86],
[19,	104.5,	66,	144.5,	66,	104.5,	86,	144.5,	86],
[20,	146,	66,	178,	66,	146,	86,	178,	86],
[21,	0,	88,	40,	88,  0,	98,	40,	98],
[22,	41.5,	88,	81.5,	88,	41.5,	98,	81.5,	98],
[23,	83,	88,	123,	88,	83,	98,	123,	98],
[24,	124.5,	88,	164.5,	88,	124.5,	98,	164.5,	98],
[25,	166,	88,	178,	88,	166,	98,	178,	98]
])


# dovelas=[[10,0,10,98],
#          [154,0,154,98],
#          [172,0,172,98]]
#GENERACIÓN AUNTOMATICA DE DOVELAS
d=[0.25*40]
LZ=178
LY=98
separacion=30
i=0
j=0
while i <LZ:
    d.append(d[j]+separacion)
    j=j+1
    if d[len(d)-1]>LZ or d[len(d)-1]>LZ-40:
        d[len(d)-1]=(muro[len(muro)-1][3]+muro[len(muro)-1][1])/2
        i=LZ+1
 
dovelas=[]
for i in range(len(d)):
    dovelas.append([d[i],10,d[i],LY])
    
        
for i in range(len(dovelas)):
    x=dovelas[i][0]
    y=dovelas[i][1]
    flag=0
    for j in range(len(muro)):
        poly=[[muro[j][1],muro[j][2]],
              [muro[j][3],muro[j][4]],
              [muro[j][7],muro[j][8]],
              [muro[j][5],muro[j][6]]]
        
        inside=Punto_dentro_Poligono(x,y,poly)
        
        if inside==True:
            flag=1
            
    if flag==0:
        dovelas[i][0]=dovelas[i][0]-40*0.25
        dovelas[i][2]=dovelas[i][0]



for i in range(len(dovelas)):   
    plt.plot(np.array((dovelas[i][0],dovelas[i][2])),np.array((dovelas[i][1],dovelas[i][3])),'darkred',linestyle='--')
    
PuntosGrafica= Grafica_Muro(muro)

Contador4=0
Contador5=1    
for i in range (len(PuntosGrafica)//2) : #dibujar los ladrillos y su número
    if PuntosGrafica[Contador4,0]==0 and PuntosGrafica[Contador4,1]==0 and PuntosGrafica[Contador4,2]==0 and PuntosGrafica[Contador4,3]==0 and PuntosGrafica[Contador4,4]==0:
        "No se imprime nada"
    else:
        plt.plot(PuntosGrafica[Contador4],PuntosGrafica[Contador5],'k',linewidth=0.5)
        
    Contador4=Contador4+2
    Contador5=Contador5+2
        
        
Ladrillos_dovelas=[]
for i in range (len(dovelas)):
    print()
    line1=[[dovelas[i][0],dovelas[i][1]],
            [dovelas[i][2],dovelas[i][3]]]
    
    for j in range(len(muro)):
        line2=[[muro[j][5],muro[j][6]],
                [muro[j][7],muro[j][8]]]
        
        intersection=line_intersection(line1, line2)
        
        if intersection!="Not intersect":
            
            if round(intersection[0],2)>round(muro[j][5],2) and round(intersection[0],2)<round(muro[j][7],2) and round(intersection[1],2)==round(muro[j][6],2) and round(intersection[1],2)==round(muro[j][8],2):
                Ladrillos_dovelas.append(muro[j][0])

print (Ladrillos_dovelas)                


