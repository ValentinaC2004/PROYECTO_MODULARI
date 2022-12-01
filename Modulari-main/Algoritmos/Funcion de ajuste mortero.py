# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:31:10 2020

@author: JuanJosé
"""
LZ=172
zi=0
Z=40
Mortero=3
MorteroMaximo=4
MorteroMinimo=1.5
CorteMinimo=5
cuenta=0
for i in range(1):
    

    for j in range(2):
        
        from math import floor
        contador2=0
        
        if abs(LZ-zi)%(Z+Mortero)==0:
            
            Ajuste=Mortero
            contador2=1
        else:
            Ajuste=round(abs(LZ-zi)-(Z+Mortero)*floor(round(abs(LZ-zi)/(Z+Mortero),2)),2)
        AjusteMortero=0
        contador=0
        
        if Ajuste!=0 and Ajuste!=Z/2 and Ajuste!=Z:
            
            if abs(Z-Ajuste)<=abs(Z/2-Ajuste):
                if Mortero-(Z-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo:
                    AjusteMortero=-(Z-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                    contador=1
                else:
                    if Z%4==0:
                        if Mortero-((Z-Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z-Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z-Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
                    elif Z%3==0:
                        if Mortero-((Z-Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z-Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z-Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
        
        
            elif Ajuste>Z/2:
                if Mortero+(abs(Z/2-Ajuste))/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                    AjusteMortero= (abs(Z/2-Ajuste))/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                    contador=1
                   
                else:
                    if Z%4==0:
                        
                        if Mortero-((Z-Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z-Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z-Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
                    elif Z%3==0:
                        if Mortero-((Z-Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z-Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z-Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
                            
                        
                    
            elif (Z/2-Ajuste)<=Ajuste:
                
                if Mortero-(Z/2-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo:
                    
                    AjusteMortero=-(Z/2-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                    contador=1
                    
                else:
                    if Z%4==0:
                        if Mortero-((Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
                            
                    elif Z%3==0:
                        if Mortero-((Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
                            
                    
            else:
                
                if contador2==1:
                    Ajuste=0
                
                if Mortero+(Ajuste+Mortero)/(floor(round(abs(LZ-zi)/(Z+Mortero),2))-1)<=MorteroMaximo:
                    
                    AjusteMortero= (Ajuste+Mortero)/(floor(round(abs(LZ-zi)/(Z+Mortero),2))-1)
                    contador=1
                    
                else:
                    if Z%4==0:
                        if Mortero-((Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z/4)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
                    elif Z%3==0:
                        if Mortero-((Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-((Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                            AjusteMortero=-((Z/3)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            contador=1
            
            if contador2!=1:  
                
                if AjusteMortero==0 and Z%Ajuste!=0 and contador!=1:
                
                    if Mortero+(Ajuste-CorteMinimo)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero+(Ajuste-CorteMinimo)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo:
                        AjusteMortero= (Ajuste-CorteMinimo)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                    else:
                        if Mortero-(round(Ajuste,0)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))>=MorteroMinimo and Mortero-(round(Ajuste,0)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))<=MorteroMaximo: 
                            AjusteMortero= -(round(Ajuste,0)-Ajuste)/(floor(round(abs(LZ-zi)/(Z+Mortero),2)))
                            
                    
               
        print ("LZ",LZ)  
                      
        print ("AusteMortero",round(AjusteMortero,2),"Ajuste",Ajuste,"Mortero",Mortero)
        
        Mortero=Mortero+AjusteMortero
    LZ=LZ+1


