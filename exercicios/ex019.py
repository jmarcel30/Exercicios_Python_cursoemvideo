 #Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
#o nome do escolhido.
from random import choice
n1 =  str(input('Primeiro aluno'))
n2 =  str(input('Segundo aluno'))
n3 = str(input("Terceiro aluno"))
n4 = str(input('Quarto aluno'))

list = [n1, n2, n3, n4]
escolhido = choice(list)
print(f'O aluno escolhido foi o {escolhido}')