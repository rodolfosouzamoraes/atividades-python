#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
17) Escreva um programa para ler o ano de nascimento 
de uma pessoa e escrever uma mensagem que 
diga se ela poderá ou não votar este ano 
(não é necessário considerar o mês em que ela nasceu).
"""
print("Informe o seu ano de nascimento: ")
ano_nascimento = int(input())
idade = 2024 - ano_nascimento
if idade >= 16:
    print("Você pode votar esse ano!")
else:
    print("Você não pode votar esse ano!")