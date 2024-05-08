#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
7) Faça um programa que calcule a fórmula de Bhaskara.
"""
print("Informe o valor de B: ")
b = float(input())
print("Informe o valor de A: ")
a = float(input())
print("Informe o valor de C: ")
c = float(input())
delta = (b**2) - 4*a*c
x_positivo = (-b +(delta**0.5))/(2*a)
x_negativo = (-b -(delta**0.5))/(2*a)
print(f"Valor de X Positivo: {x_positivo}")
print(f"Valor de X Negativo: {x_negativo}")