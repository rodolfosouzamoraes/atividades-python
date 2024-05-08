#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
4) João recebeu seu salário e precisa pagar duas contas 
que estão atrasadas. Como as contas estão atrasadas, 
João pagará multa de 2% sobre as contas. 
Desenvolva um algoritmo que leia as informações 
necessárias e que calcule quantas restará do salário do João.
"""
print("Informe o salário do João:")
salario_joao = float(input())
print("Informe o valor da primeira conta: ")
conta1 = float(input())
print("Informe o valor da segunda conta: ")
conta2 = float(input())
multa = (conta1 + conta2) * 1.02
salario_final = salario_joao - multa
print(f"O salário final de João: R${round(salario_final,2)}")
