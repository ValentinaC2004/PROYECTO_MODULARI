# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:30:51 2020

@author: juanjose
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from time import time
#================================Rotación de un solo vector===================#
#x=np.array((10.0,14.0,14,10,10))
#y=np.array((1.0,1.0,2,2,1))
#Xprima=[]
#Yprima=[]
#
#
#    
#alpha=45*math.pi/180
#MatrizRotacion=np.array([[math.cos(alpha),-math.sin(alpha)],
#                        [math.sin(alpha),math.cos(alpha)]])
#   
#
#for j in range(2):
#    Puntos_A_Rotar=np.array([[x[j]],
#                       [y[j]]])
#    PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
#    
#    Xprima.append(round(PuntosRotados[0,0],5))
#    Yprima.append(round(PuntosRotados[1,0],5))
#print "Xprima",Xprima
#print "Yprima",Yprima    

#Diferencia=[round(Xprima[0]-x[0],2),round(Yprima[0]-y[0],2)]
#
#for i in range(len(Xprima)):
#    Xprima[i]=Xprima[i]-Diferencia[0]
#for i in range(len(Yprima)):
#    Yprima[i]=Yprima[i]-Diferencia[1]

#plt.figure()
#plt.rc('lines', linewidth = 1.0)  # A partir de aquí todas las líneas que dibujemos irán con ancho doble
#plt.xlabel(r"$ (L)$", fontsize = 14, color = 'black')                    
#plt.ylabel(r"$ (h)$", fontsize = 14, color = 'black') 
#plt.plot(Xprima,Yprima,'r',linewidth=10.0)
#X=np.array((x[0],x[1]))
#Y=np.array((y[0],y[1]))
#plt.plot(x,y,'r',linewidth=5.0)
#=============================================================================#


#==================Rotación 3d=================================================

