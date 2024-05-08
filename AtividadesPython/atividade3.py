#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
3) O custo ao consumidor de um carro novo é a soma do 
custo de fábrica com a percentagem do distribuidor e 
dos impostos (aplicados ao custo de fábrica). 
Supondo que a percentagem do distribuidor seja de 28% e 
os impostos de 45%, escreva um programa em python 
que leia o custo de fábrica de um carro e escreva o 
custo ao consumidor.
"""
print("Informe o custo de fabrica do carro: ")
custo_fabrica = float(input())
distribuidor = custo_fabrica * 0.28
imposto = custo_fabrica * 0.45
custo_consumidor = custo_fabrica + distribuidor + imposto
print(f"O custo do consumidor foi R${round(custo_consumidor,2)}")
