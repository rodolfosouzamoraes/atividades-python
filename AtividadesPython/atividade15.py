#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
Escreva um programa que calcule o salário semanal 
de um trabalhador. As entradas são o número de horas 
trabalhadas na semana e o valor da hora. 
Até 40 h/semana não se acrescenta nenhum adicional. 
Acima de 40h e até 60h há um bônus de 50% para essas horas. 
Acima de 60h há um bônus de 100% para essas horas.
Exemplo acréscimo de porcentagem:
50% porcento a mais de 76 é = 76*1,5
"""
print("Informe o número de horas trabalhadas: ")
horas_trabalhadas = float(input())
print("Informe o valor da hora: ")
valor_hora = float(input())
salario_semanal = horas_trabalhadas * valor_hora
if horas_trabalhadas > 60:
    salario_final = salario_semanal *2
    print(f"Seu salário final é R${round(salario_final,2)}")
elif horas_trabalhadas > 40:
    salario_final = salario_semanal * 1.5
    print(f"Seu salário final é R${round(salario_final,2)}")
else:
    print(f"Seu salário final é R${round(salario_semanal,2)}")

