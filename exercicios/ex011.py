# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('EDigite a largura da parede'))
alt = float(input('Digite a altura da parede'))
area = larg * alt
tinta = area / 2 

print(f'Sua parede tem {larg} de latgura e {alt} de altura e sua area total e de {area}')
print(f'Você precisa de {tinta} litros de tinta ára íntar sua parede')
