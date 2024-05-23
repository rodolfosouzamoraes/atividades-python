#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
26) Utilizando o comando match case, 
fa�a um programa que leia dois n�meros inteiros. 
O programa deve ter um menu de op��es que s�o: 
Somar, dividir, subtrair e multiplicar. 
Onde o usu�rio deve informar uma letra para poder 
escolher qual op��o escolhida. Ao escolher a op��o o 
programa deve fazer a opera��o selecionada com os dois 
n�meros lidos. 
Exemplo: ao informar os n�meros 21 e 50, 
depois informar a letra correspondente a soma, 
o programa deve pegar esses dois n�meros e somar, 
no final deve mostrar o resultado para o usu�rio.
"""
print("Informe um n�mero: ")
numero1 = int(input())
print("Informe um segundo n�mero: ")
numero2 = int(input())
print("Informe uma das op��es abaixo: ")
print("1 - Somar")
print("2 - Dividir")
print("3 - Subtrair")
print("4 - Multiplicar")
opcao = input()
match opcao:
  case "1":
    soma = numero1 + numero2
    print(f"A soma dos n�meros: {soma}")
  case "2":
    divisao = numero1/numero2
    print(f"A divis�o dos n�meros: {divisao}")
  case "3":
    subtracao = numero1 - numero2
    print(f"A subtra��o dos n�meros: {subtracao}")
  case "4":
    multiplicacao = numero1 * numero2
    print(f"A multiplica��o dos n�meros: {multiplicacao}")
  case _:
    print("Op��o Inv�lida. Tente novamente mais tarde!")
