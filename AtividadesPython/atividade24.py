#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
24) Escreva um programa que leia as medidas dos 
lados de um tri�ngulo e escreva se ele � Equil�tero, 
Is�sceles ou Escaleno.
Sendo que:
Tri�ngulo Equil�tero: possui os 3 lados iguais
Tri�ngulo Is�scele: possui 2 lados iguais
Tri�ngulo Escaleno: possui 3 lados diferentes
"""
print("Informe a primeira medida do tri�ngulo: ")
medida1 = int(input())
print("Informe a segunda medida do tri�ngulo: ")
medida2 = int(input())
print("Informe a terceira medida do tri�ngulo: ")
medida3 = int(input())
if medida1 == medida2 == medida3:
    print("Tri�ngulo Equil�tero")
elif medida1 != medida2 != medida3:
    print("Tri�ngulo Escaleno")
elif medida1 == medida2 != medida3:
    print("Tri�ngulo Is�scele")
elif medida1 == medida3 != medida2:
    print("Tri�ngulo Is�scele")
elif medida2 == medida3 != medida1:
    print("Tri�ngulo Is�scele")