#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
26) Utilizando o comando match case, 
faça um programa que leia dois números inteiros. 
O programa deve ter um menu de opções que são: 
Somar, dividir, subtrair e multiplicar. 
Onde o usuário deve informar uma letra para poder 
escolher qual opção escolhida. Ao escolher a opção o 
programa deve fazer a operação selecionada com os dois 
números lidos. 
Exemplo: ao informar os números 21 e 50, 
depois informar a letra correspondente a soma, 
o programa deve pegar esses dois números e somar, 
no final deve mostrar o resultado para o usuário.
"""
print("Informe um número: ")
numero1 = int(input())
print("Informe um segundo número: ")
numero2 = int(input())
print("Informe uma das opções abaixo: ")
print("1 - Somar")
print("2 - Dividir")
print("3 - Subtrair")
print("4 - Multiplicar")
opcao = input()
match opcao:
  case "1":
    soma = numero1 + numero2
    print(f"A soma dos números: {soma}")
  case "2":
    divisao = numero1/numero2
    print(f"A divisão dos números: {divisao}")
  case "3":
    subtracao = numero1 - numero2
    print(f"A subtração dos números: {subtracao}")
  case "4":
    multiplicacao = numero1 * numero2
    print(f"A multiplicação dos números: {multiplicacao}")
  case _:
    print("Opção Inválida. Tente novamente mais tarde!")
