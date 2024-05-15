#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
11) Faça um programa que leia dois números inteiros. 
O programa deve ter um menu de opções que são: 
Somar, dividir, subtrair e multiplicar. 
Onde o usuário deve informar uma letra para 
poder escolher qual opção escolhida. 
Ao escolher a opção o programa deve fazer a 
operação selecionada com os dois números lidos. 
Exemplo: ao informar os números 21 e 50, 
depois informar a letra correspondente a soma, 
o programa deve pegar esses dois números e somar, 
no final deve mostrar o resultado para o usuário.
"""
print(f"Informe um número inteiro: ")
numero1 = int(input())
print(f"Informe um segundo número inteiro: ")
numero2 = int(input())
print("Escolha uma das opções abaixo:")
print("A - Somar")
print("B - Dividir")
print("C - Subtrair")
print("D - Multiplicar")
opcao_escolhida = input()
if opcao_escolhida == "A":
    soma = numero1 + numero2
    print(f"A soma de {numero1} com {numero2} é igual a {soma}")
elif opcao_escolhida == "B":
    divisao = numero1/numero2
    print(f"A divisão de {numero1} por {numero2} é igual a {divisao}")
elif opcao_escolhida == "C":
    subtrair = numero1 - numero2
    print(f"A subtração de {numero1} com {numero2} é igual a {subtrair}")
elif opcao_escolhida == "D":
    multiplicacao = numero1 * numero2
    print(f"A multiplicação de {numero1} por {numero2} é igual a {multiplicacao}")
else:
    print("Opção inválida! Tente novamente mais tarde.")