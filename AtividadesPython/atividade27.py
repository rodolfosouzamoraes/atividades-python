#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Fa�a um programa que leia um n�mero de 1 a 12 
e mostre ao usu�rio qual m�s pertence 
aquele n�mero. 
Utilize match case para resolver esse problema. 
No final informe ao usu�rio qual m�s se 
refere aquele n�mero informado.
Se o usu�rio informar um n�mero menor que 
1 ou maior que 12, informar que a op��o 
� inv�lida.
"""
print("Informe o n�mero do m�s: ")
mes = int(input())
match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Mar�o")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Op��o Inv�lida!")