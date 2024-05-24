#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Faça um programa que leia um número de 1 a 12 
e mostre ao usuário qual mês pertence 
aquele número. 
Utilize match case para resolver esse problema. 
No final informe ao usuário qual mês se 
refere aquele número informado.
Se o usuário informar um número menor que 
1 ou maior que 12, informar que a opção 
é inválida.
"""
print("Informe o número do mês: ")
mes = int(input())
match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
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
        print("Opção Inválida!")