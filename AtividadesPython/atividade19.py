#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
19) As ma��s custam R$ 0,30 cada se forem compradas 
menos do que uma d�zia, e R$ 0,25 se forem compradas 
pelo menos doze. 
Escreva um programa que leia o n�mero de ma��s 
compradas, calcule e escreva o valor total da compra.
"""
print("Informe a quantidade de ma��s compradas: ")
quantidade_macas = int(input())
if quantidade_macas < 12:
    valor_final = quantidade_macas * 0.3
    print(f"O valor final da compra ser� R${round(valor_final,2)}")
else:
    valor_final = quantidade_macas * 0.25
    print(f"O valor final da compra ser� R${round(valor_final,2)}")