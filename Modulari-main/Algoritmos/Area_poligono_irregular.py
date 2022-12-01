# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:14:38 2020

@author: JuanJosé
"""


""""Area de un poligo irregular:
    si los vectores se enumeran 
    en sentido del reloj, el area será positiva,
    de lo contrario será negativa. Por 
    eso se pone en valor absoluto"""


def find_area(array):
    a = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        ox,oy = x,y
    return (abs(a/2))

l=[[ 870.,   30.],
        [1070.,   30.],
        [1070.,  200.],
        [ 870.,  200.],
        [ 870.,  170.],
        [1020.,  170.],
        [1020.,   70.],
        [ 870.,   70.],
        [870.,   30.]]

print (find_area(l))