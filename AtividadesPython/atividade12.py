#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
12) Um tonel de refresco é feito com 80% de água mineral e
20% partes de suco de maracujá. 
Construa um programa em python para calcular quantos
litros de água e de suco são necessários para se fazer 
X litros de refresco (informados pelo usuário).
"""

print("Informe a quantidade em litros de refresco que deseja fazer: ")
litros_refresco = float(input())
agua_mineral = litros_refresco * 0.8
parte_suco = litros_refresco * 0.2
print(f"Para fazer {litros_refresco} litros de refresco")
print(f"É necessário {agua_mineral} litros de água")
print(f"Também é necessário {parte_suco} litros partes de maracujá")
