#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
16) Escreva um programa para ler 2 valores e 
escrever o maior deles e se s�o iguais.
"""
print("Informe um valor: ")
valor1 = float(input())
print("Informe um segundo valor: ")
valor2 = float(input())
if valor1 > valor2:
    print(f"O {valor1} � maior que {valor2}.")
elif valor1 < valor2:
    print(f"O {valor2} � maior que {valor1}.")
else:
    print(f"O {valor2} � igual a {valor1}.")