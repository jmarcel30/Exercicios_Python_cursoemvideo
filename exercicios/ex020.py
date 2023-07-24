#: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
#e mostre a ordem sorteada.

import random

n1 = input('Nome do aulno')
n2 = input('Nome do aluno')
n3 = input('Nome do aulno')
n4 = input('Nome do aluno')

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(f"A ordem da lista é ?")
print(lista)