# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite a preço do produto R$'))

#conta = preço/100
#desconto = 10 

#desconto_total = desconto * conta 

#total = preço - desconto_total

novo = preço - (preço * 15 /100)




print(f'O preço do produto é R${preço} e o valor com desconto é de R${novo} ')