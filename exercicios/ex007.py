# Desenvolva um programa que leia 4 notas e calcula a media

n1 = float(input('Digite a 1 nota'))
n2 = float(input('Digite a 2 nota'))
n3 = float(input('Digite a 3 nota'))
n4 = float(input('Digite a 4 nota'))

media = (n1 + n2 + n3 + n4) / 4 

print(f'Suas notas foram {n1}, {n2}, {n3}, {n4} e sua media final é {media:,.2f}')