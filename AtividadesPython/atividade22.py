#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""
22) Escreva um programa para ler o número de 
lados de um polígono regular.
Calcular e imprimir o seguinte:
Se o número de lados for igual a 3 escrever TRIÂNGULO;
Se o número de lados for igual a 4 escrever QUADRADO;
Se o número de lados for igual a 5 escrever PENTÁGONO;
Caso o número de lados seja inferior a 3 escrever NÃO É 
UM POLÍGONO;
Caso o número de lados seja superior a 5 escrever 
POLÍGONO NÃO IDENTIFICADO.
"""


print("Informe o número de lados: ")
lados = int(input())
if lados == 3:
    print("TRIÂNGULO")
elif lados == 4:
    print("QUADRADO")
elif lados == 5:
    print("PENTÁGONO")
elif lados < 3:
    print("NÃO É UM POLÍGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO")
