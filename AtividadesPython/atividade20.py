#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
20) Escreva um programa para ler 3 valores inteiros 
(considere que não serão lidos valores iguais) e 
escrevê-los em ordem crescente.
"""

print("Informe um valor: ")
valor1 = int(input())
print("Informe um segundo valor: ")
valor2 = int(input())
print("Informe um terceiro valor: ")
valor3 = int(input())
if valor1 < valor2 < valor3:
    print(f"{valor1}, {valor2}, {valor3}")
elif valor1 < valor3 < valor2:
    print(f"{valor1}, {valor3}, {valor2}")
elif valor2 < valor1 < valor3:
    print(f"{valor2}, {valor1}, {valor3}")
elif valor2 < valor3 < valor1:
    print(f"{valor2}, {valor3}, {valor1}")
elif valor3 < valor1 < valor2:
    print(f"{valor3}, {valor1}, {valor2}")
else:
    print(f"{valor3}, {valor2}, {valor1}")
    