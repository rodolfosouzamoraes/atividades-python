#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
24) Escreva um programa que leia as medidas dos 
lados de um triângulo e escreva se ele é Equilátero, 
Isósceles ou Escaleno.
Sendo que:
Triângulo Equilátero: possui os 3 lados iguais
Triângulo Isóscele: possui 2 lados iguais
Triângulo Escaleno: possui 3 lados diferentes
"""
print("Informe a primeira medida do triângulo: ")
medida1 = int(input())
print("Informe a segunda medida do triângulo: ")
medida2 = int(input())
print("Informe a terceira medida do triângulo: ")
medida3 = int(input())
if medida1 == medida2 == medida3:
    print("Triângulo Equilátero")
elif medida1 != medida2 != medida3:
    print("Triângulo Escaleno")
elif medida1 == medida2 != medida3:
    print("Triângulo Isóscele")
elif medida1 == medida3 != medida2:
    print("Triângulo Isóscele")
elif medida2 == medida3 != medida1:
    print("Triângulo Isóscele")