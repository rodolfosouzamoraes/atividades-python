#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
25) Escreva um programa que leia o valor de 3 �ngulos de um 
tri�ngulo e escreva se o tri�ngulo � Acut�ngulo, 
Ret�ngulo ou Obtus�ngulo. 
Sendo que:
Tri�ngulo Ret�ngulo: possui um �ngulo reto. (igual a 90�)
Tri�ngulo Obtus�ngulo: possui um �ngulo obtuso. (maior que 90�)
Tri�ngulo Acut�ngulo: possui tr�s �ngulos agudos. (menor que 90�)
"""
print("Informe o primeiro �ngulo do tri�ngulo: ")
angulo1 = int(input())
print("Informe o segundo �ngulo do tri�ngulo: ")
angulo2 = int(input())
print("Informe o terceiro �ngulo do tri�ngulo: ")
angulo3 = int(input())

if 90 > angulo1 and 90 > angulo2 and 90 > angulo3:
    print("Tri�ngulo Acut�ngulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Tri�ngulo Obtus�ngulo")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Tri�ngulo Ret�ngulo")