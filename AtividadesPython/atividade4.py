#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
4) Jo�o recebeu seu sal�rio e precisa pagar duas contas 
que est�o atrasadas. Como as contas est�o atrasadas, 
Jo�o pagar� multa de 2% sobre as contas. 
Desenvolva um algoritmo que leia as informa��es 
necess�rias e que calcule quantas restar� do sal�rio do Jo�o.
"""
print("Informe o sal�rio do Jo�o:")
salario_joao = float(input())
print("Informe o valor da primeira conta: ")
conta1 = float(input())
print("Informe o valor da segunda conta: ")
conta2 = float(input())
multa = (conta1 + conta2) * 1.02
salario_final = salario_joao - multa
print(f"O sal�rio final de Jo�o: R${round(salario_final,2)}")
