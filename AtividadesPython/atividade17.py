#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
17) Escreva um programa para ler o ano de nascimento 
de uma pessoa e escrever uma mensagem que 
diga se ela poder� ou n�o votar este ano 
(n�o � necess�rio considerar o m�s em que ela nasceu).
"""
print("Informe o seu ano de nascimento: ")
ano_nascimento = int(input())
idade = 2024 - ano_nascimento
if idade >= 16:
    print("Voc� pode votar esse ano!")
else:
    print("Voc� n�o pode votar esse ano!")