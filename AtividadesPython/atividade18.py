#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
18) Escreva um programa que verifique a validade 
de uma senha fornecida pelo usu�rio. 
A senha v�lida � o n�mero 1234. 
Devem ser impressas as seguintes mensagens: 
ACESSO PERMITIDO caso a senha seja v�lida. 
ACESSO NEGADO caso a senha seja inv�lida.
"""
print("Informe a senha: ")
senha = input()
if senha == "1234":
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
