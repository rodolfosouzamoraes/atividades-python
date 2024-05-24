#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
28) Faça um programa em C que simula um 
Menu de Opções utilizando match case, e que 
para cada uma das opções abaixo lidas, 
imprima as seguintes mensagens:
Opções 	Mensagem 
1	Executa a rotina de Inclusão de Aluno
2	Executa a rotina de Alteração de Aluno
3	Executa a Rotina de Exclusão de Aluno
4	Executa a rotina de Consulta de Alunos
Se o usuário informar um número menor que 0 
ou maior que 4, informar que a opção é inválida.
"""
print("Informe uma das opções abaixo: ")
print("1	Executa a rotina de Inclusão de Aluno")
print("2	Executa a rotina de Alteração de Aluno")
print("3	Executa a Rotina de Exclusão de Aluno")
print("4	Executa a rotina de Consulta de Alunos")
opcao = int(input())
match opcao:
    case 1:
        print("Executa a rotina de Inclusão de Aluno")
    case 2:
        print("Executa a rotina de Alteração de Aluno")
    case 3:
        print("Executa a Rotina de Exclusão de Aluno")
    case 4:
        print("Executa a rotina de Consulta de Alunos")
    case _:
        print("Opção Inválida!")

