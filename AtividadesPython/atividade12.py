#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
12) Um tonel de refresco � feito com 80% de �gua mineral e
20% partes de suco de maracuj�. 
Construa um programa em python para calcular quantos
litros de �gua e de suco s�o necess�rios para se fazer 
X litros de refresco (informados pelo usu�rio).
"""

print("Informe a quantidade em litros de refresco que deseja fazer: ")
litros_refresco = float(input())
agua_mineral = litros_refresco * 0.8
parte_suco = litros_refresco * 0.2
print(f"Para fazer {litros_refresco} litros de refresco")
print(f"� necess�rio {agua_mineral} litros de �gua")
print(f"Tamb�m � necess�rio {parte_suco} litros partes de maracuj�")
