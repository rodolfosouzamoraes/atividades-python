#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

print("Informe o n�mero do dia:")
dia = int(input())
match dia:
  case 1:
    print("Domingo.")
  case 2:
    print("Segunda.")
  case 3:
    print("Ter�a")
  case 4:
    print("Quarta")
  case 5:
    print("Quinta")
  case 6:
    print("Sexta")
  case 7:
    print("S�bado")
  case _:
    print("Dia inv�lido.")