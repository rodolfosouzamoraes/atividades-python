#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
8) Leia um n�mero e diga se esse n�mero � 
positivo, negativo ou neutro.
"""
print("Informe um n�mero: ")
numero = float(input())
if numero > 0:
    print("N�mero Positivo.")
elif numero < 0:
    print("N�mero Negativo.")
else:
    print("N�mero Neutro.")