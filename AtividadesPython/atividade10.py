#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
10) Fa�a um programa que leia 3 notas e calcule 
a m�dia aritm�tica. 
Leia tamb�m a frequ�ncia desse aluno. 
Se a frequ�ncia for menor que 70, o aluno 
est� reprovado por frequ�ncia. 
Se o aluno tiver com a frequ�ncia maior 
ou igual a 70 o programa deve 
verificar se ele est� aprovado, 
de recupera��o ou reprovado por nota. 
Para estar aprovado o aluno deve ter uma 
m�dia maior ou igual a 60, para estar de 
recupera��o o aluno deve estar maior 
que ou igual a 40, para estar reprovado 
por nota ele deve ter a m�dia abaixo de 40. 
O programa deve informar no final a situa��o do aluno.
"""
print("Informe a primeira nota: ")
nota1 = float(input())
print("Informe a segunda nota: ")
nota2 = float(input())
print("Informe a terceira nota: ")
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3
print("Informe a frequ�ncia: ")
frequencia = float(input())
if frequencia < 70:
    print("Aluno reprovado por frequ�ncia!")
else:
    if media >= 60:
        print("Aluno Aprovado!")
    elif media >= 40:
        print("Aluno de Recupera��o!")
    else:
        print("Aluno Reprovado!")
    