# alpha=math.pi/4
# 
# #================Matriz de rotación antihoraria=============#
# MatrizRotacion=np.array([[math.cos(alpha),-math.sin(alpha)],
#                         [math.sin(alpha),math.cos(alpha)]])
# #===========================================================#
# PuntosGrafica=np.array([(2,6,6,2,2),(0,0,2,2,0),(7,11,11,7,7),(0,0,2,2,0),(12,16,16,12,12),(0,0,2,2,0),(17,21,21,17,17),(0,0,2,2,0)])
# #PuntosGrafica=np.array([(2,6,6,2,2),(0,0,2,2,0),(7,11,11,7,7),(0,0,2,2,0)])
# 
# #se crean los 3 arreglos con las coordenas de cada ladrillo en cad aeje#
# x=np.zeros((len(PuntosGrafica)/2,5))
# y=np.zeros((len(PuntosGrafica)/2,5))
# z=np.zeros((len(PuntosGrafica)/2,5))
# 
# for i in range(len(PuntosGrafica)/2):
#     for j in range(5):
#         x[i,j]=20
# 
# contador=1
# for i in range(len(PuntosGrafica)/2):
#     for j in range(5):
#         y[i,j]=PuntosGrafica[contador,j]
#     contador=contador+2
#     
# contador=0
# for i in range(len(PuntosGrafica)/2):
#     for j in range(5):
#         z[i,j]=PuntosGrafica[contador,j]
#     contador=contador+2
# 
# #======================================================================#    
# for i in range(len(x)):
# 
# 
#     """1. Trasladar todos los ladrillos para que queden sobra la línea"""
#     Xprima=[]
#     Zprima=[]
#     #VECTOR DE REFERENCIA PARA POSICIÓN DEL MURO
#     vz=[2,z[i,0]] #el primer número debe ser donde empieza el muro
#     vx=[20,20]
#     print "vz",vz
#     print "vx",vx
#     print
#     for j in range(2):
#         Puntos_A_Rotar=np.array([[vz[j]],
#                         [vx[j]]])
#          
#         PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
#          
#         Zprima.append(PuntosRotados[0,0])
#         Xprima.append(PuntosRotados[1,0])
#     #=======Mover al punto de origen============#
#     """Como las rotaciones se hacen respecto al cero,
#     calculamos la distancia a la que queda el cálculo
#     con respecto al punto de referencia,para luego 
#     mover las coordenas a este punto original"""   
#     #Diferencia entre el resultado y las coordenadas iniciales#
#     Diferencia=[Xprima[0]-vx[0],Zprima[0]-vz[0]]
#     #=========================================================# 
#     #Movemos las coordenadas al punto de inicio del ladrillo#           
#     for j in range(len(Xprima)):
#         Xprima[j]=round(Xprima[j]-Diferencia[0],2)
#      
#     for j in range(len(Zprima)):
#         Zprima[j]=round(Zprima[j]-Diferencia[1],2)
#     #=========================================================#
#     print "Zprima",Zprima
#     print "Xprima",Xprima
#     print
#     
#     z[i,0]=Zprima[1]
#     z[i,1]=z[i,1]-(vz[1]-Zprima[1])
#     z[i,2]=z[i,1]
#     z[i,3]=Zprima[1]
#     z[i,4]=z[i,0]
#     
#     x[i,0]=Xprima[1]
#     x[i,1]=Xprima[1]
#     x[i,2]=Xprima[1]
#     x[i,3]=Xprima[1]
#     x[i,4]=x[i,0]
#       
#     """2. Rotar los ladrillos en dirección a la línea"""
#     Xprima=[]
#     Zprima=[]
#      
#     for j in range(2):
#         Puntos_A_Rotar=np.array([[z[i,j]],
#                         [x[i,j]]])
#          
#         PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
#          
#         Zprima.append(PuntosRotados[0,0])
#         Xprima.append(PuntosRotados[1,0])
#          
#     Diferencia=[Xprima[0]-x[i,0],Zprima[0]-z[i,0]]
#                 
#     for j in range(len(Xprima)):
#         Xprima[j]=Xprima[j]-Diferencia[0]
#  
#     for j in range(len(Zprima)):
#         Zprima[j]=Zprima[j]-Diferencia[1]
#  
#  
#     x[i,0]=round(Xprima[0],2)
#     x[i,1]=round(Xprima[1],2)
#     x[i,2]=round(Xprima[1],2)
#     x[i,3]=round(Xprima[0],2)
#     x[i,4]=round(x[i,0],0)
#  
#     z[i,0]=round(Zprima[0],2)
#     z[i,1]=round(Zprima[1],2)
#     z[i,2]=round(Zprima[1],2)
#     z[i,3]=round(Zprima[0],2)
#     z[i,4]=round(z[i,0],2)
# 
# for i in range(len(x)):
#     print "Longitud",((z[i,1]-z[i,0])**2+(x[i,1]-x[i,0])**2)**(0.5)
#     
# for i in range(len(x)-1):
#     print "Mortero",((z[i+1,0]-z[i,1])**2+(x[i+1,0]-x[i,1])**2)**(0.5)
# 
# fig = plt.figure()
# # Agrrgamos un plano 3D
# ax = plt.axes(projection='3d')
# 
# 
# Contador4=0
# Contador5=1
# 
# for i in range (len(PuntosGrafica)/2) : 
#     ax.plot_wireframe(z[i],x[i],y[i],facecolors ='c')     
#     Contador4=Contador4+2
#     Contador5=Contador5+2
# 
#==============================================================================




