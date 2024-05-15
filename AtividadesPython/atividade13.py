#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
13) Um comerciante deseja fazer o levantamento do lucro das 
mercadorias que ele comercializa. 
Para isto, crie um programa em python que leia o código, 
o preço de compra e o preço de venda de uma mercadoria e 
determine se ela proporciona:
lucro < 10%
10% ≤ lucro ≤ 20%
lucro > 20%
"""
print("Informe o código do produto: ")
codigo = input()
print("Informe o preço de compra do produto: ")
preco_compra = float(input())
print("Informe o preço de venda do produto: ")
preco_venda = float(input())
lucro = (1 - (preco_compra/preco_venda)) * 100
if lucro > 20:
    print("Lucro maior que 20%.")
elif lucro > 10:
    print("Lucro entre 10% e 20% ")
else:
    print("Lucro menor que 10%")

