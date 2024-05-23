#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Escreva um programa para ler 3 valores inteiros e escrever o
maior deles. 
Considere que o usuário não informará valores iguais.
"""

print("Informe um valor: ")
valor1 = int(input())
print("Informe um segundo valor: ")
valor2 = int(input())
print("Informe um terceiro valor: ")
valor3 = int(input())

if valor1 > valor2 > valor3:
    print(f"O valor {valor1} é o maior!")
elif valor1 > valor3 > valor2:
    print(f"O valor {valor1} é o maior!")
elif valor2 > valor1 > valor3:
    print(f"O valor {valor2} é o maior!")
elif valor2 > valor3 > valor1:
    print(f"O valor {valor2} é o maior!")
elif valor3 > valor1 > valor2:
    print(f"O valor {valor3} é o maior!")
else:
    print(f"O valor {valor3} é o maior!")
