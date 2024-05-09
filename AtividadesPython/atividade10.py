#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
10) Faça um programa que leia 3 notas e calcule 
a média aritmética. 
Leia também a frequência desse aluno. 
Se a frequência for menor que 70, o aluno 
está reprovado por frequência. 
Se o aluno tiver com a frequência maior 
ou igual a 70 o programa deve 
verificar se ele está aprovado, 
de recuperação ou reprovado por nota. 
Para estar aprovado o aluno deve ter uma 
média maior ou igual a 60, para estar de 
recuperação o aluno deve estar maior 
que ou igual a 40, para estar reprovado 
por nota ele deve ter a média abaixo de 40. 
O programa deve informar no final a situação do aluno.
"""
print("Informe a primeira nota: ")
nota1 = float(input())
print("Informe a segunda nota: ")
nota2 = float(input())
print("Informe a terceira nota: ")
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3
print("Informe a frequência: ")
frequencia = float(input())
if frequencia < 70:
    print("Aluno reprovado por frequência!")
else:
    if media >= 60:
        print("Aluno Aprovado!")
    elif media >= 40:
        print("Aluno de Recuperação!")
    else:
        print("Aluno Reprovado!")
    