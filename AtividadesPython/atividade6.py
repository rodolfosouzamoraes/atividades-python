#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
6) Uma companhia de teatro planeja dar uma série de 
espetáculos. Para cada espetáculo serão vendidos 120 
ingressos e as despesas fixas somam R$ 2000,00. 
A direção precisa calcular o valor a ser pago por ingresso. 
Para isso, escreva um programa em python que leia o valor que 
ele pretende cobrar no ingresso e informe se esse valor 
cobrirá as despesas e, caso ele cubra, quanto restará de 
lucro para companhia.
"""
print("Informe o valor do ingresso: ")
valor_ingresso = float(input())
total_ingressos = valor_ingresso * 120
if total_ingressos >= 2000:
    lucro = total_ingressos - 2000
    print(f"Lucro final R${round(lucro,2)}")
else:
    print("Não cobriu as dispesas")    
