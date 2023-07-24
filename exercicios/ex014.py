#: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp_c = float(input('Informe a temperatura em °C'))

#far = (temp_c * 1.8) + 32 
far = ((9 * temp_c) / 5 ) + 32

print(f"A temperatura é {far}")