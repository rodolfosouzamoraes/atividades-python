#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
14) Leia um n�mero inteiro e diga 
se ele � par ou impar
"""
print("Informe um n�mero:")
numero = int(input())
par = numero % 2
if par == 0:
    print("N�mero Par")
else:
    print("N�mero �mpar")
