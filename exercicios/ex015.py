 #Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
 #pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
#custa R$60 por dia e R$0,15 por Km rodado.


km_rodados = float(input('Quantos km '))
dias_alugados = int(input('Dias alugado'))

valor_km = km_rodados * 0.15 
valor_dias = dias_alugados * 60 
total = valor_km + valor_dias 

print(f'O valor para alugar o carro sai por km {valor_km} e por dia sai {valor_dias} o total fica {total}')

