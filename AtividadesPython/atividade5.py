#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
5) Fa�a um programa em python que leia os valores 
necess�rios e efetue o seguinte c�lculo: 
D = (X*2 � X*1)*2 + (Y*2 � Y*1)*2
"""
print("Informe o valor de X: ")
x = float(input())
print("Informe o valor de Y: ")
y = float(input())
d = (x*2 - x*1)*2 + (y*2 - y*1)*2
print(f"O resultado final de D �: {d}")