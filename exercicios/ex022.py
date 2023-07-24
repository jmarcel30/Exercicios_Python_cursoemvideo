"""Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""


nome = str(input('Digite seu nome completo'))
print(nome)

print(f'Seu nome é {nome.upper()}')
print(f'Seu nome é {nome.lower()}')
print(nome.strip().len(nome))