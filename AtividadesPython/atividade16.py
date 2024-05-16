#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
16) Escreva um programa para ler 2 valores e 
escrever o maior deles e se são iguais.
"""
print("Informe um valor: ")
valor1 = float(input())
print("Informe um segundo valor: ")
valor2 = float(input())
if valor1 > valor2:
    print(f"O {valor1} é maior que {valor2}.")
elif valor1 < valor2:
    print(f"O {valor2} é maior que {valor1}.")
else:
    print(f"O {valor2} é igual a {valor1}.")