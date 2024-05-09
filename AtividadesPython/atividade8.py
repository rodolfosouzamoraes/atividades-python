#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
8) Leia um número e diga se esse número é 
positivo, negativo ou neutro.
"""
print("Informe um número: ")
numero = float(input())
if numero > 0:
    print("Número Positivo.")
elif numero < 0:
    print("Número Negativo.")
else:
    print("Número Neutro.")