#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
28) Fa�a um programa em C que simula um 
Menu de Op��es utilizando match case, e que 
para cada uma das op��es abaixo lidas, 
imprima as seguintes mensagens:
Op��es 	Mensagem 
1	Executa a rotina de Inclus�o de Aluno
2	Executa a rotina de Altera��o de Aluno
3	Executa a Rotina de Exclus�o de Aluno
4	Executa a rotina de Consulta de Alunos
Se o usu�rio informar um n�mero menor que 0 
ou maior que 4, informar que a op��o � inv�lida.
"""
print("Informe uma das op��es abaixo: ")
print("1	Executa a rotina de Inclus�o de Aluno")
print("2	Executa a rotina de Altera��o de Aluno")
print("3	Executa a Rotina de Exclus�o de Aluno")
print("4	Executa a rotina de Consulta de Alunos")
opcao = int(input())
match opcao:
    case 1:
        print("Executa a rotina de Inclus�o de Aluno")
    case 2:
        print("Executa a rotina de Altera��o de Aluno")
    case 3:
        print("Executa a Rotina de Exclus�o de Aluno")
    case 4:
        print("Executa a rotina de Consulta de Alunos")
    case _:
        print("Op��o Inv�lida!")