#===================================Grafica 2d planta=========================#
#alpha=math.pi/4
# 
##================Matriz de rotación antihoraria=============#
#MatrizRotacion=np.array([[math.cos(alpha),-math.sin(alpha)],
#                        [math.sin(alpha),math.cos(alpha)]])
#===========================================================#
#PuntosGrafica=np.array([(2,6,6,2,2),(0,0,2,2,0),(7,11,11,7,7),(0,0,2,2,0),(12,16,16,12,12),(0,0,2,2,0),(17,21,21,17,17),(0,0,2,2,0)])
#PuntosGrafica=np.array([[(2,6,6,2,2),(0,0,2,2,0),(7,11,11,7,7),(0,0,2,2,0),(12,16,16,12,12),(0,0,2,2,0)],
#                         [(2,6,6,2,2),(9,9,11,11,9),(7,11,11,7,7),(9,9,11,11,9),(12,16,16,12,12),(9,9,11,11,9)]])
#
##PuntosGrafica=np.array([[(2,6,6,2,2),(0,0,2,2,0),(7,11,11,7,7),(0,0,2,2,0),(12,16,16,12,12),(0,0,2,2,0)]])
#            
#DatosMuros=np.array([(24,	20,	10,	10,	15),
#                    (10,	10,	10,	10,	10),
#                    (30,	30,	10,	10,	0),
#                    (0,	24,	24,	15,	15),
#                    (30,	10,	10,	0,	0),
#                    (24,	24,	14,	15,	0)])
#
#plt.figure()
#plt.rc('lines', linewidth = 1.0)  # A partir de aquí todas las líneas que dibujemos irán con ancho doble
#plt.xlabel(r"$ (L)$", fontsize = 14, color = 'black')                    
#plt.ylabel(r"$ (h)$", fontsize = 14, color = 'black') 
#plt.ylim(0,20)
#plt.xlim(0,25)
#
#
#for i in range(len(PuntosGrafica)):
#    """Ángulo de rotación"""
#    v1=[10.0,0] #vector horizontal. se obtiene de las coordenadas del ladrillo
#    
#    "definir si el muro va horizontal, vertical o diagonal, para saber como organizar el v2"
#    if DatosMuros[2,i]==DatosMuros[4,i]: #si está vertical
#        if DatosMuros[5,i]>DatosMuros[3,i]: #Hacia arriba
#            v2=[0,DatosMuros[0,i]]
#        else:
#            v2=[0,-DatosMuros[0,i]] #Hacia abajo
#    
#    elif DatosMuros[3,i]==DatosMuros[5,i]: #si es horizontal
#        if DatosMuros[4,i]>DatosMuros[2,i]: #Haia la derecha
#            v2=[DatosMuros[0,i],0]
#        else:
#            v2=[-DatosMuros[0,i],0]
#    
#    else: #si está diagonal
#        v2=[] #vector de dirección final del muro
#        if DatosMuros[4,i]>DatosMuros[2,i]:
#            v2.append(DatosMuros[4,i]-DatosMuros[2,i])
#        else:
#            v2.append(DatosMuros[4,i]-DatosMuros[2,i])
#            
#        if DatosMuros[5,i]>DatosMuros[3,i]:
#            v2.append(DatosMuros[5,i]-DatosMuros[3,i])
#        else:
#            v2.append(DatosMuros[5,i]-DatosMuros[3,i])
#    
#    
#    alpha=math.acos((v1[0]*v2[0]+v1[1]*v2[1])/(((v1[0]**2+v1[1]**2)**0.5)*((v2[0]**2+v2[1]**2)**0.5)))
#    
#    if v2[0]<0 and v2[1]<0 or v2[0]==0 and v2[1]<0: #cudrante 3
#        alpha=2*math.pi-alpha
#    if v2[0]>0 and v2[1]<0: #cuadrante 4
#        alpha=2*math.pi-alpha
#    print alpha*180/math.pi
#    
#    
#    #================Matriz de rotación antihoraria=============#
#    MatrizRotacion=np.array([[math.cos(alpha),-math.sin(alpha)],
#                            [math.sin(alpha),math.cos(alpha)]])
#    #===========================================================#
#
#    
#    
#    #se crean los 2 arreglos con las coordenas de cada ladrillo en cada aeje#
#    x=np.zeros((len(PuntosGrafica[i])/2,2))
#    y=np.zeros((len(PuntosGrafica[i])/2,2))
#    
#    contador=0
#    for j in range(len(x)):
#        for k in range(2):
#            x[j,k]=PuntosGrafica[i,contador,k]
#        contador=contador+2
#        
#    contador=1
#    for j in range(len(y)):
#        for k in range(2):
#            y[j,k]=PuntosGrafica[i,contador,k]
#        contdor=contador+2
#        
#    for j in range(len(x)):
#        plt.plot(x[j],y[j],'b',linewidth=2.5)
#        
#    #==========================================================================
#    for j in range(len(x)):
#    
#        
#        """1. Trasladar todos los ladrillos para que queden sobra la línea"""
#        Xprima=[]
#        Zprima=[]
#        #VECTOR DE REFERENCIA PARA POSICIÓN DEL MURO
#        vx=[PuntosGrafica[i,j,0],x[j,0]]
#        vy=[PuntosGrafica[i,1,0],PuntosGrafica[i,1,0]]
#    
#        for k in range(2):
#            Puntos_A_Rotar=np.array([[vx[k]],
#                            [vx[k]]])
#             
#            PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
#             
#            Zprima.append(PuntosRotados[0,0])
#            Xprima.append(PuntosRotados[1,0])
#        #=======Mover al punto de origrn============#
#        """Como las rotaciones se hacen respecto al cero,
#        calculamos la distancia a la que queda el cálculo
#        con respecto al punto de referencia,para luego 
#        mover las coordenas a este punto original"""   
#        #Diferencia entre el resultado y las coordenadas iniciales#
#        Diferencia=[Xprima[0]-vx[0],Zprima[0]-vx[0]]
#        #=========================================================# 
#        #Movemos las coordenadas al punto de inicio del ladrillo#           
#        for k in range(len(Xprima)):
#            Xprima[k]=round(Xprima[k]-Diferencia[0],2)
#         
#        for k in range(len(Zprima)):
#            Zprima[k]=round(Zprima[k]-Diferencia[1],2)
#        #=========================================================#
#        
#        
#        x[i,0]=Zprima[1]
#        x[i,1]=x[i,1]-(vx[1]-Zprima[1])
#        
#        y[i,0]=Xprima[1]
#        y[i,1]=Xprima[1]
#
#        for j in range(len(x)):
#            plt.plot(x[j],y[j],'b',linewidth=2.5)
##======================================================================#    
#      
##"""2. Rotar los ladrillos en dirección a la línea"""
##
##Yprima=[]
##Xprima=[]
##contador=0 
##for j in range(2):
##    Puntos_A_Rotar=np.array([[x[i,j]],
##                    [y[i,contador]]])
##      
#    PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
#      
#    Xprima.append(PuntosRotados[0,0])
#    Yprima.append(PuntosRotados[1,0])
#    contador=contador+2
#Diferencia=[Yprima[0]-y[i,0],Xprima[0]-x[i,0]]
#            
#for j in range(len(Yprima)):
#    Yprima[j]=Yprima[j]-Diferencia[0]
# 
#for j in range(len(Xprima)):
#    Xprima[j]=Xprima[j]-Diferencia[1]
# 
#x[i,0]=
#x[i,1]=
#x[i,2]=
#x[i,3]=
#x[i,4]=
#
#y[i,0]=
#y[i,1]=
#y[i,2]=
#y[i,3]=
#y[i,4]=
 
 #========================Grafica 3d ladrillos especiales=====================#   
