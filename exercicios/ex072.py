numero = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove', 'Dez','Onze','Doze',
          'Treze', 'Quatroze', 'Quinze', 'Dezesseis', 'Dezessete','Dezoito','Dezenovo','Vinte' )


num = int(input('Digite um numero entre 10 e 20:'))

if num > 20:
    print('Numero acima de Vinte, Digite outro numero')
else: print(f'O munero digitado foi {numero[num]}({num})')    

