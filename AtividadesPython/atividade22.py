#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
22) Escreva um programa para ler o n�mero de 
lados de um pol�gono regular.
Calcular e imprimir o seguinte:
Se o n�mero de lados for igual a 3 escrever TRI�NGULO;
Se o n�mero de lados for igual a 4 escrever QUADRADO;
Se o n�mero de lados for igual a 5 escrever PENT�GONO;
Caso o n�mero de lados seja inferior a 3 escrever N�O � 
UM POL�GONO;
Caso o n�mero de lados seja superior a 5 escrever 
POL�GONO N�O IDENTIFICADO.
"""


print("Informe o n�mero de lados: ")
lados = int(input())
if lados == 3:
    print("TRI�NGULO")
elif lados == 4:
    print("QUADRADO")
elif lados == 5:
    print("PENT�GONO")
elif lados < 3:
    print("N�O � UM POL�GONO")
else:
    print("POL�GONO N�O IDENTIFICADO")
