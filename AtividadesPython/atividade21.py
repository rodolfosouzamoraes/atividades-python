#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
21) Tendo como entrada a altura e o sexo 
(codificado da seguinte forma: 1:feminino 2:masculino) 
de uma pessoa, construa um programa que calcule e 
imprima seu peso ideal, utilizando as seguintes Fórmulas:
para homens: (72.7 * Altura)  58
para mulheres: (62.1 * Altura)  44.7
"""

print("Informe sua altura em m: ")
altura = float(input())
print("Escolha uma das opções abaixo para o sexo:")
print("1:Feminino")
print("2:Masculino")
sexo = input()
if sexo == "1":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {round(peso_ideal,2)}")
elif sexo == "2":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {round(peso_ideal,2)}")
else:
    print("Opção inválida! Tente novamente mais tarde.")