fig=plt.figure(num='Modelo 3D')                                                                                                                                                                  #
# Agrrgamos un plano 3D                                                                                                                                                                          #
ax = plt.axes(projection='3d')     
 
 
"""Ángulo de rotación"""
alpha=45*math.pi/180

#================Matriz de rotación antihoraria=============#
MatrizRotacion=np.array([[math.cos(alpha),-math.sin(alpha)],
                        [math.sin(alpha),math.cos(alpha)]])
#===========================================================#
PuntosGrafica=np.array([[8.03,12.03,12.03,9,9,8.03,8.03],
                        [3.6,3.6,4.0,4.0,4.6,4.6,3.6],
                        [12.18,16.18,16.18,13,13,12.18,12.18],
                        [3.6,3.6,4.6,4.6,4,4,3.6],
                        [5.88,5.88,9.88,9.88,9,9,5.88],
                        [7.2,8.2,8.2,8,8,7.2,7.2],
                        [14.03,14.03,10.03,10.03,13,13,14.03],
                        [7.2,8.2,8.2,8.0,8.0,7.2,7.2]])

#PuntosGrafica=np.array([[8.03,12.03,12.03,9,9,8.03,8.03],
#                        [3.6,3.6,4.0,4.0,4.6,4.6,3.6]])


#se crean los 3 arreglos con las coordenas de cada ladrillo en cada aeje#
x=np.zeros((len(PuntosGrafica)/2,7))
y=np.zeros((len(PuntosGrafica)/2,7))
z=np.zeros((len(PuntosGrafica)/2,7))

