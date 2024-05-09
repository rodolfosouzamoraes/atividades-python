#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
9)Calcule a média aritmética de 
quatro notas bimestrais, se a média for 
maior ou igual a 50 o aluno está aprovado, 
se não está reprovado. 
Informe a situação do aluno no final do programa.
"""
print("Informe a primeira nota: ")
nota1 = float(input())
print("Informe a segunda nota: ")
nota2 = float(input())
print("Informe a terceira nota: ")
nota3 = float(input())
print("Informe a quarta nota: ")
nota4 = float(input())
media = (nota1+nota2+nota3+nota4)/4
if media >= 50:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
