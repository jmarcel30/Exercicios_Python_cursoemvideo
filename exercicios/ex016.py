#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input("Digite um numero"))

res = math.trunc(num)
print(f"O valor digitado é {num} e sua maior parte é {res}")

