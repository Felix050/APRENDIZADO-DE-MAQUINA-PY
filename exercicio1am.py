# -*- coding: utf-8 -*-
"""Exercicio1AM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GMMEvSJmwA689uAJ8Ig2Y9aYo7vHjKHS
"""

# Exercicio 1
# a = int(input("Lendo um número: "))
# print("imprimindo o numero", a)

del print

a = int(input("Quanto é seu salario por hora: "))
b = int(input("Quantas horas você trabalha por mês:"))
salb = a * b
print("Esse é seu salario bruto: ", salb)

inss = float(salb * 11)/100
print("Esse é o desconto do inss: ", inss)

ir = float((salb - inss)*8)/100
print("Esse é o desconto do imposto de renda: ", ir)

del print

sind = float((salb - inss - ir)*5)/100
print("Esse é o desconto do sindicato: ", sind)

sall = salb - inss - ir - sind
print("Esse é seu salario liquido: ", sall)