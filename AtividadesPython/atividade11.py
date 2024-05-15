#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
11) Fa�a um programa que leia dois n�meros inteiros. 
O programa deve ter um menu de op��es que s�o: 
Somar, dividir, subtrair e multiplicar. 
Onde o usu�rio deve informar uma letra para 
poder escolher qual op��o escolhida. 
Ao escolher a op��o o programa deve fazer a 
opera��o selecionada com os dois n�meros lidos. 
Exemplo: ao informar os n�meros 21 e 50, 
depois informar a letra correspondente a soma, 
o programa deve pegar esses dois n�meros e somar, 
no final deve mostrar o resultado para o usu�rio.
"""
print(f"Informe um n�mero inteiro: ")
numero1 = int(input())
print(f"Informe um segundo n�mero inteiro: ")
numero2 = int(input())
print("Escolha uma das op��es abaixo:")
print("A - Somar")
print("B - Dividir")
print("C - Subtrair")
print("D - Multiplicar")
opcao_escolhida = input()
if opcao_escolhida == "A":
    soma = numero1 + numero2
    print(f"A soma de {numero1} com {numero2} � igual a {soma}")
elif opcao_escolhida == "B":
    divisao = numero1/numero2
    print(f"A divis�o de {numero1} por {numero2} � igual a {divisao}")
elif opcao_escolhida == "C":
    subtrair = numero1 - numero2
    print(f"A subtra��o de {numero1} com {numero2} � igual a {subtrair}")
elif opcao_escolhida == "D":
    multiplicacao = numero1 * numero2
    print(f"A multiplica��o de {numero1} por {numero2} � igual a {multiplicacao}")
else:
    print("Op��o inv�lida! Tente novamente mais tarde.")