#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
14) Leia um número inteiro e diga 
se ele é par ou impar
"""
print("Informe um número:")
numero = int(input())
par = numero % 2
if par == 0:
    print("Número Par")
else:
    print("Número Ímpar")