for i in range(len(PuntosGrafica)/2):
    for j in range(7):
        x[i,j]=0

contador=1
for i in range(len(PuntosGrafica)/2):
    for j in range(7):
        y[i,j]=PuntosGrafica[contador,j]
    contador=contador+2
    
contador=0
for i in range(len(PuntosGrafica)/2):
    for j in range(7):
        z[i,j]=PuntosGrafica[contador,j]
    contador=contador+2


#======================================================================#  
profX=38.0
zi=5.0
 
for i in range(len(x)):

    """1. Trasladar todos los ladrillos para que queden sobra la línea"""
    Xprima=[]
    Zprima=[]
    #VECTOR DE REFERENCIA PARA POSICIÓN DEL MURO
    vz=[z[i,0]-zi]
    vx=[0]
    
    
    Puntos_A_Rotar=np.array([[vz[0]],
                    [vx[0]]])
     
    PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
     
    Zprima.append(PuntosRotados[0,0])
    Xprima.append(PuntosRotados[1,0])
         
    
    #=======Mover al punto de origen============#
    """Como las rotaciones se hacen respecto al cero,
    el resultado son las ditancias absulotas que hay que
    desplazarse desde el punto de origen"""
    print Zprima
    print z
    z[i]=z[i]-((z[i,0]-zi)-Zprima[0])
    print z
    x[i,0]=profX+Xprima[0]
    x[i,1]=profX+Xprima[0]
    x[i,2]=profX+Xprima[0]
    x[i,3]=profX+Xprima[0]
    x[i,4]=profX+Xprima[0]
    x[i,5]=profX+Xprima[0]
    x[i,6]=profX+Xprima[0]
    
    """2. Rotar los ladrillos en dirección a la línea"""
    for j in range(7):
        Xprima=[]
        Zprima=[]
        
        Puntos_A_Rotar=np.array([[z[i,j]-z[i,0]],
                        [x[i,j]-x[i,0]]])
         
        PuntosRotados=np.dot(MatrizRotacion,Puntos_A_Rotar)
#        print Puntos_A_Rotar
#        print
#        print PuntosRotados
        Zprima.append(PuntosRotados[0,0])
        Xprima.append(PuntosRotados[1,0])
             
        
     
        
        
        
        
#        print Zprima,Xprima
        z[i,j]=z[i,0]+round(Zprima[0],2)  
        x[i,j]=x[i,0]+round(Xprima[0],2)
     
#print z,x


for i in range (len(PuntosGrafica)/2) : 
    ax.plot_wireframe(z[i],x[i],y[i],color='k',facecolors ='chocolate')
    ax.plot_wireframe(np.array((5,5)),np.array((40,60)),np.array((0,0)))















