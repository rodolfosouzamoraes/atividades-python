#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
29) Fa�a um programa em python que leia um total de 
1 a 10 Terabytes e converta para as seguintes nota��es: 
0 � para bytes 
1 � para Kilobyte 
2 � para Megabyte 
3 � para Gigabyte 
Informe ao usu�rio o resultado da convers�o realizada.
Se o usu�rio informar um n�mero menor que 0 ou 
maior que 3, informar que a op��o � inv�lida.
"""
print("Informe a quantidade de terabyte: ")
terabyte = int(input())
if terabyte > 0 and terabyte <=10:
    print("Escolha uma das op��es abaixo para converter:")
    print("0 � para bytes")
    print("1 � para Kilobyte ")
    print("2 � para Megabyte ")
    print("3 � para Gigabyte")
    opcao = int(input())
    match opcao:
        case 3:
            gigabyte = terabyte * 1024
            print(f"{gigabyte}GB")
        case 2:
            megabyte = terabyte * 1024**2
            print(f"{megabyte}MB")
        case 1: 
            kilobyte = terabyte * 1024**3
            print(f"{kilobyte}KB")
        case 0:
            byte = terabyte * 1024**4
            print(f"{byte}B")
        case _:
            print("Op��o Inv�lida!")
else:
    print("Terabyte informado fora do intervalo!")
        