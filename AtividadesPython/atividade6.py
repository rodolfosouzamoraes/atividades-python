#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
6) Uma companhia de teatro planeja dar uma s�rie de 
espet�culos. Para cada espet�culo ser�o vendidos 120 
ingressos e as despesas fixas somam R$ 2000,00. 
A dire��o precisa calcular o valor a ser pago por ingresso. 
Para isso, escreva um programa em python que leia o valor que 
ele pretende cobrar no ingresso e informe se esse valor 
cobrir� as despesas e, caso ele cubra, quanto restar� de 
lucro para companhia.
"""
print("Informe o valor do ingresso: ")
valor_ingresso = float(input())
total_ingressos = valor_ingresso * 120
if total_ingressos >= 2000:
    lucro = total_ingressos - 2000
    print(f"Lucro final R${round(lucro,2)}")
else:
    print("N�o cobriu as dispesas")    
