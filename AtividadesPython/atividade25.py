#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
25) Escreva um programa que leia o valor de 3 ângulos de um 
triângulo e escreva se o triângulo é Acutângulo, 
Retângulo ou Obtusângulo. 
Sendo que:
Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
"""
print("Informe o primeiro ângulo do triângulo: ")
angulo1 = int(input())
print("Informe o segundo ângulo do triângulo: ")
angulo2 = int(input())
print("Informe o terceiro ângulo do triângulo: ")
angulo3 = int(input())

if 90 > angulo1 and 90 > angulo2 and 90 > angulo3:
    print("Triângulo Acutângulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("Triângulo Obtusângulo")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Triângulo Retângulo")